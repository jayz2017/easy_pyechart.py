from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any,Optional
from pyecharts.charts import Graph
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import baseParams,_graph_base_config

'''
圆弧型的关系图
'''
class eGraph():
    def __init__(
        self,
        nodes:Optional[list] = [],
        links:Optional[list] = [],
        categories:Optional[list] = [],
    ):
        self.opts: dict = {
                           "lengend":Graph,
                           "nodes":nodes,
                           "links":links,
                           "categories":categories
                           }
          
    def excute_eGraph(self,baseParams):
        self.opts.update(baseParams.opts)
        return _graph_base_config(self)    
