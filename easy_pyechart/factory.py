from __future__ import annotations

from typing import Any

from pyecharts import options as opts
from pyecharts.charts import Bar, EffectScatter, Funnel, Gauge, Graph, Grid, Line, Liquid, Parallel, Pie, Radar, Sankey, TreeMap
from pyecharts.components import Table

from easy_pyechart.schemas import ChartRequest, ChartType, SeriesItem
from easy_pyechart.styles import (
    apply_common_global_options,
    area_gradient,
    build_init_opts,
    category_axis_opts,
    get_chart_style,
    glow_graphics,
    item_style,
    label_opts,
    legend_opts,
    linear_gradient,
    title_opts,
    tooltip_opts,
    value_axis_opts,
)


def build_chart(request: ChartRequest) -> Any:
    builders = {
        ChartType.bar: build_bar_chart,
        ChartType.line: build_line_chart,
        ChartType.pie: build_pie_chart,
        ChartType.radar: build_radar_chart,
        ChartType.sankey: build_sankey_chart,
        ChartType.scatter: build_scatter_chart,
        ChartType.treemap: build_treemap_chart,
        ChartType.liquid: build_liquid_chart,
        ChartType.gauge: build_gauge_chart,
        ChartType.funnel: build_funnel_chart,
        ChartType.graph: build_graph_chart,
        ChartType.parallel: build_parallel_chart,
        ChartType.grid: build_grid_chart,
        ChartType.table: build_table_chart,
    }
    return builders[request.chart_type](request)


def build_bar_chart(request: ChartRequest) -> Bar:
    style = get_chart_style(request.style)
    chart = Bar(init_opts=build_init_opts(style))
    labels = _require_labels(request)
    chart.add_xaxis(labels)
    for index, series in enumerate(_require_series(request)):
        color = style.palette[index % len(style.palette)]
        end_color = style.palette[(index + 2) % len(style.palette)]
        chart.add_yaxis(
            series.name,
            series.data,
            stack="total" if request.stack else None,
            category_gap="36%",
            color=color,
            itemstyle_opts=item_style(linear_gradient(color, end_color)),
            label_opts=opts.LabelOpts(
                is_show=True,
                position="top",
                color=style.text_color,
                font_weight="bold",
            ),
        )
    rotate = -20 if _has_long_label(labels) else 0
    apply_common_global_options(
        chart,
        title=request.title,
        subtitle=request.subtitle,
        style=style,
        xaxis_opts=category_axis_opts(style, rotate=rotate),
        yaxis_opts=value_axis_opts(style),
    )
    if len(labels) > 30:
        chart.set_global_opts(datazoom_opts=opts.DataZoomOpts())
    return chart


def build_line_chart(request: ChartRequest) -> Line:
    style = get_chart_style(request.style)
    chart = Line(init_opts=build_init_opts(style))
    labels = _require_labels(request)
    chart.add_xaxis(labels)
    for index, series in enumerate(_require_series(request)):
        area_opts = None
        if request.area:
            color = style.palette[index % len(style.palette)]
            area_opts = opts.AreaStyleOpts(
                opacity=0.34,
                color=area_gradient(color, "rgba(255, 255, 255, 0.02)"),
            )
        color = style.palette[index % len(style.palette)]
        chart.add_yaxis(
            series.name,
            series.data,
            is_smooth=request.smooth,
            symbol="circle",
            symbol_size=10,
            color=color,
            linestyle_opts=opts.LineStyleOpts(width=5, color=color),
            itemstyle_opts=opts.ItemStyleOpts(color=color, border_color="#FFFFFF", border_width=2),
            label_opts=label_opts(style, is_show=False),
            areastyle_opts=area_opts,
        )
    rotate = -20 if _has_long_label(labels) else 0
    apply_common_global_options(
        chart,
        title=request.title,
        subtitle=request.subtitle,
        style=style,
        xaxis_opts=category_axis_opts(style, rotate=rotate, boundary_gap=False),
        yaxis_opts=value_axis_opts(style),
    )
    return chart


