from __future__ import annotations

from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator

from easy_pyechart.examples import BAR_EXAMPLE


class ChartType(str, Enum):
    bar = "bar"
    line = "line"
    pie = "pie"
    radar = "radar"
    sankey = "sankey"
    scatter = "scatter"
    treemap = "treemap"
    liquid = "liquid"
    gauge = "gauge"
    funnel = "funnel"
    graph = "graph"
    parallel = "parallel"
    grid = "grid"
    table = "table"


class RenderFormat(str, Enum):
    html = "html"
    file = "file"


class SeriesItem(BaseModel):
    name: str = Field(..., examples=["线上渠道"])
    data: list[Any] = Field(..., examples=[[120, 132, 101, 134]])


class ChartRequest(BaseModel):
    chart_type: ChartType = Field(..., description="图表类型")
    title: str | None = Field(default=None, description="图表标题")
    subtitle: str | None = Field(default=None, description="图表副标题")
    labels: list[Any] | None = Field(default=None, description="横轴标签或分类标签")
    series: list[SeriesItem] = Field(default_factory=list, description="系列数据")
    style: Literal["business", "fresh", "dark", "aurora", "neon", "luxe"] = Field(
        default="aurora",
        description="内置样式和配色方案",
    )
    render_format: RenderFormat = Field(
        default=RenderFormat.html,
        description="html 直接返回内容，file 保存 HTML 到输出目录",
    )
    output_path: str | None = Field(
        default=None,
        description="render_format=file 时的 HTML 相对输出路径",
    )
    stack: bool = Field(default=False, description="柱状图是否堆叠")
    smooth: bool = Field(default=True, description="折线图是否平滑")
    area: bool = Field(default=False, description="折线图是否显示面积阴影")
    capture_gif: bool = Field(default=False, description="是否额外输出 GIF 动图")
    nodes: list[dict[str, Any]] | None = Field(default=None, description="关系图或桑基图节点")
    links: list[dict[str, Any]] | None = Field(default=None, description="关系图或桑基图连线")
    categories: list[dict[str, Any]] | None = Field(default=None, description="关系图分类")
    indicators: list[dict[str, Any]] | None = Field(default=None, description="雷达图指标")
    tree_data: list[dict[str, Any]] | None = Field(default=None, description="矩形树图数据")

    model_config = {
        "json_schema_extra": {
            "examples": [BAR_EXAMPLE],
        }
    }

    @field_validator("series")
    @classmethod
    def validate_series(cls, value: list[SeriesItem]) -> list[SeriesItem]:
        if value is None:
            return []
        return value


class ChartResponse(BaseModel):
    chart_type: ChartType
    render_format: RenderFormat
    html: str | None = None
    output_path: str | None = None
    image_path: str | None = None
    gif_path: str | None = None
    request_path: str | None = None
    log_path: str | None = None
    render_id: str | None = None
    message: str


class ExampleResponse(BaseModel):
    chart_type: str
    request: dict[str, Any]


class BatchRenderResponse(BaseModel):
    output_dir: str
    log_path: str
    total: int
    rendered: list[ChartResponse]


class HealthResponse(BaseModel):
    status: str
    service: str
