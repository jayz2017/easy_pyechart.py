from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any,Optional
from pyecharts.charts import Bar,Line
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import _get_base_example,constants

'''封装柱状图'''
class eBar():
    def __init__(
        self,
        title:Optional[str] =None,
        subTitle:Optional[str] =None,
        lableList:Optional[list] = [],
        valueList:Optional[list] = [],
        legendsOpts:Optional[list] = [],
        themeType = constants.defualt_theme,
        isStack :bool =False ,
        isShowPercentage :bool =False ,
        backgroundImageUrl:Optional[str] =None,
        category_gap : Optional[str] ='50%'
    ):
        self.opts: dict = {
                           "lengend":Bar,
                           "title": title,
                           "subTitle" :subTitle,
                           "lableList":lableList,
                           "valueList":valueList,
                           "legendsOpts":legendsOpts,
                           "themeType":themeType,
                           "isStack":isStack,
                           "isShowPercentage":isShowPercentage,
                           "backgroundImageUrl":backgroundImageUrl,
                           "category_gap":category_gap
                           }
    #只有柱状图的图例
    def _stack_bar_percent(self): 
        return _get_base_example(self)
    
    #柱状图和折线图两种的混合图例
    def _mixed_bar_and_line(self,extraYname,extraLegendName,extraYList):
        _c = _get_base_example(self)
        _c.extend_axis(yaxis= opts.AxisOpts(
            name=extraYname,
            type_="value",
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            ))
        line = (
            Line()
            .add_xaxis(xaxis_data=self.opts['lableList'])
            .add_yaxis(
                series_name=extraLegendName,
                yaxis_index=1,
                y_axis=extraYList,
                label_opts=opts.LabelOpts(is_show=False),
            )
        )
        return  _c.overlap(line)
















