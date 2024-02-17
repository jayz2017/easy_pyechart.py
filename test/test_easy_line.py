import pyecharts.options as opts
from pyecharts.charts import Line
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import baseParams,easy_line,save_static_image

def baseLine():
    _base=baseParams(title= '未来天气图')
    week_name_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    high_temperature = [11, 11, 15, 13, 12, 13, 10]
    low_temperature = [1, -2, 2, 5, 3, 2, 0]
    _valueList=[
    {
    "name":"最高气温",
    "value":high_temperature,
    # "setMarkPoint":[
    #                 opts.MarkPointItem(type_="max", name="最大值"),
    #                 opts.MarkPointItem(type_="min", name="最小值"),
    #             ],
    # "setMarkLine":[opts.MarkLineItem(type_="average", name="平均值")],
    },{
    "name":"最低气温",
    "value":low_temperature,
    # "setMarkPoint":[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)],
    # "setMarkLine":[
    #                 opts.MarkLineItem(type_="average", name="平均值"),
    #                 opts.MarkLineItem(symbol="none", x="90%", y="max"),
    #                 opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
    #             ],
    }
    ]
    for i in range(len(_valueList)):
            if(i==0):
                _valueList[i]['setMarkPoint']=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                    ]
                _valueList[i]['setMarkLine']=[opts.MarkLineItem(type_="average", name="平均值")]
            else:
                _valueList[i]['setMarkPoint']=[opts.MarkPointItem(value=min(_valueList[i]['value']), name="周最低", x=1, y=-1.5)]   
                _valueList[i]['setMarkLine']=[
                    opts.MarkLineItem(type_="average", name="平均值"),
                    opts.MarkLineItem(symbol="none", x="90%", y="max"),
                    opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
                ]

    easy_line.eLine(lableList=week_name_list,valueList=_valueList,areastyleOpt=True,isSmooth=True).basicLine(_base).render("temperature_change_line_chart.html")

#baseLine()

def upDownLine():
    #第一个x轴的数据集合
    xList= [
            "2016-1",
            "2016-2",
            "2016-3",
            "2016-4",
            "2016-5",
            "2016-6",
            "2016-7",
            "2016-8",
            "2016-9",
            "2016-10",
            "2016-11",
            "2016-12",
        ]
    #第二个x轴的数据集合
    extra_xList =[
            "2015-1",
            "2015-2",
            "2015-3",
            "2015-4",
            "2015-5",
            "2015-6",
            "2015-7",
            "2015-8",
            "2015-9",
            "2015-10",
            "2015-11",
            "2015-12",
        ]
    yList=[
            {
            "name":"最高气温",
            "value":[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            },{
            "name":"最低气温",
            "value":[3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7],
            }
    ]
    ee =easy_line.eLine(lableList=xList,valueList=yList,areastyleOpt=True,isSmooth=True).up_down_x_line(baseParams(title= '降水图'),extraXlist=extra_xList).render("multiple_x_axes.html")
    #save_static_image(ee,"out.jpeg")
#upDownLine()

#渐变色的图例测试
def test_gradientLine():
    x_data = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    yList=[
            {
            "name":"注册总量",
            "value":[393, 438, 485, 631, 689, 824, 987, 1000, 1100, 1200]
            }, {
            "name":"注册x量",
            "value":[293, 138, 483, 331, 689, 224, 57, 700, 900, 1300]
            }
    ]
    ee = easy_line.eLine(lableList=x_data,valueList=yList).gradientLine(baseParams(title= '降水图'))
    #save_static_image(ee,"out1.png")
    ee.render("line_color_with_js_func.html")

test_gradientLine()
