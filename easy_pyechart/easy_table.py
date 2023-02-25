from pyecharts import options as opts
from typing import Any,Optional
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import constants,baseParams,table_base_config


class eTable():
    def __init__(
        self,
        headerList:Optional[list] = [],
        rowList:Optional[list] = [],
        valueList:Optional[list] = [],
    ):
        self.opts: dict = {
                           "lengend":Table,
                           "headerList":headerList,
                           "rowList":rowList,
                           }
        
    def base_table(self,baseParams):
        self.opts.update(baseParams.opts)
        return table_base_config(self)









