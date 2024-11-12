import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import baseParams, constants, line_base_config,gradientLine_base_config
from pyecharts.commons.utils import JsCode
import pyecharts.options as opts
from pyecharts.options.series_options import Numeric
from typing import Any, Optional, Union
from pyecharts.charts import Line


'''折线'''
class eLine():
    def __init__(self,
                 lableList: Optional[list] = [],
                 valueList: Optional[list] = [],
                 # 设置两个折点之间的连线是圆润，还是平直，true是圆润
                 isSmooth:   bool = False,
                 # 设置折线图与x轴之间的区域是否为阴影，true 会自动添加阴影
                 areastyleOpt: bool = False,
                 # 设置线的宽度
                 lineStyleWidth: Union[Numeric, int, None] = 2,
                 # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 
                 # 'pin', 'arrow', 'none'
                # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
                 symbolStype:Optional[str] = 'circle'
                 ):
        self.opts: dict = {
            "lengend": Line,
            "xList": lableList,
            "yList": valueList,
            "_is_smooth": isSmooth,
            "areastyleOpt": areastyleOpt,
            "lineStyleWidth": lineStyleWidth,
            "symbolStype":symbolStype
        }

    def basicLine(self, baseParams):
        self.opts.update(baseParams.opts)
        return line_base_config(self)

    # 上下两个x轴的数据图
    def up_down_x_line(self, baseParams, extraXlist):
        self.opts.update(baseParams.opts)
        js_formatter = """function (params) {
        return '' + params.value + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
        }"""

        xaxis = opts.AxisOpts(
            type_="category",
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#6e9ef1")
            ),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
            ),
        )
        self.opts["_xaxis"] = xaxis
        c = line_base_config(self)
        c.extend_axis(
            xaxis_data=extraXlist,
            xaxis=opts.AxisOpts(
                type_="category",
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                axisline_opts=opts.AxisLineOpts(
                    is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#6e9ef1")
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
                ),
            ),
        )
        c.set_global_opts(
            title_opts=opts.TitleOpts(title=self.opts['title']),
            legend_opts=opts.LegendOpts(),
            tooltip_opts=opts.TooltipOpts(
                trigger="none", axis_pointer_type="cross"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                axisline_opts=opts.AxisLineOpts(
                    is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        return c
    
    #渐变色的折线图，阴影部分呈现渐变的色彩效果
    def gradientLine(self, baseParams):
        self.opts.update(baseParams.opts)
        return gradientLine_base_config(self)


