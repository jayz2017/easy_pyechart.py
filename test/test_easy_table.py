import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_table, baseParams,set_water_marking,save_static_image,screen
from pyecharts.render import make_snapshot
from snapshot_phantomjs   import snapshot

# headers = ["City name", "Area", "Population", "Annual Rainfall"]
# rows = [
#     ["Brisbane", 5905, 1857594, 1146.4],
#     ["Adelaide", 1295, 1158259, 600.5],
#     ["Darwin", 112, 120900, 1714.7],
#     ["Hobart", 1357, 205556, 619.5],
#     ["Sydney", 2058, 4336374, 1214.8],
#     ["Melbourne", 1566, 3806092, 646.9],
#     ["Perth", 5386, 1554769, 869.4],
# ]

# c=easy_table.eTable(rowList=rows,headerList=headers).base_table(baseParams(title='sss',subTitle=''))
#c.render("table_base.html")
make_snapshot(engine=snapshot,file_name= "customized_pie.html",output_name="customized_pie.png")








