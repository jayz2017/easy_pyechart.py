from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any,Optional
from pyecharts.charts import Pie
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import pie_base_config,constants

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
    def dataset_pie(self):
        return pie_base_config(self)

