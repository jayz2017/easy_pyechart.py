import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import baseParams, constants, liquid_base_config
from pyecharts.options.series_options import Numeric
from typing import Any, Optional
from pyecharts.charts import Liquid


#水球图
class eLiquid():
    def __init__(self,
                 valueList: Optional[list] = [],
                 labelOpts:bool =False
                 ):
        self.opts: dict = {
            "lengend": Liquid,
            "yList": valueList,
            "labelOpts":labelOpts
        }

    def baseLiquid(self, baseParams):
        self.opts.update(baseParams.opts)
        return liquid_base_config(self)

    def precisionLiquid(self, baseParams):
        self.opts.update(baseParams.opts)
        self.opts['labelOpts']=True
        return liquid_base_config(self)