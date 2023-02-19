from pyecharts.faker import Faker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_pie

def base_pie():
    source = [
        ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
        ["Matcha Latte", 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
        ["Milk Tea", 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
        ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
        ["Walnut Brownie", 55.2, 67.1, 69.2, 72.4, 53.9, 39.1],
    ]
    layOutCenter = [
        ["25%", "30%"],
        ["75%", "30%"],
        ["25%", "75%"],
        ["75%", "75%"],
    ]
    easy_pie.epie(title='测试一把', sourceList=source,
                  layOutCenter=layOutCenter).dataset_pie().render("dataset_pie.html")


def double_pie():
        x_data = ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
        y_data = [335, 310, 274, 235, 400]
        data_pair = [list(z) for z in zip(x_data, y_data)]
        data_pair.sort(key=lambda x: x[1])
        #data_pair  = [list(z) for z in zip(Faker.choose(), Faker.values())]
        _dataList = [
                {
                "name": '1',
                "value": data_pair,
                "isRichLabel":False,
                # 饼图的半径，数组的第一项是内半径，第二项是外半径
                # 默认设置成百分比，相对于容器高宽中较小的一项的一半
                "radius":"55%",
                # 是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。
                # radius：扇区圆心角展现数据的百分比，半径展现数据的大小
                # area：所有扇区圆心角相同，仅通过半径展现数据大小
                "type":'radius',
                # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
                # 默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
                "centerLayOut":["50%", "50%"],
                }
                ]
        easy_pie.epie(title='cesss').double_pie(dataList=_dataList).render("customized_pie.html")
double_pie()