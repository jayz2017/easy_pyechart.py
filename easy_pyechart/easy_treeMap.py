from pyecharts.charts import TreeMap
from typing import Optional
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import constants,baseParams,treeMap_base_config

class eTreeMap():
    def __init__(self,
                 dataList: Optional[list] = [],
                 ):
        self.opts: dict = {
            "lengend" : TreeMap,
            "dataList":dataList
        }

    def echarts_option(self,baseParams):
        self.opts.update(baseParams.opts)
        return treeMap_base_config(self)

















