from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any,Optional
from pyecharts.charts import Pie
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import pie_base_config,constants,double_pie_base_config

class epie():
    def __init__(
        self,
        title:Optional[str] =None,
        subTitle:Optional[str] =None,
        sourceList:Optional[list] = [],
        themeType = constants.defualt_theme,
        layOutCenter:Optional[list] = [],
        radius:Optional[int]=60,
        backgroundImageUrl:Optional[str] =None,
    ):
        self.opts: dict = {
                           "lengend":Pie,
                           "title": title,
                           "subTitle" :subTitle,
                           "sourceList":sourceList,
                           "themeType":themeType,
                           "layOutCenter":layOutCenter,
                           "radius":radius,
                           "backgroundImageUrl":backgroundImageUrl,
                           }
        #简单的单个饼状图模型
    def dataset_pie(self):
        return pie_base_config(self)
    
    #复杂的饼状图模型，可以设置饼图的样式，以及叠加多个饼图
    def double_pie(self,dataList):
        self.opts['dataList'] = dataList
        return double_pie_base_config(self)


