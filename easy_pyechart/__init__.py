from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional, Union
from easy_pyechart import constants
from pyecharts.options.series_options import Numeric
from pyecharts.charts import Page
import random
from pyecharts.options import ComponentTitleOpts

default_color_list=["#FFC125","#FF4040","#FF00FF","#C0FF3E","#9A32CD","#B03060","#48D1CC","#00EE00","#0000FF","#00F5FF","#228B22"]



class baseParams():
    def __init__(
        self,
        title: Optional[str] = None,
        subTitle: Optional[str] = None,
        themeType=constants.defualt_theme,
        backgroundImageUrl: Optional[str] = None,
    ):
        self.opts: dict = {
            "title": title,
            "subTitle": subTitle,
            "themeType": themeType,
            "backgroundImageUrl": backgroundImageUrl,
        }


'''位置上的定位定义类'''


class basePosition():
    def __init__(
        self,
        pos_left: Union[Numeric, str, None] = None,
        pos_top: Union[Numeric, str, None] = None,
        pos_right: Union[Numeric, str, None] = None,
        pos_bottom: Union[Numeric, str, None] = None
    ):
        self.opts: list = [
            pos_left,
            pos_right,
            pos_top,
            pos_bottom
        ]


'''
初始化图列的配置，
设置背景图片，或者是使用主题样式
'''


def _init_lengend(self):
    chart = self.opts['lengend']

    try:
        if self.opts['background_color_js'] != None:
            c = (
                chart(init_opts=opts.InitOpts(
                    bg_color=JsCode(self.opts['background_color_js']))
                )
            )
            return c
    except:
        # 这里的设置为异常什么都不干的原因是background_color_js是后来的属性，在没有做公共配置的其他图例中可能报错，为了不影响其他代码的执行
        ''

    backgroundImageUrl = self.opts['backgroundImageUrl']
    _initOpts = None
    if backgroundImageUrl != None and backgroundImageUrl.lstrip() != '':
        _initOpts = opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"})
    else:
        _initOpts = opts.InitOpts(theme=self.opts['themeType'])
    c = (
        chart(init_opts=_initOpts)
    )
    # 添加背景图片
    if backgroundImageUrl != None and backgroundImageUrl.lstrip() != '':
        _img = _setBackGroudImage_jsCode(backgroundImageUrl)
        c.add_js_funcs(
            _img
        )
    return c


def _init_grid_lengend(self):
    chart = self.opts['lengend']
    c = (
        chart(init_opts=opts.InitOpts(
            theme=self.opts['themeType'], width="1200px", height="800px"))
    )
    return c


'''柱状图的核心配置'''


def _get_base_example(self):
    title = self.opts['title']
    subtitle = self.opts['subTitle']
    if subtitle == None:
        subtitle = ''
    lableList = self.opts['lableList']
    valueList = self.opts['valueList']
    legendsOpts = self.opts['legendsOpts']
    isShowPercentage = self.opts['isShowPercentage']
    isStack = self.opts['isStack']
    backgroundImageUrl = self.opts['backgroundImageUrl']
    _category_gap = self.opts['category_gap']

    if lableList == None or type(lableList) != list or len(lableList) < 1:
        return None
    if valueList == None or type(valueList) != list or len(valueList) < 1:
        return None
    if legendsOpts == None or type(legendsOpts) != list or len(legendsOpts) < 1:
        return None

    c = _init_lengend(self)
    c.add_xaxis(lableList)
    for i in range(len(valueList)):
        # 是否堆叠
        if isStack == True:
            c.add_yaxis(legendsOpts[i], valueList[i],
                        stack="stack1", category_gap=_category_gap)
        else:
            c.add_yaxis(legendsOpts[i], valueList[i],
                        category_gap=_category_gap)

    if isShowPercentage != None and isShowPercentage == True:
        c.set_series_opts(
            label_opts=opts.LabelOpts(
                position="right",
                formatter=JsCode(
                    "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
                ),
            )
        )
    xaxis_opts_param = None
    _max_lable_ = max(lableList)
    if (type(_max_lable_) == str and len(_max_lable_) >= 5) or (type(_max_lable_) == int and _max_lable_ >= 1000):
        xaxis_opts_param = opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-15))
    datazoom_opts_par = None
    # 如果横坐标轴上的数据最多超过30个值，那么就开启压缩
    if len(lableList) > 30:
        datazoom_opts_par = opts.DataZoomOpts()
    try:
        c.set_global_opts(
            xaxis_opts=xaxis_opts_param,
            title_opts=opts.TitleOpts(title=title),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="shadow"),
            datazoom_opts=datazoom_opts_par
        )
    except:
        c.set_global_opts(
            xaxis_opts=xaxis_opts_param,
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="shadow"),
            datazoom_opts=datazoom_opts_par
        )
    return c


