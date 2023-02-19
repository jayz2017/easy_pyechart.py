from easy_pyechart import _grid_base_config, constants, set_water_marking, _set_logo_, _set_logo_ratate,_page_layout_base_config
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional
from pyecharts.charts import Grid
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 设置图表组合配装的方法实现
'''
Grid：并行多图是非常简单的一种合组的图列，grid 的属性比较少 ，图例是横着排放的

1：# 初始化配置项   init_opts
2：图例添加，   add
3：GridOpts：直角坐标系网格配置项

'''

class eGrid():
    def __init__(
        self,
        title: Optional[str] = None,
        subTitle: Optional[str] = None,
        charts: Optional[list] = [],
        themeType=constants.defualt_theme,
        backgroundImageUrl: Optional[str] = None,
    ):
        self.opts: dict = {
            "lengend": Grid,
            "title": title,
            "subTitle": subTitle,
            "charts": charts,
            "themeType": themeType,
            "backgroundImageUrl": backgroundImageUrl,
        }

    def excute(self):
        return _grid_base_config(self)

'''页面布局的图例使用，图例是竖着排放的'''
class ePage():
    def __init__(
        self,
        charts: Optional[list] = [],
    ):
        self.opts: dict = {
            "charts": charts,
        }
    def excute(self):
        return _page_layout_base_config(self)