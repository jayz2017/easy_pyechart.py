import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_liquid,baseParams
from pyecharts import options as opts
from pyecharts.charts import Bar, Line

yList=[0.6,0.7]
#easy_liquid.eLiquid(valueList=yList).baseLiquid(baseParams(title='lail')).render("liquid_base.html")
easy_liquid.eLiquid(valueList=yList).precisionLiquid(baseParams(title='lail')).render("liquid_base.html")