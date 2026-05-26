from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType


DEFAULT_PALETTE = [
    "#2563EB",
    "#16A34A",
    "#F97316",
    "#DC2626",
    "#7C3AED",
    "#0891B2",
    "#DB2777",
    "#65A30D",
    "#475569",
    "#D97706",
]

SOFT_PALETTE = [
    "#4F46E5",
    "#0EA5E9",
    "#10B981",
    "#F59E0B",
    "#EF4444",
    "#8B5CF6",
    "#14B8A6",
    "#F43F5E",
]

DARK_PALETTE = [
    "#38BDF8",
    "#34D399",
    "#FBBF24",
    "#FB7185",
    "#A78BFA",
    "#2DD4BF",
    "#F472B6",
    "#A3E635",
]

AURORA_PALETTE = [
    "#00F5D4",
    "#00BBF9",
    "#F15BB5",
    "#FEE440",
    "#9B5DE5",
    "#FF6B6B",
    "#7CFFCB",
    "#FFB703",
]

NEON_PALETTE = [
    "#39FF14",
    "#00E5FF",
    "#FF2BD6",
    "#FFE66D",
    "#7B61FF",
    "#FF4D6D",
    "#2AF598",
    "#F9F871",
]

LUXE_PALETTE = [
    "#F7C948",
    "#F97316",
    "#E11D48",
    "#8B5CF6",
    "#06B6D4",
    "#10B981",
    "#FDE68A",
    "#F9A8D4",
]


@dataclass(frozen=True)
class ChartStyle:
    name: str
    theme: ThemeType | str
    palette: list[str]
    background_color: str
    text_color: str
    axis_color: str
    split_line_color: str
    title_color: str
    legend_text_color: str
    font_family: str = "Microsoft YaHei, Arial, sans-serif"
    glow_color: str = "rgba(0, 229, 255, 0.35)"
    is_dark: bool = False


STYLE_PRESETS: dict[str, ChartStyle] = {
    "business": ChartStyle(
        name="business",
        theme=ThemeType.LIGHT,
        palette=DEFAULT_PALETTE,
        background_color="#FFFFFF",
        text_color="#334155",
        axis_color="#94A3B8",
        split_line_color="#E2E8F0",
        title_color="#0F172A",
        legend_text_color="#475569",
    ),
    "fresh": ChartStyle(
        name="fresh",
        theme=ThemeType.WALDEN,
        palette=SOFT_PALETTE,
        background_color="#F8FAFC",
        text_color="#334155",
        axis_color="#CBD5E1",
        split_line_color="#E2E8F0",
        title_color="#111827",
        legend_text_color="#475569",
    ),
    "dark": ChartStyle(
        name="dark",
        theme=ThemeType.DARK,
        palette=DARK_PALETTE,
        background_color="#111827",
        text_color="#E5E7EB",
        axis_color="#64748B",
        split_line_color="rgba(148, 163, 184, 0.20)",
        title_color="#F8FAFC",
        legend_text_color="#CBD5E1",
        is_dark=True,
    ),
    "aurora": ChartStyle(
        name="aurora",
        theme=ThemeType.DARK,
        palette=AURORA_PALETTE,
        background_color="rgba(7, 10, 35, 1)",
        text_color="#DDF9FF",
        axis_color="rgba(148, 236, 255, 0.68)",
        split_line_color="rgba(111, 231, 255, 0.16)",
        title_color="#FFFFFF",
        legend_text_color="#DDF9FF",
        glow_color="rgba(0, 245, 212, 0.45)",
        is_dark=True,
    ),
    "neon": ChartStyle(
        name="neon",
        theme=ThemeType.DARK,
        palette=NEON_PALETTE,
        background_color="#05010D",
        text_color="#E9D5FF",
        axis_color="rgba(236, 72, 153, 0.65)",
        split_line_color="rgba(57, 255, 20, 0.14)",
        title_color="#FFFFFF",
        legend_text_color="#F5D0FE",
        glow_color="rgba(255, 43, 214, 0.55)",
        is_dark=True,
    ),
    "luxe": ChartStyle(
        name="luxe",
        theme=ThemeType.ROMA,
        palette=LUXE_PALETTE,
        background_color="#130B2A",
        text_color="#FFF7ED",
        axis_color="rgba(253, 230, 138, 0.62)",
        split_line_color="rgba(251, 191, 36, 0.14)",
        title_color="#FFF7ED",
        legend_text_color="#FDE68A",
        glow_color="rgba(247, 201, 72, 0.42)",
        is_dark=True,
    ),
}


def get_chart_style(style_name: str | None = None) -> ChartStyle:
    return STYLE_PRESETS.get(style_name or "aurora", STYLE_PRESETS["aurora"])


def gradient_background(style: ChartStyle) -> JsCode | str:
    if style.name == "aurora":
        return JsCode(
            "new echarts.graphic.RadialGradient(0.2, 0.15, 1.1, ["
            "{offset: 0, color: '#243B9F'},"
            "{offset: 0.38, color: '#081A44'},"
            "{offset: 0.72, color: '#10062B'},"
            "{offset: 1, color: '#020617'}])"
        )
    if style.name == "neon":
        return JsCode(
            "new echarts.graphic.LinearGradient(0, 0, 1, 1, ["
            "{offset: 0, color: '#05010D'},"
            "{offset: 0.45, color: '#1B0637'},"
            "{offset: 1, color: '#001B2E'}])"
        )
    if style.name == "luxe":
        return JsCode(
            "new echarts.graphic.LinearGradient(0, 0, 1, 1, ["
            "{offset: 0, color: '#130B2A'},"
            "{offset: 0.48, color: '#2D123A'},"
            "{offset: 1, color: '#4A1D1F'}])"
        )
    return style.background_color


