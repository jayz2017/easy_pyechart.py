from matplotlib import pyplot as plt 
from matplotlib.patches import Arc, Circle, Rectangle
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import os
#投篮球场散点图存储基本地址
baseGenImageUrl ='C:\\testimage\\{name}'

def draw_ball_field(color="#20458C", lw=2):
     """ 绘制篮球场 """ 
     # 新建一个大小为(6,6)的绘图窗口 
     fig=plt.figure(figsize=(6, 6))
     # 获得当前的Axes对象ax,进行绘图 
     ax = plt.gca() 
     # 对篮球场进行底色填充
     lines_outer_rec = Rectangle(xy=(-250, -47.5), width=500, height=470, linewidth=lw, color="#F0F0F0", fill=True) 
     # 设置篮球场填充图层为最底层 
     lines_outer_rec.set_zorder(0) 
     #将rec添加进ax 
     ax.add_patch(lines_outer_rec)
      # 绘制篮筐,半径为7.5 
     circle_ball = Circle(xy=(0, 0), radius=7.5, linewidth=lw, color=color, fill=False) 
    # 将circle添加进ax 
     ax.add_patch(circle_ball) 
    # 绘制篮板,尺寸为(60,1) 
     plate = Rectangle(xy=(-30, -7.5), width=60, height=-1, linewidth=lw, color=color, fill=False) 
    # 将rec添加进ax 
     ax.add_patch(plate) 
    # 绘制2分区的外框线,尺寸为(160,190) 
     outer_rec = Rectangle(xy=(-80, -47.5), width=160, height=190, linewidth=lw, color=color, fill=False) 
    # 将rec添加进ax 
     ax.add_patch(outer_rec) 
    # 绘制2分区的内框线,尺寸为(120,190) 
     inner_rec = Rectangle(xy=(-60, -47.5), width=120, height=190, linewidth=lw, color=color, fill=False) 
    # 将rec添加进ax 
     ax.add_patch(inner_rec) 
    # 绘制罚球区域圆圈,半径为60 
     circle_punish = Circle(xy=(0, 142.5), radius=60, linewidth=lw, color=color, fill=False)
     # 将circle添加进ax 
     ax.add_patch(circle_punish) 
    # 绘制三分线的左边线 
     three_left_rec = Rectangle(xy=(-220, -47.5), width=0, height=140, linewidth=lw, color=color, fill=False) 
    # 将rec添加进ax 
     ax.add_patch(three_left_rec) 
    # 绘制三分线的右边线 
     three_right_rec = Rectangle(xy=(220, -47.5), width=0, height=140, linewidth=lw, color=color, fill=False) 
    # 将rec添加进ax 
     ax.add_patch(three_right_rec) 
    # 绘制三分线的圆弧,圆心为(0,0),半径为238.66,起始角度为22.8,结束角度为157.2 
     three_arc = Arc(xy=(0, 0), width=477.32, height=477.32, theta1=22.8, theta2=157.2, linewidth=lw, color=color, fill=False) 
    # 将arc添加进ax 
     ax.add_patch(three_arc) 
    # 绘制中场处的外半圆,半径为60 
     center_outer_arc = Arc(xy=(0, 422.5), width=120, height=120, theta1=180, theta2=0, linewidth=lw, color=color, fill=False) 
    # 将arc添加进ax 
     ax.add_patch(center_outer_arc) 
    # 绘制中场处的内半圆,半径为20 
     center_inner_arc = Arc(xy=(0, 422.5), width=40, height=40, theta1=180, theta2=0, linewidth=lw, color=color, fill=False) 
    # 将arc添加进ax 
     ax.add_patch(center_inner_arc) 
    # 绘制篮球场外框线,尺寸为(500,470) 
     lines_outer_rec = Rectangle(xy=(-250, -47.5), width=500, height=470, linewidth=lw, color=color, fill=False) 
    # 将rec添加进ax 
     ax.add_patch(lines_outer_rec) 
     return ax

def _excutePlayerShootWriteImage(inShoot,noShoot,imageName):
    axs= draw_ball_field(color="#20458C", lw=2)
    # 设置坐标轴范围
    axs.set_xlim(-250, 250)
    axs.set_ylim(422.5, -47.5)
    # 消除坐标轴刻度
    axs.set_xticks([])
    axs.set_yticks([])
    # 绘制散点图
    for i in range(len(inShoot)):
        _in_=inShoot[i]
        _out_=noShoot[i]
        axs.scatter(x=_out_["adj_x"], y=_out_["adj_y"], s=30, marker="x", color="#A82B2B")
        axs.scatter(x=_in_["adj_x"], y=_in_["adj_y"], s=30, marker="o", edgecolors="#3A7711", color="#F0F0F0", linewidths=2)
    # 添加备注信息
    plt.annotate("By haochen", xy=(100, 160), xytext=(178, 418))
    plt.savefig(baseGenImageUrl.format(name=imageName)) 
    #plt.show()

def colormap(): 
    """ 颜色转换 """ 
    return mpl.colors.LinearSegmentedColormap.from_list("cmap", ["#C5C5C5", "#9F9F9F", "#706A7C", "#675678", "#713A71","#9D3E5E", "#BC5245", "#C86138", "#C96239", "#D37636", "#D67F39", "#DA8C3E", "#E1A352"], 256)

# shoot 的数据为width和height组成的集合字典数据 
### shoot["width"] 为所有的x轴数据集合
### shoot["height"] 为所有的y轴数据集合

def heatPowerImageWrite(_shoot_list_,imageName):
# 读取数据 df =  = pd.read_csv("C:\\Users\\haochenhu\\Documents\\curry.csv", header=None, names=["width", "height", "type"])
    shoot = pd.DataFrame(_shoot_list_,columns=["width", "height"])
    # 绘制球员投篮热力图
    shot_heatmap = sns.jointplot (x= shoot["width"], y =shoot["height"],stat_func=None, kind="kde", space=0, color="w", cmap=colormap())
    # 设置图像大小
    shot_heatmap.fig.set_size_inches(6, 6)
    # 图像反向
    ax = shot_heatmap.ax_joint
    # 绘制投篮散点图
    ax.scatter(x=shoot["width"], y=shoot["height"], s=0.1, marker="o", color="w", alpha=1)
    # 添加篮球场
    draw_ball_field(color="w", lw=2)
    # 将坐标轴颜色更改为白色
    lines = plt.gca()
    lines.spines["top"].set_color("none")
    lines.spines["left"].set_color("none")
    # 去除坐标轴标签
    ax.axis("off")
    plt.savefig(baseGenImageUrl.format(name=imageName)) 