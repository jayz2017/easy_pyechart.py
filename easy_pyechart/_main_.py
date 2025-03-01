import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_Bar, easy_funnel, easy_gauge,easy_graph,easy_line,easy_liquid, easy_parallel,easy_pie,easy_radar,easy_sankey,easy_scatter,easy_table,easy_treeMap,easy_shoot,set_water_marking, save_static_image,baseParams,table
from flask import Flask, request
import json
app = Flask(__name__)
import pyecharts.options as opts
from PIL import Image
'''主要针对的是使用baseParams作为基本参数获取的图例模型'''
def packBaseParams(params):
    values = {}
    try:
        title = params['title']
    except:
        title =None
    try:
        saveUrl = params['saveUrl']
    except:
        return '请输入保存的图片名称'
    try:
        subTitle = params['subTitle']
    except:
        subTitle = None
    try:
        backgroundImageUrl = params['backgroundImageUrl']
    except:
        backgroundImageUrl = None
    try:
        water_marking = params['waterMarking']
    except:
        water_marking = None
    values['title'] = title
    values['saveUrl'] = saveUrl
    values['subTitle'] = subTitle
    values['backgroundImageUrl'] = backgroundImageUrl
    values['water_marking'] = water_marking
    return values

def packParams(params):
    values = {}
    try:
        title = params['title']
        lableList = params['lableList']
        valueList = params['valueList']
        legendsOpts = params['legendsOpts']
    except:
        '404，请输入对应的参数'
    try:
        saveUrl = params['saveUrl']
    except:
        return '请输入保存的图片名称'
    try:
        subTitle = params['subTitle']
    except:
        subTitle = None
    try:
        backgroundImageUrl = params['backgroundImageUrl']
    except:
        backgroundImageUrl = None
    try:
        water_marking = params['waterMarking']
    except:
        water_marking = None
    values['title'] = title
    values['lableList'] = lableList
    values['valueList'] = valueList
    values['legendsOpts'] = legendsOpts
    values['saveUrl'] = saveUrl
    values['subTitle'] = subTitle
    values['backgroundImageUrl'] = backgroundImageUrl
    values['water_marking'] = water_marking
    return values

'''pyechart 图例统一保存的方法'''
def easyModelLegendToSaveImage(water_marking,easyModelLegend,saveUrl):
        if (water_marking != None):
            easyModelLegend.set_global_opts(
                graphic_opts=set_water_marking(water_marking))
        save_static_image(easyModelLegend, saveUrl)
        
'''
柱状图模型，暂时只有简单的柱状图、以及柱状图和折线图的符合图

'''

@app.post("/easy/Bar/<type>/")
def excute_easy_Bar(type):
    params = json.loads(request.get_data())
    _getValue = packParams(params)
    # if (type(_getValue) == str):
    #     return _getValue
    easyModel = easy_Bar.eBar(title=_getValue['title'], subTitle=_getValue.get('subTitle'), lableList=_getValue['lableList'],
                             valueList=_getValue['valueList'], legendsOpts=_getValue.get('legendsOpts',None), backgroundImageUrl=_getValue.get('backgroundImageUrl',None))

    if (type == 'bar'):
        easyModelLegend = easyModel._stack_bar_percent()
        easyModelLegendToSaveImage(_getValue['water_marking'],easyModelLegend,_getValue['saveUrl']) 
    elif (type == 'lineBar'):

        extraYname = params['extraYname']
        extraYList = params['extraYList']
        extraLegendName = params['extraLegendName']
        easyModelLegend = easyModel._mixed_bar_and_line(
            extraYname=extraYname, extraYList=extraYList, extraLegendName=extraLegendName)
        easyModelLegendToSaveImage(_getValue.get('water_marking',''),easyModelLegend,_getValue['saveUrl'])    
    else:
        return {'error':404}
    return {'sucessful':200}

'''漏斗图'''
@app.post("/easy/Funnel/<type>/")
def excute_easy_Funnel(type):
    _getValue = packParams(json.loads(request.get_data()))
    easyModel = easy_funnel.eFunnel(title=_getValue['title'], subTitle=_getValue['subTitle'], lableList=_getValue['lableList'],
                                    valueList=_getValue['valueList'], backgroundImageUrl=_getValue['backgroundImageUrl'])
    easyModelLegend = easyModel._funnel_chart()
    easyModelLegendToSaveImage(_getValue['water_marking'],easyModelLegend,_getValue['saveUrl'])    
    return {'sucessful':200}

