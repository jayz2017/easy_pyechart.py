''''
并行坐标系的图例，能够展示各个数据相对于两外一组数据时的有关量
'''
from easy_pyechart import parallel_base_config, constants
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from typing import Any, Optional
from pyecharts.charts import Parallel
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Any, Optional, Union
from pyecharts.options.series_options import Numeric

class eParallel():
    def __init__(self,
                 #最右边设置的标签属性
                 lableList: Optional[list] = [],
                 schemaType : Optional[str] = 'category',
                 ydata :Optional[list] = [],
                 valueList: Optional[list] = [],
                 #线条是否变圆润
                 isSmooth:   bool = False,
                 #线条宽度
                 lineStyleWidth: Union[Numeric, int, None] = 2,
                 #表示lable 标签值的属性设置，是否时起始位置，起始位置为true
                 isLableStardFlag:bool = False,
                 ):
        self.opts: dict = {
            "lengend": Parallel,
            "lableList": lableList,
            "schemaType": schemaType,
            "valueList":valueList,
            "ydata": ydata,
            "isSmooth": isSmooth,
            "lineStyleWidth": lineStyleWidth,
            "isLableStardFlag":isLableStardFlag
        }

    def base_parallel(self,baseParams):
        self.opts.update(baseParams.opts)
        return parallel_base_config(self)