def build_pie_chart(request: ChartRequest) -> Pie:
    style = get_chart_style(request.style)
    chart = Pie(init_opts=build_init_opts(style))
    series = _require_series(request)[0]
    data_pair = _normalize_name_value_data(series.data)
    chart.add(
        series_name=series.name,
        data_pair=data_pair,
        radius=["34%", "68%"],
        center=["50%", "55%"],
        color=style.palette,
        rosetype="radius",
        itemstyle_opts=item_style(),
        label_opts=opts.LabelOpts(
            formatter="{b|{b}}\n{per|{d}%}",
            rich={
                "b": {"color": style.text_color, "fontSize": 13, "fontWeight": "bold"},
                "per": {"color": style.palette[3], "fontSize": 16, "fontWeight": "bold"},
            },
        ),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style, pos_top="10%"),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_radar_chart(request: ChartRequest) -> Radar:
    style = get_chart_style(request.style)
    chart = Radar(init_opts=build_init_opts(style))
    indicators = request.indicators or []
    if not indicators:
        raise ValueError("radar 图需要 indicators")
    chart.add_schema(
        schema=[
            opts.RadarIndicatorItem(
                name=str(item["name"]),
                max_=float(item.get("max", item.get("max_", 100))),
                min_=float(item.get("min", item.get("min_", 0))),
            )
            for item in indicators
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.12),
        ),
        textstyle_opts=opts.TextStyleOpts(color=style.text_color),
    )
    for index, series in enumerate(_require_series(request)):
        values = series.data
        if values and not isinstance(values[0], list):
            values = [values]
        chart.add(
            series.name,
            values,
            color=style.palette[index % len(style.palette)],
            areastyle_opts=opts.AreaStyleOpts(opacity=0.28),
            linestyle_opts=opts.LineStyleOpts(width=4, color=style.palette[index % len(style.palette)]),
        )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style, pos_top="8%"),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_sankey_chart(request: ChartRequest) -> Sankey:
    style = get_chart_style(request.style)
    nodes = request.nodes or []
    links = request.links or []
    if not nodes or not links:
        raise ValueError("sankey 图需要 nodes 和 links")
    chart = Sankey(init_opts=build_init_opts(style))
    chart.add(
        series_name=request.title or "sankey",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.55, curve=0.55, color="gradient"),
        label_opts=opts.LabelOpts(color=style.text_color, font_weight="bold"),
        itemstyle_opts=item_style(opacity=0.96),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_scatter_chart(request: ChartRequest) -> EffectScatter:
    style = get_chart_style(request.style)
    chart = EffectScatter(init_opts=build_init_opts(style))
    series = _require_series(request)[0]
    points = series.data
    if request.labels:
        chart.add_xaxis(request.labels)
        chart.add_yaxis(
            series.name,
            points,
            color=style.palette[0],
            symbol_size=18,
            label_opts=label_opts(style, is_show=False),
            itemstyle_opts=item_style(style.palette[0], opacity=0.92),
        )
    else:
        chart.add_xaxis([item[0] for item in points])
        chart.add_yaxis(
            series.name,
            [item[1] for item in points],
            color=style.palette[0],
            symbol_size=18,
            label_opts=label_opts(style, is_show=False),
            itemstyle_opts=item_style(style.palette[0], opacity=0.92),
        )
    apply_common_global_options(
        chart,
        title=request.title,
        subtitle=request.subtitle,
        style=style,
        xaxis_opts=value_axis_opts(style),
        yaxis_opts=value_axis_opts(style),
    )
    return chart


def build_treemap_chart(request: ChartRequest) -> TreeMap:
    style = get_chart_style(request.style)
    tree_data = request.tree_data or []
    if not tree_data:
        raise ValueError("treemap 图需要 tree_data")
    chart = TreeMap(init_opts=build_init_opts(style))
    chart.add(
        series_name=request.title or "treemap",
        data=tree_data,
        leaf_depth=1,
        label_opts=opts.LabelOpts(position="inside", color="#FFFFFF", font_weight="bold"),
        upper_label_opts=opts.LabelOpts(is_show=True, color=style.text_color),
        itemstyle_opts=item_style(opacity=0.95),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=tooltip_opts("item"),
        visualmap_opts=opts.VisualMapOpts(
            is_show=False,
            min_=0,
            max_=900,
            range_color=style.palette,
        ),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_liquid_chart(request: ChartRequest) -> Liquid:
    style = get_chart_style(request.style)
    series = _require_series(request)[0]
    chart = Liquid(init_opts=build_init_opts(style))
    chart.add(
        series.name,
        series.data,
        color=style.palette[:3],
        label_opts=opts.LabelOpts(
            font_size=40,
            color=style.title_color,
            formatter="{c}",
        ),
        outline_itemstyle_opts=opts.ItemStyleOpts(border_color=style.palette[0], border_width=6),
        background_color="rgba(255,255,255,0.08)",
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_gauge_chart(request: ChartRequest) -> Gauge:
    style = get_chart_style(request.style)
    series = _require_series(request)[0]
    chart = Gauge(init_opts=build_init_opts(style))
    chart.add(
        series_name=series.name,
        data_pair=_normalize_name_value_data(series.data),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.35, style.palette[1]), (0.75, style.palette[2]), (1, style.palette[3])],
                width=28,
            )
        ),
        detail_label_opts=opts.LabelOpts(
            formatter="{value}%",
            color=style.title_color,
            font_size=30,
        ),
        pointer=opts.GaugePointerOpts(width=8),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_funnel_chart(request: ChartRequest) -> Funnel:
    style = get_chart_style(request.style)
    series = _require_series(request)[0]
    data_pair = _normalize_label_series(request.labels, series.data)
    chart = Funnel(init_opts=build_init_opts(style))
    chart.add(
        series_name=series.name,
        data_pair=data_pair,
        gap=3,
        color=style.palette,
        label_opts=opts.LabelOpts(position="inside", color="#FFFFFF", font_weight="bold"),
        itemstyle_opts=item_style(opacity=0.95),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style, pos_top="10%"),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_graph_chart(request: ChartRequest) -> Graph:
    style = get_chart_style(request.style)
    nodes = request.nodes or []
    links = request.links or []
    if not nodes or not links:
        raise ValueError("graph 图需要 nodes 和 links")
    chart = Graph(init_opts=build_init_opts(style))
    chart.add(
        "",
        nodes=nodes,
        links=links,
        categories=request.categories or [],
        layout="force",
        repulsion=3200,
        gravity=0.08,
        edge_symbol=["none", "arrow"],
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.28, opacity=0.82, width=3),
        label_opts=opts.LabelOpts(position="right", color=style.text_color, font_weight="bold"),
        itemstyle_opts=item_style(opacity=0.96),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style, pos_top="10%"),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_parallel_chart(request: ChartRequest) -> Parallel:
    style = get_chart_style(request.style)
    labels = _require_labels(request)
    series = _require_series(request)[0]
    chart = Parallel(init_opts=build_init_opts(style))
    schema = []
    for index, label in enumerate(labels):
        values = [row[index] for row in series.data if len(row) > index]
        if values and all(isinstance(value, (int, float)) for value in values):
            schema.append(
                opts.ParallelAxisOpts(
                    dim=index,
                    name=str(label),
                    min_=min(values),
                    max_=max(values),
                )
            )
        else:
            schema.append(
                opts.ParallelAxisOpts(
                    dim=index,
                    name=str(label),
                    type_="category",
                    data=sorted({str(value) for value in values}),
                )
            )
    chart.add_schema(schema=schema)
    chart.add(
        series.name,
        series.data,
        linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.78, color=style.palette[1]),
    )
    chart.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style, pos_top="8%"),
        tooltip_opts=tooltip_opts("item"),
        graphic_opts=glow_graphics(style),
    )
    return chart


