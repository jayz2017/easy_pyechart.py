from argparse import _get_action_name
from typing import Any, Optional, Union
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import table_base_config,double_head_config

class table():
    def __init__(
                self,
                page_wight=None,
                page_hight=None,
                #指定特定行的颜色
                the_row_color:Optional[dict] = {},
                #指定特定行的字体大小
                the_row_font_size:Optional[dict] = {},
                #指定特定列的字体大小
                the_column_font_size:Optional[dict] = {},
                #指定特定列的字体颜色
                the_column_font_color:Optional[dict] = {},
                #指定特定列自动的渐变颜色
                the_auto_line_color:Optional[list] = [],
                #指定圆圈形状的列
                the_donut_col:Optional[list] = [],
                #指定星星图案形状的列
                the_stars_col:Optional[list] = [],
                #指定进度条图案形状的列
                the_bar_col:Optional[list] = [],
                #指定条柱样式图形的列
                the_bars_col:Optional[list] = [],
                #表格列
                columns :Optional[list] = [],
                #表格数据
                _data:Optional[list] = [],
                head_colors:Optional[dict] = {},
                head_width:Optional[dict] = {},
                #表格行整体宽度压缩比例，默认是3
                line_comp_ratio:Optional[int] = 3,
                #水印文本内容
                water_mark=None
                 ) :
        self.opts: dict = {
                "page_wight":page_wight,
                "page_hight":page_hight,
                "the_row_color":the_row_color,
                "columns":columns,
                "_data":_data,
                "head_colors":head_colors,
                "head_width":head_width,
                "line_comp_ratio":line_comp_ratio,
                "the_row_font_size":the_row_font_size,
                "the_column_font_size":the_column_font_size,
                "the_column_font_color":the_column_font_color,
                "the_auto_line_color":the_auto_line_color,
                "the_donut_col":the_donut_col,
                "the_stars_col":the_stars_col,
                "the_bar_col":the_bar_col,
                "the_bars_col":the_bars_col,
                "water_mark":water_mark
                }
    #基本表格图，没有上面之外的样式设置    
    def base_table(self):
        _c = table_base_config(self,None)
        return _c
        # _c.savefig("alternating_row_color2.png", 
        #     bbox_inches='tight', 
        #     pad_inches=0,dpi=1200)
        
    #表格图，有列样式的分割线式设置    
    def table_col_split(self,lineSplit):
        _c = table_base_config(self,lineSplit)
        return _c
        # _c.savefig("C:\\Users\\haochenhu\\Desktop\\2121321\\table_split_col.png", 
        #     bbox_inches='tight', 
        #     pad_inches=0,dpi=100)
    def double_head_table(self,groupHeader,lineSplit):
        return double_head_config(self,groupHeader,lineSplit)    


def test_base_table():
    #指定行颜色
    the_row_color={13:'#E6DBC7',17:'#583434',18:'#E6DBC7'}
    columns=['关键KPI','2月','1-2月','年累同比','达成率',' ','110均值']
    head_colors={' ':'#FFFFFF'}
    head_width={5:0.1}
    the_column_font_color={17:"#FFFFFF"}
    _data = [  ['关键KPI','2月','1-2月','年累同比','达成率',' ','110均值'],
                ['新车销量','84','164','+23.3%','106.5%','✅','90'],
                ['单车产值（万）','64.0','63.1','+5.1%','131.3%','🐠','59.0'],
                ['二手车销量','40','69','+9.5%','89.6%',' ','30'],
                ['旧新比','47.6%','42.1%','-11.2%','84.1%',' ','32.7%'],
                ['水平事业贡献率','3.4%','3.2%','-20.6%','68.1%','⚠','3.9%'],
                ['可变综合毛利（万）\n2123123123','366.4','720.2','+45.3%','140.7%','🐠','380.7'],
                ['可变综合毛利率','6.4%','6.6%','+13.5%','120.5%','🐠6.8%'],
                ['固定回厂','2,591','4,671','+19.2%','142.5%','🐠2,308'],
                ['固定产值（万）','915.4','1,645.0','+25.8%','93.8%',' ','587.8'],
                ['固定毛利（万）','429.5','765.8','+23.8%','80.5%',' ','248.7'],
                ['单车产值','3,533','3,522','+5.6%','65.8%','⚠','2,547'],
                ['综合毛利率','46.9%','46.6%','-1.6%','85.8%',' ','42.3%'],
                ['服务满足率','110.4%','99.0%','+19.3%','64.2%','⚠','78.3%'],
                ['费用（万）','389.0','773.5','+3.7%','125.3%',' ','317.6'],
                ['费用率','5.9%','6.1%','-18.8%','90.3%',' ','5.1%'],
                ['税前利润（万）','417.1','743.6','+140.3%','87.9%',' ','325.1'],
                ['ROS','6.3%','5.9%','+88.1%','77.7%','⚠','5.2%'],
                ['客户保留能力','-3.0%','-3.0%',' ',' ','⚠','0.2%']
            ]
    _c=table(
        page_hight=900,
        page_wight=700,
          the_row_color=the_row_color,
          columns=columns,
          _data=_data,
          head_colors=head_colors,
          line_comp_ratio=2,
          head_width=head_width,
          the_column_font_color=the_column_font_color
          ).table_col_split(lineSplit=[3,6])
    #.base_table(lineSplit=[3,6])
    _c.savefig(r'F:\ss\1.png', 
                        bbox_inches='tight', 
                        pad_inches=0,dpi=600)

