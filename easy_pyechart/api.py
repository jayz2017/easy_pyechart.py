from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from easy_pyechart.examples import get_example, list_examples
from easy_pyechart.schemas import (
    BatchRenderResponse,
    ChartRequest,
    ChartResponse,
    ExampleResponse,
    HealthResponse,
    RenderFormat,
)
from easy_pyechart.services import ChartRenderService, build_render_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    service = build_render_service()
    app.state.render_service = service
    try:
        yield
    finally:
        service.shutdown()


app = FastAPI(
    title="Easy PyEChart API",
    description="统一图表渲染服务，Swagger 请求体中内置柱状图模拟数据，可通过示例接口获取其他图例数据。",
    version="0.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)


def get_render_service() -> ChartRenderService:
    return app.state.render_service


@app.get("/health", response_model=HealthResponse, tags=["system"])
async def health() -> HealthResponse:
    return HealthResponse(status="ok", service="easy-pyechart-api")


@app.get("/api/v1/examples", tags=["examples"])
async def examples() -> dict[str, dict]:
    return list_examples()


@app.get("/api/v1/examples/{chart_type}", response_model=ExampleResponse, tags=["examples"])
async def example(chart_type: str = "bar") -> ExampleResponse:
    return ExampleResponse(chart_type=chart_type, request=get_example(chart_type))


@app.post("/api/v1/charts/render", response_model=ChartResponse, tags=["charts"])
async def render_chart(request: ChartRequest) -> ChartResponse:
    try:
        return await get_render_service().render(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/v1/charts/render/examples", response_model=BatchRenderResponse, tags=["charts"])
async def render_all_examples() -> BatchRenderResponse:
    try:
        return await get_render_service().render_all_examples()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/v1/charts/render/html", response_class=HTMLResponse, tags=["charts"])
async def render_chart_html(request: ChartRequest) -> HTMLResponse:
    request = request.model_copy(update={"render_format": RenderFormat.html})
    try:
        response = await get_render_service().render(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return HTMLResponse(response.html or "")