'''仪表盘'''
@app.post("/easy/gauge/<type>/")
def excute_easy_Gauge(type):
    _getValue = packParams(json.loads(request.get_data()))
    easyModel = easy_gauge.eGauge(title = _getValue['title'],
                                  subTitle = _getValue['subTitle'],
                                  seriesName = _getValue['lableList'],
                                  dataList = _getValue['valueList'],
                                  backgroundImageUrl=_getValue['backgroundImageUrl'])
    
    easyModelLegend = easyModel.excute_eGauge()
    easyModelLegendToSaveImage(_getValue['water_marking'],easyModelLegend,_getValue['saveUrl'])    
    return {'sucessful':200}

'''
关系图
'''
@app.post("/easy/Graph/<type>/")
def excute_easy_Graph(type):
    _rDate =json.loads(request.get_data())

    title = _rDate['title']
    nodes = _rDate['nodes']
    links = _rDate['links']
    categories = _rDate['categories']
    try:
        subTitle = _rDate['subTitle']
    except:
        subTitle =None
    try:
        saveUrl = _rDate['saveUrl']
    except:
        return '请输入保存的图片名称'
    try:
        water_marking = _rDate['waterMarking']
    except:
        water_marking = None
    #圆弧型的关系图    
    easyModelLegend = easy_graph.eGraph(nodes,links,categories).excute_eGraph(title,subTitle)
    easyModelLegendToSaveImage(water_marking,easyModelLegend,saveUrl)  
    return {'sucessful':200}

'''折线图'''
@app.post("/easy/Line/<type>/")
def excute_easy_Line(type):
    _rDate =json.loads(request.get_data())
    lableList = _rDate['lableList']
    valueList = _rDate['valueList']
    if(type =='basicLine'):
        for i in range(len(valueList)):
            if(i==0):
                valueList[i]['setMarkPoint']=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                    ]
                valueList[i]['setMarkLine']=[opts.MarkLineItem(type_="average", name="平均值")]
            else:
                valueList[i]['setMarkPoint']=[opts.MarkPointItem(value=min(valueList[i]['value']), name="周最低", x=1, y=-1.5)]   
                valueList[i]['setMarkLine']=[
                    opts.MarkLineItem(type_="average", name="平均值"),
                    opts.MarkLineItem(symbol="none", x="90%", y="max"),
                    opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
                ]
    try:
        subTitle = _rDate['subTitle']
    except:
        subTitle =None
    try:
        saveUrl = _rDate['saveUrl']
    except:
        return '请输入保存的图片名称'
    try:
        water_marking = _rDate['waterMarking']
    except:
        water_marking = None
    try:
        backgroundImageUrl = _rDate['backgroundImageUrl']
    except:
        backgroundImageUrl = None        
    easyModel = easy_line.eLine(lableList=lableList,valueList=valueList)
    _baseParams =baseParams(title= _rDate['title'],subTitle = subTitle, backgroundImageUrl = backgroundImageUrl )
    #基本折线图
    if(type =='basicLine'):
        easyModelLegend = easyModel.basicLine(_baseParams)
    #基本折线图
    elif(type =='doubleLine'):
        easyModelLegend = easyModel.doubleLine(_baseParams)
    # 上下两个x轴的数据图    
    elif(type =='upDownXLine'):
        try:
            extraXlist=   _rDate['extraXlist']
        except:
            return 'erro,缺少一个x轴lable数据'    
        easyModelLegend = easyModel.up_down_x_line(_baseParams,extraXlist)
    #渐变色的折线图，阴影部分呈现渐变的色彩效果
    elif(type =='gradientLine'):
        easyModelLegend = easyModel.gradientLine(_baseParams)
    else:
        return 'erro,找不到对应的图例模型'    
    easyModelLegendToSaveImage(water_marking,easyModelLegend,saveUrl) 
    try:
        if 'playerId' in _rDate and _rDate['playerId'] is not None:
            saveLeftPiJie(saveUrl,_rDate['playerId'],_rDate['teamName'])
    except:
        1 
    return {'sucessful':200}

