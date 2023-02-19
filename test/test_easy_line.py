import pyecharts.options as opts
from pyecharts.charts import Line
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import baseParams,easy_line

_base=baseParams(title= '未来天气图')
week_name_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
high_temperature = [11, 11, 15, 13, 12, 13, 10]
low_temperature = [1, -2, 2, 5, 3, 2, 0]
_valueList=[
{
"name":"最高气温",
"value":high_temperature,
"setMarkPoint":[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ],
"setMarkLine":[opts.MarkLineItem(type_="average", name="平均值")],
},{
"name":"最低气温",
"value":low_temperature,
"setMarkPoint":[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)],
"setMarkLine":[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ],
}
]

easy_line.eLine(lableList=week_name_list,valueList=_valueList).basicLine(_base).render("temperature_change_line_chart.html")