def build_grid_chart(request: ChartRequest) -> Grid:
    style = get_chart_style(request.style)
    labels = _require_labels(request)
    series = _require_series(request)
    if len(series) < 2:
        raise ValueError("grid 图至少需要两个 series")

    bar = Bar(init_opts=build_init_opts(style))
    bar.add_xaxis(labels)
    bar.add_yaxis(
        series[0].name,
        series[0].data,
        color=style.palette[0],
        itemstyle_opts=item_style(linear_gradient(style.palette[0], style.palette[2])),
        label_opts=label_opts(style, is_show=True),
    )
    bar.set_global_opts(
        title_opts=title_opts(request.title, request.subtitle, style),
        legend_opts=legend_opts(style, pos_top="8%"),
        tooltip_opts=tooltip_opts(),
        xaxis_opts=category_axis_opts(style),
        yaxis_opts=value_axis_opts(style),
    )

    line = Line()
    line.add_xaxis(labels)
    line.add_yaxis(
        series[1].name,
        series[1].data,
        color=style.palette[1],
        is_smooth=True,
        label_opts=label_opts(style, is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=5, color=style.palette[1]),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.24, color=area_gradient(style.palette[1], "rgba(255,255,255,0.02)")),
    )
    line.set_global_opts(
        xaxis_opts=category_axis_opts(style),
        yaxis_opts=value_axis_opts(style),
        legend_opts=legend_opts(style, pos_top="8%"),
    )

    grid = Grid(init_opts=build_init_opts(style, height="860px"))
    grid.add(bar, grid_opts=opts.GridOpts(pos_left="7%", pos_right="7%", pos_top="12%", pos_bottom="58%"))
    grid.add(line, grid_opts=opts.GridOpts(pos_left="7%", pos_right="7%", pos_top="56%", pos_bottom="10%"))
    return grid


def build_table_chart(request: ChartRequest) -> Table:
    labels = [str(label) for label in _require_labels(request)]
    series = _require_series(request)[0]
    table = Table()
    table.add(labels, series.data)
    table.set_global_opts(
        title_opts=opts.ComponentTitleOpts(
            title=request.title or "",
            subtitle=request.subtitle or "",
        )
    )
    return table


def _require_labels(request: ChartRequest) -> list[Any]:
    if not request.labels:
        raise ValueError(f"{request.chart_type.value} 图需要 labels")
    return request.labels


def _require_series(request: ChartRequest) -> list[SeriesItem]:
    if not request.series:
        raise ValueError(f"{request.chart_type.value} 图需要 series")
    return request.series


def _has_long_label(labels: list[Any]) -> bool:
    return any(len(str(label)) >= 5 for label in labels)


def _normalize_name_value_data(data: list[Any]) -> list[list[Any]]:
    data_pair: list[list[Any]] = []
    for item in data:
        if isinstance(item, dict):
            data_pair.append([item.get("name"), item.get("value")])
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            data_pair.append([item[0], item[1]])
        else:
            raise ValueError("数据项需要是 {'name': ..., 'value': ...} 或 [name, value]")
    return data_pair


def _normalize_label_series(labels: list[Any] | None, values: list[Any]) -> list[list[Any]]:
    if values and isinstance(values[0], dict):
        return _normalize_name_value_data(values)
    if not labels:
        raise ValueError("该图需要 labels 或 name/value 数据")
    if len(labels) != len(values):
        raise ValueError("labels 和 series.data 长度不一致")
    return [[label, value] for label, value in zip(labels, values)]