#水球图
@app.post("/easy/Liquid/<type>/")
def excute_easy_Liquid(type):
    _rDate =json.loads(request.get_data())
    try:
       valueList =  _rDate['valueList']
    except:
        return '请输入图例数据'
    _rParams = packBaseParams(_rDate)
    easyModel = easy_liquid.eLiquid(valueList)
    if(type =='baseLiquid'):
        easyModelLegend = easyModel.baseLiquid(baseParams(title=_rParams['title'] ,
                                        subTitle= _rParams['subTitle'],
                                         backgroundImageUrl= _rParams[' backgroundImageUrl']
                                        ))
    elif(type =='precisionLiquid'):
        easyModelLegend = easyModel.precisionLiquid(baseParams(title=_rParams['title'] ,
                                        subTitle= _rParams['subTitle'],
                                         backgroundImageUrl= _rParams[' backgroundImageUrl']
                                        ))
    else:
        return 'erro,找不到对应的图例模型'    
    easyModelLegendToSaveImage(_rParams['water_marking'],easyModelLegend,_rParams['saveUrl']) 
    return {'sucessful':200}

''''
并行坐标系的图例，能够展示各个数据相对于两外一组数据时的有关量
'''
@app.post("/easy/Parallel/<type>/")
def excute_easy_Parallel(type):
    _rDate =json.loads(request.get_data())
    try:
        lableList = _rDate['lableList']
        ydata = _rDate['ydata']
        valueList = _rDate['valueList']
    except:
        return 'erro,输入的参数不够'  
    easyModel = easy_parallel.eParallel(lableList=lableList,ydata=ydata,valueList=valueList)
    _rParams = packBaseParams(_rDate)
    easyModelLegend = easyModel.base_parallel(baseParams(title=_rParams['title'] ,
                                        subTitle= _rParams['subTitle'],
                                         backgroundImageUrl= _rParams[' backgroundImageUrl']
                                        ))
    easyModelLegendToSaveImage(_rParams['water_marking'],easyModelLegend,_rParams['saveUrl']) 
    return {'sucessful':200}

'''饼状图'''
@app.post("/easy/pie/<type>/")
def excute_easy_pie(type):
    _rDate =json.loads(request.get_data())
    _rParams = packBaseParams(_rDate)

    if(type =='simple'):
            #只有一个图例
        if(len(_rDate['sourceList'][0]) ==2):
            _layOutCenter =[["50%", "50%"]]
            radius =150
        #有两个图例    
        elif(len(_rDate['sourceList'][0]) ==3):
            _layOutCenter =[
                ["25%", "50%"],
                ["75%", "50%"],
                ]
            radius =150
        #有三个图例    
        elif(len(_rDate['sourceList'][0]) ==4):
            _layOutCenter =[
            ["15%", "50%"],
            ["45%", "50%"],
            ["75%", "50%"],
                ]
            radius =100
        #有4个图例    
        elif(len(_rDate['sourceList'][0]) ==5):
            _layOutCenter =[
            ["25%", "30%"],
                ["75%", "30%"],
                ["25%", "75%"],
                ["75%", "75%"],
                ]
            radius =60
        else:
            return '暂时不能融合这么多图例'           
        easyModel = easy_pie.epie(title=_rParams['title'],
                    subTitle= _rParams['subTitle'],
                    backgroundImageUrl= _rParams[' backgroundImageUrl'],
                    sourceList = _rDate['sourceList'],
                    layOutCenter =_layOutCenter,
                    radius =radius
                    )
        easyModelLegend = easyModel.dataset_pie()
    #玫瑰花瓣的样式
    else:
        x_data =_rDate['x_data']
        y_data =_rDate['y_data']
        _dataList=[]
        _len =len(y_data)
        centerLayOutList =[]
        _radius =None
        if(_len==1):
            centerLayOutList.append(["50%", "50%"])
            _radius = ["40%", "55%"]
        elif(_len==2):
            centerLayOutList.append(["30%", "50%"])
            centerLayOutList.append(["70%", "50%"])
            _radius = ["30%", "50%"]
        elif(_len==3):
            centerLayOutList.append(["18%", "60%"])
            centerLayOutList.append(["47%", "60%"])
            centerLayOutList.append(["75%", "60%"])
            _radius = ["20%", "35%"]
        elif(_len==4):
            centerLayOutList.append(["30%", "30%"])
            centerLayOutList.append(["70%", "70%"])
            centerLayOutList.append(["30%", "70%"])
            centerLayOutList.append(["70%", "30%"])
            _radius = ["20%", "35%"]        
        else:
            return '暂时不能融合这么多图例' 

        for i in range(_len):
            _dataMap={}
            data_pair = [list(z) for z in zip(x_data, y_data[i])]
            data_pair.sort(key=lambda x: x[1])
            _dataMap['name'] =i
            _dataMap['value'] = data_pair
            _dataMap['isRichLabel'] = False
            _dataMap['radius'] = ["40%", "55%"]
            _dataMap['type'] ='radius'
            _dataMap['centerLayOut'] =centerLayOutList[i]
            _dataList.append(_dataMap)
        easyModelLegend = easy_pie.epie(title=_rParams['title']).double_pie(dataList=_dataList)
    easyModelLegendToSaveImage(_rParams['water_marking'],easyModelLegend,_rParams['saveUrl']) 
    return {'sucessful':200}

