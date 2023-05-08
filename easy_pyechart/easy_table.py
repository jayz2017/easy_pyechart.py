from pyecharts import options as opts
from typing import Any,Optional
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import constants,baseParams,table_base_config
import matplotlib.pyplot as plt

class eTable():
    def __init__(
        self,
        headerList:Optional[list] = [],
        rowList:Optional[list] = [],
          columnColor:Optional[list] = []
    ):
        self.opts: dict = {
                           "lengend":Table,
                           "headerList":headerList,
                           "rowList":rowList,
                           }
        
    def base_table(self,baseParams):
        self.opts.update(baseParams.opts)
        return table_base_config(self)

class eMTable():
    def __init__(
        self,
        rowList:Optional[list] = [],
        columnColor:Optional[list] = [],
        outSaveUrl:Optional[str] =None
        ):
        self.opts: dict = {
                           "lengend":Table,
                           "columnColor":columnColor,
                           "rowList":rowList,
                           'outSaveUrl':outSaveUrl
                           }
    def base_table(self):
        fig, ax = plt.subplots()    
        # 隐藏坐标轴
        ax.axis("off")
        table = ax.table(cellText=self.opts['rowList'], cellColours=self.opts['columnColor'], loc="center")
        table.set_edges("closed")
        plt.savefig(self.opts['outSaveUrl'])



