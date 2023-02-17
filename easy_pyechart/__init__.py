from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional
'''
初始化图列的配置，
设置背景图片，或者是使用主题样式
'''
def _init_lengend(self):
    chart = self.opts['lengend']
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
        _img = """
            var img = new Image(); img.src = '{backgroundImageUrl}';
            """
        _img = _img.format(
            backgroundImageUrl=backgroundImageUrl).replace('\\', '\\\\')
        c.add_js_funcs(
            _img
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

    c=_init_lengend(self)
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
    #单行图列所布局分布
    layOutCenter = self.opts['layOutCenter']
    title = self.opts['title']
    subtitle = self.opts['subTitle']
    radius=self.opts['radius']

    c=_init_lengend(self)
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
        title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
        legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
    )
    return c

'''涟漪图基本配置'''
def scatter_base_config(self):
    xList = self.opts['xList']
    yList = self.opts['yList']
    title =  self.opts['title']
    subtitle =  self.opts['subTitle']
    _symbolType=self.opts['symbolType']
    c=_init_lengend(self)
    c.add_xaxis(xList)
    c.add_yaxis("", yList, symbol=_symbolType)
    c.set_global_opts(
        title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
    )
    return c

'''漏斗图基本配置项'''
def _funnel_base_config(self):
    xList = self.opts['xList']
    yList = self.opts['yList']
    title =  self.opts['title']
    subtitle =  self.opts['subTitle']
    data = [[xList[i], yList[i]] for i in range(len(xList))]
    c=_init_lengend(self)
    c.add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    c.set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle))
    return c
    
'''仪表盘的基本配置项'''
def _gauge_base_config(self):
    c=_init_lengend(self)
    seriesName = self.opts['seriesName']
    dataList = self.opts['dataList']
    c.add(series_name=seriesName, data_pair=dataList)
    c.set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )













































'''定义水印'''
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