'''雷达图'''
@app.post("/easy/radar/<type>/")
def excute_easy_radar(type):
    _rDate =json.loads(request.get_data())
    _rParams = packBaseParams(_rDate)
    easyModel  = easy_radar.eRadar(_rDate['lableList'],_rDate['valueList'])
    if(type =='Base'):
        easyModelLegend = easyModel.basic_radar_chart(baseParams(title=_rParams.get('title','') ,
                                        subTitle= _rParams.get('subTitle',''),
                                         backgroundImageUrl= _rParams.get('backgroundImageUrl',None)
                                        ))
    elif(type =='Single'):
        easyModelLegend = easyModel.radar_selected_mode(baseParams(title=_rParams.get('title','') ,
                                        subTitle= _rParams.get('subTitle',''),
                                         backgroundImageUrl= _rParams.get('backgroundImageUrl',None)
                                        ))
    elif(type =='Air'):
        easyModelLegend = easyModel.radar_air_quality(baseParams(title=_rParams.get('title','') ,
                                        subTitle= _rParams.get('subTitle',''),
                                         backgroundImageUrl= _rParams.get('backgroundImageUrl',None)
                                        ))
    elif(type =='angle'):
        easyModelLegend = easyModel.radar_angle_radius_axis(baseParams(title=_rParams.get('title','') ,
                                        subTitle= _rParams.get('subTitle',''),
                                         backgroundImageUrl= _rParams.get('backgroundImageUrl',None)
                                        ),max=_rDate.get('max',100),min=_rDate.get('min',-100))
    easyModelLegendToSaveImage(_rParams.get('water_marking',None),easyModelLegend,_rParams['saveUrl']) 
    return {'sucessful':200}

'''桑基图'''
@app.post("/easy/sankey/<type>/")
def excute_easy_sankey(type):
    _rDate =json.loads(request.get_data())
    _rParams = packBaseParams(_rDate)
    easyModel = easy_sankey.eSankey(_rDate['seriesName'],_rDate['lableList'],_rDate['valueList'])
    if(type == 'Base'):
        easyModelLegend = easyModel.sankey_base(baseParams(title=_rParams['title'] ,
                                        subTitle= _rParams['subTitle'],
                                         backgroundImageUrl= _rParams[' backgroundImageUrl']
                                        ))
    easyModelLegendToSaveImage(_rParams['water_marking'],easyModelLegend,_rParams['saveUrl']) 
    return {'sucessful':200}

'''散点图'''
@app.post("/easy/scatter/<type>/")
def excute_easy_scatter(type):
    _rDate =json.loads(request.get_data())
    _rParams = packBaseParams(_rDate)
    easyModelLegend = easy_scatter.eScatter(title=_rParams['title'],
                          subTitle = _rParams['subTitle'],
                          lableList = _rDate['lableList'],
                          valueList = _rDate['valueList'],
                          backgroundImageUrl = _rParams['backgroundImageUrl']
                          )._effectscatter()
    easyModelLegendToSaveImage(_rParams['water_marking'],easyModelLegend,_rParams['saveUrl']) 
    return {'sucessful':200}

'''表格图'''
@app.post("/easy/table/<type>/")
def excute_easy_table(type):
    _rDate =json.loads(request.get_data())
    easy_table.eMTable(_rDate['rowList'],_rDate['columnColor'],_rDate['outSaveUrl'])
    return {'sucessful':200}

'''投射图'''
@app.post("/easy/shoot/image/<type>/")
def excute_easy_shootImage(type):
    #print(request.get_data())
    _rDate =json.loads(request.get_data())
    imageName = _rDate['imageName']
    if(type =='scatter'):
        inShoot = _rDate['inShoot']
        noShoot = _rDate['noShoot']
        easy_shoot._excutePlayerShootWriteImage(inShoot,noShoot,imageName)
    elif(type =='hot'):
        _shoot_list_ = _rDate['_shoot_list_']
        easy_shoot.heatPowerImageWrite(_shoot_list_,imageName)
    try:
        if 'playerId' in _rDate and _rDate['playerId'] is not None:
            saveButtonPiJie(imageName,_rDate['playerId'],_rDate['teamName'])
    except:
        1        
    return {'sucessful':200}

