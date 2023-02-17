from easy_pyechart import _gauge_base_config, constants
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional
from pyecharts.charts import Gauge
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def eGauge():
    def __init__(
            self,
            title: Optional[str] = None,
            subTitle: Optional[str] = None,
            seriesName: Optional[str] = None,
            dataList: Optional[list] = [],
            color : Optional[list] = [(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")],
            themeType=constants.defualt_theme,
            backgroundImageUrl: Optional[str] = None):
        self.opts: dict = {
            "lengend": Gauge,
            "seriesName": seriesName,
            "dataList": dataList,
            "themeType": themeType,
            "color":color,
            "backgroundImageUrl": backgroundImageUrl,
            "title": title,
            "subTitle": subTitle,
        }
        
    def excute_eGauge(self):
        return _gauge_base_config(self)