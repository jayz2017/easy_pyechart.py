from __future__ import annotations

import asyncio
import json
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from PIL import Image
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

from easy_pyechart.examples import list_examples
from easy_pyechart.factory import build_chart
from easy_pyechart.schemas import BatchRenderResponse, ChartRequest, ChartResponse, RenderFormat
from easy_pyechart.styles import get_chart_style


DEFAULT_WORKERS = min(32, (os.cpu_count() or 1) + 4)
DEFAULT_OUTPUT_DIR = Path(r"G:\echaet")
REQUEST_DIR_NAME = "requests"
HTML_DIR_NAME = "html"
IMAGE_DIR_NAME = "images"
GIF_DIR_NAME = "gifs"
LOG_DIR_NAME = "logs"
DEFAULT_GIF_CHART_TYPES = {"line", "liquid", "gauge", "graph", "sankey", "parallel"}
EDGE_PATHS = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]


class ChartRenderService:
    def __init__(
        self,
        output_dir: str | Path = DEFAULT_OUTPUT_DIR,
        max_workers: int | None = None,
        capture_images: bool = True,
    ) -> None:
        self.output_dir = Path(output_dir).resolve()
        self.capture_images = capture_images
        self.html_dir = self.output_dir / HTML_DIR_NAME
        self.image_dir = self.output_dir / IMAGE_DIR_NAME
        self.gif_dir = self.output_dir / GIF_DIR_NAME
        self.request_dir = self.output_dir / REQUEST_DIR_NAME
        self.log_dir = self.output_dir / LOG_DIR_NAME
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.html_dir.mkdir(parents=True, exist_ok=True)
        self.image_dir.mkdir(parents=True, exist_ok=True)
        self.gif_dir.mkdir(parents=True, exist_ok=True)
        self.request_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.log_dir / "render-history.jsonl"
        self.executor = ThreadPoolExecutor(max_workers=max_workers or DEFAULT_WORKERS)

    async def render(self, request: ChartRequest) -> ChartResponse:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self.executor, self._render_sync, request)

    async def render_all_examples(self) -> BatchRenderResponse:
        examples = list_examples()
        requests = []
        for chart_type, payload in examples.items():
            payload = {
                **payload,
                "render_format": RenderFormat.file,
                "output_path": f"{chart_type}.html",
                "capture_gif": chart_type in DEFAULT_GIF_CHART_TYPES,
            }
            requests.append(ChartRequest(**payload))
        rendered = []
        for request in requests:
            rendered.append(await self.render(request))
        self._write_manifest(rendered)
        return BatchRenderResponse(
            output_dir=str(self.output_dir),
            log_path=str(self.log_path),
            total=len(rendered),
            rendered=list(rendered),
        )

    def _render_sync(self, request: ChartRequest) -> ChartResponse:
        render_id = uuid4().hex
        chart = build_chart(request)
        if request.render_format == RenderFormat.file:
            output_path = self._resolve_output_path(request.output_path, request.chart_type.value)
            chart.render(str(output_path))
            request_path = self._write_request_file(render_id, request)
            image_path, image_error = self._capture_image(output_path, request.chart_type.value)
            gif_path, gif_error = self._capture_gif(output_path, request.chart_type.value) if request.capture_gif else (None, None)
            self._write_render_log(
                render_id,
                request,
                output_path,
                request_path,
                image_path,
                image_error,
                gif_path,
                gif_error,
            )
            message = "chart rendered to file"
            if not image_path:
                message += f"; image capture failed: {image_error}"
            if request.capture_gif and not gif_path:
                message += f"; gif capture failed: {gif_error}"
            return ChartResponse(
                chart_type=request.chart_type,
                render_format=request.render_format,
                output_path=str(output_path),
                image_path=str(image_path) if image_path else None,
                gif_path=str(gif_path) if gif_path else None,
                request_path=str(request_path),
                log_path=str(self.log_path),
                render_id=render_id,
                message=message,
            )

        html = chart.render_embed()
        request_path = self._write_request_file(render_id, request)
        self._write_render_log(render_id, request, None, request_path, None, None, None, None)
        return ChartResponse(
            chart_type=request.chart_type,
            render_format=request.render_format,
            html=html,
            request_path=str(request_path),
            log_path=str(self.log_path),
            render_id=render_id,
            message="chart rendered as html",
        )

    def _resolve_output_path(self, output_path: str | None, chart_type: str) -> Path:
        if output_path:
            candidate = Path(output_path)
            if candidate.is_absolute():
                raise ValueError("output_path must be a relative path under the configured output directory")
            target = (self.html_dir / candidate).resolve()
        else:
            target = (self.html_dir / f"{chart_type}-{uuid4().hex}.html").resolve()

        if not str(target).startswith(str(self.html_dir)):
            raise ValueError("output_path escapes the configured output directory")
        if target.suffix.lower() != ".html":
            target = target.with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        return target

    def _write_request_file(self, render_id: str, request: ChartRequest) -> Path:
        request_path = self.request_dir / f"{render_id}-{request.chart_type.value}.json"
        request_path.write_text(
            json.dumps(request.model_dump(mode="json"), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return request_path

    def _write_render_log(
        self,
        render_id: str,
        request: ChartRequest,
        output_path: Path | None,
        request_path: Path,
        image_path: Path | None,
        image_error: str | None,
        gif_path: Path | None,
        gif_error: str | None,
    ) -> None:
        style = get_chart_style(request.style)
        record = {
            "render_id": render_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "chart_type": request.chart_type.value,
            "render_format": request.render_format.value,
            "style": request.style,
            "palette": style.palette,
            "output_path": str(output_path) if output_path else None,
            "image_path": str(image_path) if image_path else None,
            "image_error": image_error,
            "gif_path": str(gif_path) if gif_path else None,
            "gif_error": gif_error,
            "request_path": str(request_path),
            "request": request.model_dump(mode="json"),
        }
        with self.log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

    def _write_manifest(self, rendered: list[ChartResponse]) -> None:
        manifest_path = self.output_dir / "latest-manifest.json"
        records = [
            {
                "chart_type": item.chart_type.value,
                "render_id": item.render_id,
                "html": item.output_path,
                "image": item.image_path,
                "gif": item.gif_path,
                "request": item.request_path,
                "log": item.log_path,
            }
            for item in rendered
        ]
        manifest_path.write_text(
            json.dumps(
                {
                    "created_at": datetime.now(timezone.utc).isoformat(),
                    "total": len(records),
                    "items": records,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    def _capture_image(self, html_path: Path, chart_type: str) -> tuple[Path | None, str | None]:
        if not self.capture_images:
            return None, "image capture disabled"
        image_path = self.image_dir / f"{chart_type}.png"
        edge_path = next((path for path in EDGE_PATHS if path.exists()), None)
        try:
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(
                    executable_path=str(edge_path) if edge_path else None,
                    headless=True,
                )
                page = browser.new_page(viewport={"width": 1280, "height": 860}, device_scale_factor=2)
                page.goto(html_path.as_uri(), wait_until="networkidle")
                page.wait_for_timeout(800)
                page.screenshot(path=str(image_path), full_page=True)
                browser.close()
            return image_path, None
        except PlaywrightError as exc:
            return None, str(exc)
        except Exception as exc:
            return None, str(exc)

    def _capture_gif(self, html_path: Path, chart_type: str) -> tuple[Path | None, str | None]:
        if not self.capture_images:
            return None, "image capture disabled"
        gif_path = self.gif_dir / f"{chart_type}.gif"
        frame_dir = self.gif_dir / "_frames" / chart_type
        frame_dir.mkdir(parents=True, exist_ok=True)
        edge_path = next((path for path in EDGE_PATHS if path.exists()), None)
        frame_paths = [frame_dir / f"{index:02d}.png" for index in range(8)]
        try:
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(
                    executable_path=str(edge_path) if edge_path else None,
                    headless=True,
                )
                page = browser.new_page(viewport={"width": 1280, "height": 860}, device_scale_factor=1)
                page.goto(html_path.as_uri(), wait_until="networkidle")
                page.wait_for_timeout(300)
                for frame_path in frame_paths:
                    page.screenshot(path=str(frame_path), full_page=True)
                    page.wait_for_timeout(250)
                browser.close()

            frames = [Image.open(frame_path).convert("P", palette=Image.Palette.ADAPTIVE) for frame_path in frame_paths]
            frames[0].save(
                gif_path,
                save_all=True,
                append_images=frames[1:],
                duration=250,
                loop=0,
                optimize=True,
            )
            for frame in frames:
                frame.close()
            return gif_path, None
        except PlaywrightError as exc:
            return None, str(exc)
        except Exception as exc:
            return None, str(exc)

    def shutdown(self) -> None:
        self.executor.shutdown(wait=True, cancel_futures=False)


def build_render_service() -> ChartRenderService:
    output_dir = os.getenv("EASY_PYECHART_OUTPUT_DIR", str(DEFAULT_OUTPUT_DIR))
    max_workers = int(os.getenv("EASY_PYECHART_MAX_WORKERS", str(DEFAULT_WORKERS)))
    capture_images = os.getenv("EASY_PYECHART_CAPTURE_IMAGES", "true").lower() not in {"0", "false", "no"}
    return ChartRenderService(output_dir=output_dir, max_workers=max_workers, capture_images=capture_images)