'''3D型柱状图配置'''


def _3D_base_config(self):
    chart = self.opts['lengend']
    _ydata = self.opts['ydata']
    x1_list = self.opts['x1_list']
    x2_list = self.opts['x2_list']
    chart.add(
        series_name="",
        data=_ydata,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=x1_list),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=x2_list),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )

    chart.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=20,
            range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
        )
    )
    return chart


'''饼状图的基本配置项'''


def pie_base_config(self):
    source_list = self.opts['sourceList']
    # 单行图列所布局分布
    layOutCenter = self.opts['layOutCenter']
    title = self.opts['title']
    subtitle = self.opts['subTitle']
    radius = self.opts['radius']

    c = _init_lengend(self)
    c.add_dataset(
        source=source_list
    )
    _lableList = source_list[0]
    _valueList = source_list[1:]
    for i in range(len(_valueList)):
        c.add(
            series_name=_valueList[i][0],
            data_pair=[],
            radius=radius,
            center=layOutCenter[i],
            encode={"itemName": _lableList[0], "value": _lableList[i+1]},
        )
    c.set_global_opts(
        title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
        legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
    )
    return c


'''涟漪图基本配置'''


def scatter_base_config(self):
    xList = self.opts['xList']
    yList = self.opts['yList']
    title = self.opts['title']
    subtitle = self.opts['subTitle']
    _symbolType = self.opts['symbolType']
    c = _init_lengend(self)
    c.add_xaxis(xList)
    c.add_yaxis("", yList, symbol=_symbolType)
    c.set_global_opts(
        title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
        xaxis_opts=opts.AxisOpts(
            splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(
            splitline_opts=opts.SplitLineOpts(is_show=True)),
    )
    return c


'''漏斗图基本配置项'''


def _funnel_base_config(self):
    xList = self.opts['xList']
    yList = self.opts['yList']
    title = self.opts['title']
    subtitle = self.opts['subTitle']
    data = [[xList[i], yList[i]] for i in range(len(xList))]
    c = _init_lengend(self)
    c.add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    c.set_global_opts(title_opts=opts.TitleOpts(
        title=title, subtitle=subtitle))
    return c


'''仪表盘的基本配置项'''


def _gauge_base_config(self):
    c = _init_lengend(self)
    seriesName = self.opts['seriesName']
    dataList = self.opts['dataList']
    _axisline_opts = None
    if self.opts['color'] != None:
        _axisline_opts = opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=self.opts['color'], width=30
            )
        )
    c.add(series_name=seriesName, data_pair=dataList,
          axisline_opts=_axisline_opts)
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title=self.opts['title'], subtitle=self.opts['subtitle']),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(
            is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    return c


'''关系图的基本配置项,简单的圆弧型设置的关系图'''


def _graph_base_config(self):
    _nodes = self.opts['nodes']
    _links = self.opts['links']
    _categories = self.opts['categories']
    c = _init_lengend(self)
    c.add(
        "",
        nodes=_nodes,
        links=_links,
        categories=_categories,
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
        label_opts=opts.LabelOpts(position="right"),
    )
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title=self.opts['title'], subtitle=self.opts['subtitle']),
        legend_opts=opts.LegendOpts(
            orient="vertical", pos_left="2%", pos_top="20%"),
    )
    return c


'''设置基本折线图的配置'''


