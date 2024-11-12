import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pyecharts import options as opts
from typing import Any,Optional
from pyecharts.charts import Sankey
from easy_pyechart import constants,baseParams,sankey_base_config

class eSankey():
    def __init__(
        self,
        seriesName:Optional[str] = None,
        lableList:Optional[list] = [],
        valueList:Optional[list] = [],
    ):
        self.opts: dict = {
                           "lengend":Sankey,
                           "seriesName":seriesName,
                           "lableList":lableList,
                           "valueList":valueList,
                           }

    def sankey_base(self,baseParams):
        self.opts.update(baseParams.opts)
        return sankey_base_config(self)