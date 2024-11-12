import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pyecharts.charts import EffectScatter
from typing import Optional
from easy_pyechart import constants,scatter_base_config
from pyecharts.globals import SymbolType

class eScatter():
    def __init__(self,
                 title: Optional[str] = None,
                 subTitle: Optional[str] = None,
                 lableList: Optional[list] = [],
                 valueList: Optional[list] = [],
                 themeType=constants.defualt_theme,
                 backgroundImageUrl: Optional[str] = None,
                 symbolType = SymbolType.ARROW
                 ):
        self.opts: dict = {
            "lengend" : EffectScatter,
            "xList":lableList,
            "yList":valueList,
            "themeType":themeType,
            "backgroundImageUrl":backgroundImageUrl,
            "title":title,
            "subTitle":subTitle,
            "symbolType":symbolType
        }
    def _effectscatter(self):
        return scatter_base_config(self)