def line_base_config(self):
    c = _init_lengend(self)
    _xaxis = None
    if self.opts['_xaxis'] != None:
        _xaxis = self.opts['_xaxis']
    try:
        c.add_xaxis(self.opts['xList'], xaxis=_xaxis)
    except:
        c.add_xaxis(self.opts['xList'])
    # 判断是否是圆润
    try:
        if self.opts['_is_smooth'] == True:
            _is_smooth = self.opts['_is_smooth']
    except:
        _is_smooth = None
    symbol = None
    symbol_size = None
    itemstyle_opts = None
    # 设置折线图上折点的样式
    if self.opts['symbolStype'] != None:
        symbol = self.opts['symbolStype'],
        symbol_size = 20,
        itemstyle_opts = opts.ItemStyleOpts(
            border_width=3
        )

    # 设置y轴的值
    for i in self.opts['yList']:
        _setMarkPoint = None
        _setMarkLine = None
        try:
            if i['setMarkPoint'] != None and len(i['setMarkPoint']) > 0:
                _setMarkPoint = opts.MarkPointOpts(
                    data=i['setMarkPoint']
                )
            if i['setMarkLine'] != None and len(i['setMarkLine']) > 0:
                _setMarkLine = opts.MarkLineOpts(
                    data=i['setMarkLine']
                )
        except:
            _setMarkPoint = None
            _setMarkLine = None

        if symbol != None:
            c.add_yaxis(
                series_name=i['name'],
                y_axis=i['value'],
                is_smooth=_is_smooth,
                markpoint_opts=_setMarkPoint,
                markline_opts=_setMarkLine,
                linestyle_opts=opts.LineStyleOpts(
                    width=self.opts['lineStyleWidth']),
                symbol=symbol,
                symbol_size=symbol_size,
                itemstyle_opts=itemstyle_opts
            )
        else:
            c.add_yaxis(
                series_name=i['name'],
                y_axis=i['value'],
                is_smooth=_is_smooth,
                markpoint_opts=_setMarkPoint,
                markline_opts=_setMarkLine,
                linestyle_opts=opts.LineStyleOpts(
                    width=self.opts['lineStyleWidth'])
            )
        # 如果横坐标的标签值比较长的话，就旋转一下
    xaxis_opts_param = None
    _max_lable_ = max(self.opts['xList'])
    if (type(_max_lable_) == str and len(_max_lable_) >= 5) or (type(_max_lable_) == int and _max_lable_ >= 1000):
        xaxis_opts_param = opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-15),
            type_="category", boundary_gap=False
        )
    else:
        xaxis_opts_param = opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            type_="category",  is_scale=False, boundary_gap=False
        )
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title=self.opts['title'], subtitle=self.opts['subTitle']),
        xaxis_opts=xaxis_opts_param,
    )

    # 设置阴影
    _areastyle_opts = None
    if self.opts['areastyleOpt'] == True:
        _areastyle_opts = opts.AreaStyleOpts(opacity=0.5)
    c.set_series_opts(
        areastyle_opts=_areastyle_opts,
        label_opts=opts.LabelOpts(is_show=True),
    )
    return c

# 渐变色的折线图配置


def gradientLine_base_config(self):
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
    )
    self.opts['background_color_js'] = background_color_js
    c = _init_lengend(self)
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
    )
    c.add_xaxis(xaxis_data=self.opts['xList'])

    for i in self.opts['yList']:
        c.add_yaxis(
            series_name=i['name'],
            y_axis=i['value'],
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(
                is_show=True, position="top", color="white"),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", border_color="#fff", border_width=3
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(
                color=JsCode(area_color_js), opacity=1),
        )

    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title=self.opts['title'],
            subtitle=self.opts['subTitle'],
            pos_bottom="5%",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#fff", font_size=16),
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
            axisline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(
                is_show=True,
                length=25,
                linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            position="right",
            axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
            ),
            axistick_opts=opts.AxisTickOpts(
                is_show=True,
                length=15,
                linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
            ),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    return c


# 水球图
def liquid_base_config(self):
    c = _init_lengend(self)
    label_opts = None
    if self.opts['labelOpts'] == True:
        label_opts = opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
            ),
            position="inside",
        )
    c.add("lq", self.opts['yList'], label_opts=label_opts)
    c.set_global_opts(title_opts=opts.TitleOpts(
        title=self.opts['title'], subtitle=self.opts['subTitle']))
    return c


