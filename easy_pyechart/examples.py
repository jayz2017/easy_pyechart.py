from __future__ import annotations

from copy import deepcopy
from typing import Any


BAR_EXAMPLE: dict[str, Any] = {
    "chart_type": "bar",
    "title": "全渠道销售能量",
    "subtitle": "高亮渐变柱图 · Swagger 示例数据",
    "labels": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "series": [
        {"name": "线上渠道", "data": [120, 132, 101, 134, 190, 230]},
        {"name": "线下渠道", "data": [80, 92, 110, 125, 145, 170]},
    ],
    "style": "aurora",
    "stack": False,
    "render_format": "html",
}

LINE_EXAMPLE: dict[str, Any] = {
    "chart_type": "line",
    "title": "用户增长脉冲",
    "subtitle": "霓虹曲线 · 面积流光",
    "labels": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
    "series": [
        {"name": "新增用户", "data": [120, 180, 150, 260, 300, 420, 390]},
        {"name": "活跃用户", "data": [320, 360, 340, 420, 480, 530, 510]},
    ],
    "style": "neon",
    "smooth": True,
    "area": True,
    "render_format": "html",
}

PIE_EXAMPLE: dict[str, Any] = {
    "chart_type": "pie",
    "title": "流量来源星环",
    "subtitle": "玫瑰环图 · 高对比标签",
    "series": [
        {
            "name": "来源",
            "data": [
                {"name": "搜索", "value": 335},
                {"name": "广告", "value": 310},
                {"name": "邮件", "value": 234},
                {"name": "直接访问", "value": 135},
                {"name": "社交媒体", "value": 148},
            ],
        }
    ],
    "style": "luxe",
    "render_format": "html",
}

RADAR_EXAMPLE: dict[str, Any] = {
    "chart_type": "radar",
    "title": "团队能力光谱",
    "subtitle": "雷达扫描 · 半透明能量面",
    "indicators": [
        {"name": "销售", "max": 100},
        {"name": "运营", "max": 100},
        {"name": "技术", "max": 100},
        {"name": "客服", "max": 100},
        {"name": "市场", "max": 100},
    ],
    "series": [
        {"name": "团队 A", "data": [82, 90, 78, 86, 73]},
        {"name": "团队 B", "data": [70, 76, 88, 72, 91]},
    ],
    "style": "aurora",
    "render_format": "html",
}

SANKEY_EXAMPLE: dict[str, Any] = {
    "chart_type": "sankey",
    "title": "用户转化流光",
    "subtitle": "渐变流线 · 转化路径",
    "nodes": [
        {"name": "访问"},
        {"name": "注册"},
        {"name": "试用"},
        {"name": "付费"},
        {"name": "流失"},
    ],
    "links": [
        {"source": "访问", "target": "注册", "value": 500},
        {"source": "注册", "target": "试用", "value": 320},
        {"source": "试用", "target": "付费", "value": 180},
        {"source": "试用", "target": "流失", "value": 140},
    ],
    "style": "neon",
    "render_format": "html",
}

SCATTER_EXAMPLE: dict[str, Any] = {
    "chart_type": "scatter",
    "title": "投入产出星图",
    "subtitle": "散点脉冲 · 门店表现",
    "series": [
        {
            "name": "门店",
            "data": [[10, 120], [20, 180], [30, 260], [42, 310], [55, 420]],
        }
    ],
    "style": "aurora",
    "render_format": "html",
}

TREEMAP_EXAMPLE: dict[str, Any] = {
    "chart_type": "treemap",
    "title": "产品销售星云",
    "subtitle": "矩形树图 · 层级结构",
    "tree_data": [
        {
            "name": "硬件",
            "value": 820,
            "children": [
                {"name": "笔记本", "value": 420},
                {"name": "显示器", "value": 260},
                {"name": "配件", "value": 140},
            ],
        },
        {
            "name": "软件",
            "value": 610,
            "children": [
                {"name": "订阅", "value": 430},
                {"name": "服务", "value": 180},
            ],
        },
    ],
    "style": "luxe",
    "render_format": "html",
}

LIQUID_EXAMPLE: dict[str, Any] = {
    "chart_type": "liquid",
    "title": "目标完成能量球",
    "subtitle": "液态波纹 · 进度视觉",
    "series": [{"name": "完成率", "data": [0.68, 0.72]}],
    "style": "neon",
    "render_format": "html",
}

