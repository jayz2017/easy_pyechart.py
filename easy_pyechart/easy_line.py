
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional
from pyecharts.charts import Line
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import baseParams, constants,line_base_config

class eLine():
    def __init__(self,
                 lableList: Optional[list] = [],
                 valueList: Optional[list] = [],
                 ):
        self.opts: dict = {
            "lengend" : Line,
            "xList": lableList,
            "yList": valueList,
        }
    def basicLine(self,baseParams):
        self.opts.update(baseParams.opts)
        return line_base_config(self)