# 平行坐标系图
def parallel_base_config(self):
    c = _init_lengend(self)
    schemaList = []
    _lableList = self.opts['lableList']
    for i in range(len(_lableList)):
        if self.opts['isLableStardFlag'] == True:
            if i == 0:
                schemaList.append(opts.ParallelAxisOpts(
                    dim=i,
                    name=_lableList[i],
                    type_=self.opts['schemaType'],
                    data=self.opts['ydata']
                )
                )
            else:
                schemaList.append(opts.ParallelAxisOpts(dim=i,
                                                        name=_lableList[i]
                                                        ))
        else:
            if i+1 == len(_lableList):
                schemaList.append(opts.ParallelAxisOpts(
                    dim=i,
                    name=_lableList[i],
                    type_=self.opts['schemaType'],
                    data=self.opts['ydata']
                )
                )
            else:
                schemaList.append(opts.ParallelAxisOpts(dim=i,
                                                        name=_lableList[i]
                                                        ))

    c.add_schema(schemaList)
    for i in self.opts['valueList']:
        c.add(i['name'], i['value'], is_smooth=self.opts['isSmooth'],
              linestyle_opts=opts.LineStyleOpts(width=self.opts['lineStyleWidth']))

    c.set_global_opts(title_opts=opts.TitleOpts(
        title=self.opts['title'], subtitle=self.opts['subTitle']))
    return c

'''饼状图基本配置'''
def double_pie_base_config(self):
    c = _init_lengend(self)
    #判断是否有富文本的标签展示
    _label_opts =opts.LabelOpts(is_show=False, position="center")
    for i in self.opts['dataList']:
        if i['isRichLabel'] == True:
            _label_opts =  opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                #is_show=True,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            )
        c.add(
            series_name = i['name'],
            data_pair= i['value'],
            rosetype= i ['type'],
            radius=i ['radius'],
            center=i ['centerLayOut'],
            label_opts=_label_opts,
        )
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title=self.opts['title'],
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        #legend_opts=opts.LegendOpts(is_show=False),
        legend_opts=opts.LegendOpts(orient="scroll", pos_top="15%", pos_left="2%" )
    )
    if self.opts['dataList'][0]['isRichLabel']==False:
        c.set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}: {c}"
            ),
            label_opts=opts.LabelOpts(color="red"),
        )
    return c

#雷达图的基本配置项
def radar_base_config(self):
    c = _init_lengend(self)
    _schema=[]
    for i in self.opts['lableList']:
        _schema.append(
            opts.RadarIndicatorItem(name=i["name"], max_=i["value"])
        )
    _color =random.sample(default_color_list, len(self.opts['valueList']))
    c.add_schema(   schema = _schema,
                    splitarea_opt=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)  ),
                    textstyle_opts=opts.TextStyleOpts(color=_color[0]),
                )
    
    for i in range(len(self.opts['valueList'])):
        _v = self.opts['valueList'][i]
        c.add(
             series_name= _v["name"],
            data=_v["value"],
            linestyle_opts=opts.LineStyleOpts(color=_color[i]),
        )

    c.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title=self.opts['title'],subtitle=self.opts['subTitle']), legend_opts=opts.LegendOpts(pos_left='legft',pos_top='15%',orient="vertical")
    )
    return c