GAUGE_EXAMPLE: dict[str, Any] = {
    "chart_type": "gauge",
    "title": "服务达成仪表",
    "subtitle": "金色刻度 · SLA 状态",
    "series": [{"name": "达成率", "data": [{"name": "SLA", "value": 87}]}],
    "style": "luxe",
    "render_format": "html",
}

FUNNEL_EXAMPLE: dict[str, Any] = {
    "chart_type": "funnel",
    "title": "转化漏斗光束",
    "subtitle": "分层漏斗 · 转化能量",
    "labels": ["访问", "注册", "试用", "下单", "支付"],
    "series": [{"name": "转化", "data": [1000, 620, 360, 220, 160]}],
    "style": "aurora",
    "render_format": "html",
}

GRAPH_EXAMPLE: dict[str, Any] = {
    "chart_type": "graph",
    "title": "业务关系星系",
    "subtitle": "力导向关系 · 节点发光",
    "nodes": [
        {"name": "产品", "symbolSize": 65},
        {"name": "用户", "symbolSize": 52},
        {"name": "订单", "symbolSize": 48},
        {"name": "渠道", "symbolSize": 42},
    ],
    "links": [
        {"source": "用户", "target": "订单"},
        {"source": "订单", "target": "产品"},
        {"source": "渠道", "target": "用户"},
    ],
    "categories": [{"name": "业务对象"}],
    "style": "neon",
    "render_format": "html",
}

PARALLEL_EXAMPLE: dict[str, Any] = {
    "chart_type": "parallel",
    "title": "门店运营光谱",
    "subtitle": "平行坐标 · 多指标对比",
    "labels": ["门店", "客流", "转化率", "客单价", "复购率", "等级"],
    "series": [
        {
            "name": "门店指标",
            "data": [
                ["A店", 820, 0.32, 168, 0.42, "优秀"],
                ["B店", 620, 0.28, 152, 0.36, "良好"],
                ["C店", 760, 0.35, 181, 0.48, "优秀"],
                ["D店", 540, 0.22, 139, 0.29, "关注"],
            ],
        }
    ],
    "style": "aurora",
    "render_format": "html",
}

GRID_EXAMPLE: dict[str, Any] = {
    "chart_type": "grid",
    "title": "收入与订单双屏",
    "subtitle": "上下组合 · 柱线联动",
    "labels": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "series": [
        {"name": "收入", "data": [120, 132, 151, 174, 210, 236]},
        {"name": "订单", "data": [220, 282, 291, 334, 390, 430]},
    ],
    "style": "luxe",
    "render_format": "html",
}

TABLE_EXAMPLE: dict[str, Any] = {
    "chart_type": "table",
    "title": "KPI 数据看板",
    "subtitle": "表格示例 · 追踪用基础数据",
    "labels": ["指标", "本月", "上月", "同比", "状态"],
    "series": [
        {
            "name": "KPI",
            "data": [
                ["销售额", "236万", "210万", "+12.4%", "达成"],
                ["订单量", "430", "390", "+10.3%", "达成"],
                ["客单价", "5480", "5385", "+1.8%", "观察"],
                ["复购率", "42%", "39%", "+3.0%", "达成"],
            ],
        }
    ],
    "style": "luxe",
    "render_format": "html",
}

EXAMPLES: dict[str, dict[str, Any]] = {
    "bar": BAR_EXAMPLE,
    "line": LINE_EXAMPLE,
    "pie": PIE_EXAMPLE,
    "radar": RADAR_EXAMPLE,
    "sankey": SANKEY_EXAMPLE,
    "scatter": SCATTER_EXAMPLE,
    "treemap": TREEMAP_EXAMPLE,
    "liquid": LIQUID_EXAMPLE,
    "gauge": GAUGE_EXAMPLE,
    "funnel": FUNNEL_EXAMPLE,
    "graph": GRAPH_EXAMPLE,
    "parallel": PARALLEL_EXAMPLE,
    "grid": GRID_EXAMPLE,
    "table": TABLE_EXAMPLE,
}


def get_example(chart_type: str = "bar") -> dict[str, Any]:
    return deepcopy(EXAMPLES.get(chart_type, BAR_EXAMPLE))


def list_examples() -> dict[str, dict[str, Any]]:
    return deepcopy(EXAMPLES)
