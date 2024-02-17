import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_table, baseParams,set_water_marking,save_static_image,screen
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
from snapshot_pyppeteer import snapshot as pyppeteer_snapshot  
from snapshot_selenium import snapshot as selenium_snapshot  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
  


headers = ["City name", "Area", "Population", "Annual Rainfall"]
rows = [
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]
#c=easy_table.eMTable(rowList=rows).base_table()

#c=easy_table.eTable(rowList=rows,headerList=headers).base_table(baseParams(title='sss',subTitle=''))
#c.render("table_base.html")
# 配置Chrome选项  
# chrome_options = Options()  
# chrome_options.add_argument("--headless")  # 以无头模式运行，不显示浏览器窗口  
# chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速  
  
# # 初始化WebDriver  
# driver = webdriver.Chrome(executable_path=r'D:\python3\goolerDriver\chromedriver.exe', options=chrome_options)  
  
# # 打开HTML文件  
# driver.get(r'D:\plg_resource\easy_pyechartpy\table_base.html')  
  
# # 截图并保存为图片  
# driver.save_screenshot('output.png')  
  
# # 关闭WebDriver  
# driver.quit()
# make_snapshot(engine=pyppeteer_snapshot,file_name=c.render(), output_name="customized_pie.png")

#make_snapshot(engine=snapshot, file_name=r"D:\plg_resource\easy_pyechartpy\table_base.html",output_name="customized_pie.png")
#save_static_image(c,"customized_pie.png")
# import matplotlib.pyplot as plt  
# import numpy as np  
  
# # 创建一些数据  
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
  
# # 创建一个新的图形  
# fig, ax = plt.subplots()  
  
# # 初始化cell_text列表  
# cell_text = []  
  
# # 填充表格的头部行  
# cell_text.append(['Row' + str(i) for i in range(1, data.shape[0] + 1)])  
  
# # 填充表格的数据行  
# for i in range(data.shape[0]):  
#     cell_text.append(['{0:.1f}'.format(cell) for cell in data[i, :]])  
  
# # 在图形上绘制表格  
# table = ax.table(cellText=cell_text, colLabels=['A', 'B', 'C'], loc='center')  
  
# # 设置表格的属性  
# table.auto_set_font_size(False)  
# table.set_fontsize(12)  
  
# # 隐藏坐标轴  
# ax.axis('off')  
  
# # 显示图形  
# plt.show()