#test_base_table()


def test_double_head():
    _r={
        'imageSaveLink': r'C:\Users\chenhao\Desktop\新建文件夹\dbfa6f4e-eeea-449c-8caf-a3e6d42138ba5.png',
         # 'lineSplit': [2, 5, 6, 9, 10], 
          'data': [
               # [' ', '2月', '1-2月', '2月'],
                ['新车销量', '231', '231', '231'], 
                ['单车产值（万）', '', '', ''], 
                ['GPI%', '22', '22', '22']
            #    ,  ['GPII%[>0%]', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '', '55', '55', '55'],
            #     ['新增订单', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'], 
            #     ['订单残', '231231', '231231', '231231', '231231', '231231', '231231', '231231', '231231', '231231', '231231', '231231', '', '231231', '231231', '231231'], 
            #     ['订单深度[1.5]', '2231', '2231', '2231', '2231', '2231', '2231', '2231', '2231', '2231', '2231', '2231', '', '2231', '2231', '2231'],
            #     ['旧新比', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'],
            #     ['单台贡献度', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'],
            #     ['贡献率', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'], 
            #     ['传统水平[3.5%]', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'],
            #     ['增值水平[1.0%]', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'], 
            #     ['可变综合毛利', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'], 
            #     ['GPIII%', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'],
            #     ['贡献度', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'], 
            #     ['库存度[0.8]', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21'], 
            #     ['GROI[>80%]', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '', '21', '21', '21']
                ], 
                 'theRowColor': {'1': '#E6DBC7', '2': '#E6DBC7', '3': '#E6DBC7'}, 
                  'columns': [' ', '2月@进口', '2月@国产', '2月@整体'
                             # , '2月', '1-2月', '110均值', '2月', '达成率', '1-2月', '年累同比', '达成率', ' ', 'T20均值', '110均值', '全国均值'
                              ],
                   'headWidth': {'1': 0.05, '9': 0.1},
                      'pageHight': 475,
                        'headColors': {' ': '#FFFFFF'}, 
                        'pageWight': 1231,
                          'type': 'double', 
                        'groupHeader': {
                            '0,1': '关键KPI', 
                            #'2,3': '进口车',
                              '2': 'YTD'
                            #   , '6,7': '国产车',
                            #     '8': 'YTD', 
                            #     '10,11,12,13,14,15': '整体//事业计划达成率', 
                            #     '16,17,18': 'YTD'
                                }}
    _image_save_link=_r['imageSaveLink']
    _c=table(
                    the_row_color=_r.get('theRowColor',{}),
                    columns=_r['columns'],
                    _data=_r['data'],
                    head_colors= _r.get('headColors',{}),
                    line_comp_ratio=_r.get('lineCompRatio',3),
                    head_width=_r.get('headWidth',{}),
                    the_column_font_color=_r.get('theColumnFontColor',{}),
                    the_column_font_size=_r.get('theColumnFontSize',{}),
                    the_row_font_size=_r.get('theRowFontSize',{}),
                    page_wight=_r.get('pageWight',None),
                    page_hight=_r.get('pageHight',None),
                  ).double_head_table(groupHeader=_r['groupHeader'],lineSplit=_r.get('lineSplit',None))
                
    _c.savefig(_image_save_link, 
                        bbox_inches='tight', 
                        pad_inches=0,dpi=600)
    

