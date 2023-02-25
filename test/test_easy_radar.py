import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_radar,baseParams


lable_list = [{
    "name":"销售（sales）",
    "value":6500
},{
    "name":"管理（Administration）",
    "value":16000
},{
    "name":"信息技术（Information Technology）",
    "value":30000
},{
    "name":"客服（Customer Support）",
    "value":38000
},{
    "name":"研发（Development）",
    "value":52000
},{
    "name":"市场（Marketing）",
    "value":25000
}]
value_list=[{
  "name":"预算分配（Allocated Budget）",
  "value":[[4300, 10000, 28000, 35000, 50000, 19000]]

},{
  "name":"实际开销（Actual Spending）",
  "value":[[5000, 14000, 28000, 31000, 42000, 21000]]
}]

#easy_radar.eRadar(lableList=lable_list,valueList=value_list).basic_radar_chart(baseParams=baseParams(title='测试一下')).render("basic_radar_chart.html")
#easy_radar.eRadar(lableList=lable_list,valueList=value_list).radar_selected_mode(baseParams=baseParams(title='测试一下')).render("basic_radar_chart.html")


data = [{"value": [4, -4, 2, 3, 0, 1], "name": "预算分配"}]
c_schema = [
    {"name": "销售", "max": 4, "min": -4},
    {"name": "管理", "max": 4, "min": -4},
    {"name": "技术", "max": 4, "min": -4},
    {"name": "客服", "max": 4, "min": -4},
    {"name": "研发", "max": 4, "min": -4},
    {"name": "市场", "max": 4, "min": -4},
]

easy_radar.eRadar(lableList=c_schema,valueList=data).radar_angle_radius_axis(baseParams=baseParams(title='测试一下')).render("basic_radar_chart.html")







