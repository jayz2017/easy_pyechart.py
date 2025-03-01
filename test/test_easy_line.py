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

#test_gradientLine()


# from PIL import Image
# # 打开图表图片和额外的图片
# chart_img = Image.open(r"E:\project\easy_pyechartpy\553682_playerNumTable.png")
# extra_img = Image.open(r"C:\Users\chenhao\Desktop\1\开拓者\stand\1631133.png").convert("RGBA")  # 替换为你的图片路径

# # 调整左侧图片的高度（按比例缩放）
# new_height = int(chart_img.height )  # 左侧图片高度设置为图表高度的 1.2 倍
# aspect_ratio = extra_img.width / extra_img.height  # 保持宽高比
# new_width = int(new_height * aspect_ratio)
# extra_img_resized = extra_img.resize((new_width, new_height))

# # 创建一个新的画布
# distance_between_images = -150  # 设置左右图片之间的距离
# canvas_width = extra_img_resized.width + distance_between_images + chart_img.width
# canvas_height = max(chart_img.height, extra_img_resized.height)
# canvas = Image.new("RGB", (canvas_width, canvas_height), color=(255, 255, 255))  # 白色背景

# # 将两张图片粘贴到画布上
# canvas.paste(extra_img_resized, (0, 0))  # 左侧放置额外图片
# canvas.paste(chart_img, (extra_img_resized.width + distance_between_images, 0))  # 右侧放置图表图片

# # 保存最终结果
# canvas.save(r"E:\project\easy_pyechartpy\2223211.png")


# from PIL import Image

# # 加载大图片和小图片
# background_img = Image.open(r"E:\project\easy_pyechartpy\1626179_all_shoot.png")  # 替换为你的大图片路径
# overlay_img = Image.open(r"C:\Users\chenhao\Desktop\1\76人\head\200768.png")    # 替换为你的小图片路径

# # 确保小图片支持透明（转换为RGBA模式）
# overlay_img = overlay_img.convert("RGBA")

# # 获取图片尺寸
# bg_width, bg_height = background_img.size
# ov_width, ov_height = overlay_img.size

# # 计算小图片放置的位置（左下角）
# position = (0, bg_height - ov_height)  # 左下角位置

# # 创建一个新的画布（如果需要保留透明背景，可以设置为RGBA模式）
# if background_img.mode != "RGBA":
#     background_img = background_img.convert("RGBA")

# # 将小图片粘贴到大图片上
# background_img.paste(overlay_img, position, mask=overlay_img)  # 使用mask保持透明效果

# # 保存最终结果
# background_img.save("result_image.png")