@app.post("/easycharts/gen/table/")
def genTable():
    _r=json.loads(request.get_data()) 
    _image_save_link=_r['imageSaveLink']     
    _type = _r['type']
    if(_type == 'base'):
        _c=table.table(
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
                    water_mark=_r.get('water_mark',None),
                    _image_save_link=_image_save_link
                  ).base_table()
        
        # _c.savefig(_image_save_link, 
        #     bbox_inches='tight', 
        #     pad_inches=0,dpi=800)
        return _image_save_link
    
    elif(_type=='lineSplit'):
                _c=table.table(
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
                    water_mark=_r.get('water_mark',None),
                    _image_save_link=_image_save_link
                  ).table_col_split(lineSplit=_r.get('lineSplit',None))
                # _c.savefig(_image_save_link, 
                #         bbox_inches='tight', 
                #         pad_inches=0,dpi=800)
                return _image_save_link
    elif (_type=='double'):
                _c=table.table(
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
                    _image_save_link=_image_save_link
                  ).double_head_table(groupHeader=_r['groupHeader'],lineSplit=_r.get('lineSplit',None))
                
                # _c.savefig(_image_save_link, 
                #         bbox_inches='tight', 
                #         pad_inches=0,dpi=600)
                return _image_save_link

    else:
        return 'The legend type is incorrect, please check!'     

def saveLeftPiJie(mainImageUrl,extraImageId,teamName):
    extraImageUrl = "C:/haochenkeji/NBA/staticHead/"+teamName+"/stand/"+extraImageId+".png"
    # 打开图表图片和额外的图片
    chart_img = Image.open(mainImageUrl)
    extra_img = Image.open(extraImageUrl)  # 替换为你的图片路径

    # 调整左侧图片的高度（按比例缩放）
    new_height = int(chart_img.height )  # 左侧图片高度设置为图表高度的 1.2 倍
    aspect_ratio = extra_img.width / extra_img.height  # 保持宽高比
    new_width = int(new_height * aspect_ratio)
    extra_img_resized = extra_img.resize((new_width, new_height))

    # 创建一个新的画布
    distance_between_images = -150  # 设置左右图片之间的距离
    canvas_width = extra_img_resized.width + distance_between_images + chart_img.width
    canvas_height = max(chart_img.height, extra_img_resized.height)
    canvas = Image.new("RGB", (canvas_width, canvas_height), color=(255, 255, 255))  # 白色背景

    # 将两张图片粘贴到画布上
    canvas.paste(extra_img_resized, (0, 0))  # 左侧放置额外图片
    canvas.paste(chart_img, (extra_img_resized.width + distance_between_images, 0))  # 右侧放置图表图片

    # 保存最终结果
    canvas.save(mainImageUrl)

def saveButtonPiJie(mainImageUrl,extraImageId,teamName):
    extraImageUrl = "C:/haochenkeji/NBA/staticHead/"+teamName+"/head/"+extraImageId+".png"
    # 加载大图片和小图片
    background_img = Image.open(mainImageUrl)  # 替换为你的大图片路径
    overlay_img = Image.open(extraImageUrl)    # 替换为你的小图片路径
    # 确保小图片支持透明（转换为RGBA模式）
    overlay_img = overlay_img.convert("RGBA")
    # 获取图片尺寸
    bg_width, bg_height = background_img.size
    ov_width, ov_height = overlay_img.size

    # 压缩小图片的宽高（例如：缩小到原来的50%）
    new_ov_width = int(ov_width * 0.7)  # 新宽度
    new_ov_height = int(ov_height * 0.7)  # 新高度
    overlay_img_resized = overlay_img.resize((new_ov_width, new_ov_height))

    # 计算小图片放置的位置（左下角）
    position = (0, bg_height - new_ov_height)  # 左下角位置

    # 创建一个新的画布（如果需要保留透明背景，可以设置为RGBA模式）
    if background_img.mode != "RGBA":
        background_img = background_img.convert("RGBA")

    # 将调整大小后的小图片粘贴到大图片上
    background_img.paste(overlay_img_resized, position, mask=overlay_img_resized)  # 使用mask保持透明效果
        # 保存最终结果
    background_img.save(mainImageUrl)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8889, debug=True)
