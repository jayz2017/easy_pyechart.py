from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_scatter

_f=[]
_f.append(Faker.values())
_f.append(Faker.values())
easy_scatter.eScatter(title='ss',lableList=Faker.choose(),valueList=_f)._effectscatter().render("effectscatter_splitline.html")