def build_init_opts(style: ChartStyle, width: str = "1280px", height: str = "760px") -> opts.InitOpts:
    return opts.InitOpts(
        theme=style.theme,
        width=width,
        height=height,
        bg_color=gradient_background(style),
    )


def title_opts(title: str | None, subtitle: str | None, style: ChartStyle) -> opts.TitleOpts:
    return opts.TitleOpts(
        title=title or "",
        subtitle=subtitle or "",
        pos_left="3%",
        pos_top="3%",
        title_textstyle_opts=opts.TextStyleOpts(
            color=style.title_color,
            font_family=style.font_family,
            font_size=26,
            font_weight="bold",
            shadow_color=style.glow_color,
            shadow_blur=16,
        ),
        subtitle_textstyle_opts=opts.TextStyleOpts(
            color=style.text_color,
            font_family=style.font_family,
            font_size=13,
        ),
    )


def legend_opts(style: ChartStyle, pos_top: str = "6%") -> opts.LegendOpts:
    return opts.LegendOpts(
        pos_top=pos_top,
        pos_right="3%",
        item_width=16,
        item_height=10,
        textstyle_opts=opts.TextStyleOpts(
            color=style.legend_text_color,
            font_family=style.font_family,
        ),
    )


def tooltip_opts(trigger: str = "axis") -> opts.TooltipOpts:
    return opts.TooltipOpts(
        is_show=True,
        trigger=trigger,
        axis_pointer_type="shadow" if trigger == "axis" else None,
        background_color="rgba(7, 10, 35, 0.90)",
        border_color="rgba(255, 255, 255, 0.18)",
        border_width=1,
        textstyle_opts=opts.TextStyleOpts(color="#FFFFFF"),
    )


def category_axis_opts(style: ChartStyle, rotate: int = 0, boundary_gap: bool = True) -> opts.AxisOpts:
    return opts.AxisOpts(
        type_="category",
        boundary_gap=boundary_gap,
        axislabel_opts=opts.LabelOpts(color=style.text_color, rotate=rotate, margin=14),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(color=style.axis_color, width=2)
        ),
        axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
        splitline_opts=opts.SplitLineOpts(
            is_show=False,
            linestyle_opts=opts.LineStyleOpts(color=style.split_line_color),
        ),
    )


def value_axis_opts(style: ChartStyle) -> opts.AxisOpts:
    return opts.AxisOpts(
        type_="value",
        axislabel_opts=opts.LabelOpts(color=style.text_color, margin=12),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(color=style.axis_color, width=2)
        ),
        splitline_opts=opts.SplitLineOpts(
            is_show=True,
            linestyle_opts=opts.LineStyleOpts(color=style.split_line_color, width=1),
        ),
    )


def label_opts(style: ChartStyle, is_show: bool = False) -> opts.LabelOpts:
    return opts.LabelOpts(
        is_show=is_show,
        color=style.text_color,
        font_family=style.font_family,
        font_weight="bold",
    )


def item_style(color: str | None = None, opacity: float = 1) -> opts.ItemStyleOpts:
    return opts.ItemStyleOpts(
        color=color,
        opacity=opacity,
        border_color="rgba(255, 255, 255, 0.35)",
        border_width=1,
    )


def linear_gradient(start_color: str, end_color: str, horizontal: bool = False) -> JsCode:
    return JsCode(
        "new echarts.graphic.LinearGradient("
        f"{'0, 0, 1, 0' if horizontal else '0, 0, 0, 1'}, "
        f"[{{offset: 0, color: '{start_color}'}}, "
        f"{{offset: 1, color: '{end_color}'}}], false)"
    )


def area_gradient(start_color: str, end_color: str) -> JsCode:
    return linear_gradient(start_color, end_color)


def glow_graphics(style: ChartStyle) -> list[Any]:
    if not style.is_dark:
        return []
    return [
        opts.GraphicGroup(
            graphic_item=opts.GraphicItem(right="6%", top="4%", z=-8),
            children=[
                opts.GraphicRect(
                    graphic_item=opts.GraphicItem(left="center", top="center"),
                    graphic_shape_opts=opts.GraphicShapeOpts(width=260, height=160, r=80),
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill=style.glow_color,
                        shadow_blur=36,
                        shadow_color=style.glow_color,
                    ),
                )
            ],
        ),
        opts.GraphicGroup(
            graphic_item=opts.GraphicItem(left="3%", bottom="6%", z=-8),
            children=[
                opts.GraphicRect(
                    graphic_item=opts.GraphicItem(left="center", top="center"),
                    graphic_shape_opts=opts.GraphicShapeOpts(width=210, height=130, r=65),
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill="rgba(255, 255, 255, 0.10)",
                        shadow_blur=24,
                        shadow_color="rgba(255, 255, 255, 0.18)",
                    ),
                )
            ],
        ),
    ]


def apply_common_global_options(
    chart: Any,
    *,
    title: str | None,
    subtitle: str | None,
    style: ChartStyle,
    trigger: str = "axis",
    xaxis_opts: opts.AxisOpts | None = None,
    yaxis_opts: opts.AxisOpts | None = None,
) -> Any:
    chart.set_global_opts(
        title_opts=title_opts(title, subtitle, style),
        legend_opts=legend_opts(style),
        tooltip_opts=tooltip_opts(trigger),
        xaxis_opts=xaxis_opts,
        yaxis_opts=yaxis_opts,
        graphic_opts=glow_graphics(style),
    )
    return chart
