import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import _funnel_base_config, constants
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional
from pyecharts.charts import Funnel


'''漏斗图'''
class eFunnel():
    def __init__(
            self,
            title: Optional[str] = None,
            subTitle: Optional[str] = None,
            lableList: Optional[list] = [],
            valueList: Optional[list] = [],
            themeType=constants.defualt_theme,
            backgroundImageUrl: Optional[str] = None):
        self.opts: dict = {
            "lengend": Funnel,
            "xList": lableList,
            "yList": valueList,
            "themeType": themeType,
            "backgroundImageUrl": backgroundImageUrl,
            "title": title,
            "subTitle": subTitle,
        }
    '''三角形的漏斗图设置'''
    def _funnel_chart(self):
        return _funnel_base_config(self)
    