#test_double_head()

def test1():
    _r={
        'imageSaveLink': r'F:\ss\dbfa6f4e-eeea-449c-2-a3138ba2.png',
        'data': [   
                    ['西蒙斯',			'24:31:00',	8,	6,  23.3,  0.45,   23,	'5',	'2',	'3',	'5 ', '5',	'0',	'4',	'4',	'0',	'0',	'0',	'3',	'1',	'0',	'2',	'5'],											
                    ['卡梅隆-约翰逊',	'35:14:00',	14,	2.0, 23,    0.33,   43,	'2',	'0',	'2',	'12', '4',	'8',	'4',	'0',	'4',	'2',	'2',	'4',	'0',	'1',	'0',	'3'],											
                    ['芬尼-史密斯',		'28:06:00',	7,	13,	 33,	0.56,  0.67,	'5',	'1',	'4',	'8	','4',	'4',	'3',	'2',	'1',	'0',	'0',	'4',	'2',	'0',	'3',	'4'],											
                    ['托马斯',			'33:18:00',	19,	0,	 56,	0.31,  0.77,	'2',	'0',	'2',	'12', '6',	'6',	'4',	'3',	'1',	'11',	'10',	'2',	'1',	'0',	'3',	'2'],											
                    ['施罗德',			'33:56:00',	33,	9,	 77,	0.23,  0.87,	'2',	'0',	'2',	'14', '5',	'9',	'11',	'5',	'6',	'5',	'5',	'8',	'1',	'0',	'2',	'1'],											
                    ['威尔逊',			'26:51:00',	12,	25,	 13,	0.12,  0.69,	'7',	'3',	'4',	'7	','4',	'3',	'5',	'4',	'1',	'2',	'1',	'2',	'0',	'0',	'2',	'1'],											
				],
        'theRowColor': {'1': '#E6DBC7', '2': '#E6DBC7', '3': '#E6DBC7'}, 
        'columns': ['名称','时间', '得分', '正负值' ,'2分%','3分%','罚球%','篮板','前场','后场','出手FM','2分FM','3分FM','命中FA','2分FA','3分FA','出手','罚中','助攻','抢断','盖帽','失误','犯规'],
        'headWidth': {'1': 0.5, '9': 0.1},
        #'pageHight': 475,
        #'headColors': {' ': '#FFFFFF'}, 
       # 'pageWight': 1231,
        'type': 'double', 
        'groupHeader': {
            '3,4,5,6': '效率',
            '7,8,9': '篮板',
            '11,12,10':'出手分布',
            '14,15,13':'命中分布',
            '17,16':'罚球'
            },
        'theAutoLineColor':["2分%",'3分%']    
        }
    _image_save_link=_r['imageSaveLink']
    _c=table(
                    the_row_color=_r.get('theRowColor',{}),
                    columns=_r['columns'],
                    _data=_r['data'],
                    head_colors= _r.get('headColors',{}),
                    line_comp_ratio=_r.get('lineCompRatio',3),
                    head_width=_r.get('headWidth',{}),
                    the_column_font_color=_r.get('theColumnFontColor',{}),
                    the_column_font_size=_r.get('theColumnFontSize',{}),
                    the_row_font_size=_r.get('theRowFontSize',{}),
                    page_wight=_r.get('pageWight',2000),
                    page_hight=_r.get('pageHight',900),
                    the_auto_line_color=_r.get('theAutoLineColor',[]),
                    the_bar_col=_r.get('theBarColor',[]),
                    the_bars_col=_r.get('theBarsColor',[]),
                    the_donut_col=_r.get('theDonutColor',[]),
                    the_stars_col=_r.get('theStarsColor',[]),
                    water_mark=_r.get('water_mark',None),
                  ).double_head_table(groupHeader=_r['groupHeader'],lineSplit=_r.get('lineSplit',None))
    
    _c.savefig(_image_save_link, 
                        bbox_inches='tight',
                        pad_inches=0,dpi=600)

#test1()