#带有阴影区域设置的雷达图的基本配置项，而且图例的样式时圆形，而不是六角型
def round_radar_base_config(self):
    c = _init_lengend(self)
    c.set_colors(["#4587E7"])
    c.add_schema(
        schema=self.opts['lableList'],
        shape="circle",
        center=["50%", "50%"],
        radius="80%",
        angleaxis_opts=opts.AngleAxisOpts(
            min_=0,
            max_=360,
            is_clockwise=False,
            interval=5,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(
            min_=-4,
            max_=4,
            interval=2,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        polar_opts=opts.PolarOpts(),
        splitarea_opt=opts.SplitAreaOpts(is_show=False),
        splitline_opt=opts.SplitLineOpts(is_show=False),
    )
    c.add(
        series_name=self.opts['valueList'][0]['name'],
        data=self.opts['valueList'],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title=self.opts['title'],subtitle=self.opts['subTitle']), legend_opts=opts.LegendOpts(pos_left='legft',pos_top='15%',orient="vertical")
    )
    return c


#定义桑基图的基本配置项
def sankey_base_config(self):
    c=_init_lengend(self)
    c.add(
        self.opts['seriesName'],
        self.opts['lableList'],
        self.opts['valueList'],
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
        itemstyle_opts=opts.ItemStyleOpts(border_width=1, border_color="#aaa"),
        tooltip_opts=opts.TooltipOpts(trigger_on="mousemove"),

    )
    c.set_global_opts(title_opts=opts.TitleOpts(title=self.opts['title'],subtitle=self.opts['subTitle']), legend_opts=opts.LegendOpts(pos_left='right',pos_top='10%',orient="vertical"))
    return c

#定义table表格的基本配置
def table_base_config(self):
    table =self.opts['lengend']
    c= table()
    c.add(self.opts['headerList'], self.opts['rowList'])
    c.set_global_opts(
        title_opts=ComponentTitleOpts(title=self.opts['title'], subtitle=self.opts['subTitle'])
    )
    return c

#定义树类型的数据表格基本配置
def treeMap_base_config(self):
    table=self.opts['lengend']
    c= table()
    c.add(
        series_name="option",
        data=self.opts['dataList'],
        visual_min=300,
        leaf_depth=1,
        # 标签居中为 position = "inside"
        label_opts=opts.LabelOpts(position="inside"),
    )
    c.set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title=self.opts['title'],subtitle=self.opts['subTitle'], pos_left="leafDepth"
        ),
    )
    return c


'''定义水印 '''
def set_water_marking(waterText):
    return [
        opts.GraphicGroup(
            graphic_item=opts.GraphicItem(
                rotation=JsCode("Math.PI / 4"),
                bounding="raw",
                right=110,
                bottom=110,
                z=100,
            ),
            children=[
                opts.GraphicRect(
                    graphic_item=opts.GraphicItem(
                        left="center", top="center", z=100
                    ),
                    graphic_shape_opts=opts.GraphicShapeOpts(
                        width=400, height=50),
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill="rgba(0,0,0,0.3)"
                    ),
                ),
                opts.GraphicText(
                    graphic_item=opts.GraphicItem(
                        left="center", top="center", z=100
                    ),
                    graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                        text=waterText,
                        font="bold 26px Microsoft YaHei",
                        graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                            fill="#fff"
                        ),
                    ),
                ),
            ],
        )
    ]


'''设置引入小图片'''


def _set_logo_(imageUrl):
    return [
        opts.GraphicImage(
            graphic_item=opts.GraphicItem(
                id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]
            ),
            graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                image=imageUrl,
                width=150,
                height=150,
                opacity=0.4,
            ),
        )
    ]


'''这只logo 旋转的功能，为何返回的是字符串，原因是可以与设置背景图片的那段js代码向 公共使用'''


def _set_logo_ratate():
    return """
        var rotation = 0;
        setInterval(function () {
            chart_1234.setOption({
                graphic: {
                    id: 'logo',
                    rotation: (rotation += Math.PI / 360) % (Math.PI * 2)
                }
            });
        }, 30);
    """

# 设置背景图片的js操作代码


def _setBackGroudImage_jsCode(imageUrl):
    _img = """
            var img = new Image(); img.src = '{backgroundImageUrl}';
            """
    _img = _img.format(
        backgroundImageUrl=imageUrl).replace('\\', '\\\\')
    return _img


'''定义多个图表组合的页面配置方式，grid 平行组件'''


def _grid_base_config(self):
    c = _init_grid_lengend(self)
    _charts = self.opts['charts']
    for i in _charts:
        # 左右上下4个值
        _pos = i['position']
        if len(_pos) != 4:
            return
        c.add(i['chart'], grid_opts=opts.GridOpts(pos_left=_pos[0],
              pos_right=_pos[1], pos_top=_pos[2], pos_bottom=_pos[3]), is_control_axis_index=True)
    return c


'''页面组件的设置'''


def _page_layout_base_config(self):
    page = Page(layout=Page.DraggablePageLayout)
    for i in self.opts['charts']:
        page.add(i)
    return i
