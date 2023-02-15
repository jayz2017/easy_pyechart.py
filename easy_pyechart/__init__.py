from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

def _get_base_example(chart,title,subtitle,lableList,valueList,legendsOpts,themeType,isShowPercentage):
    if lableList==None or type(lableList)!=list or len(lableList) <1:
        return None
    if valueList==None or type(valueList)!=list or len(valueList) <1:
        return None
    if legendsOpts==None or type(legendsOpts)!=list or len(legendsOpts) <1:
        return None
    c = (
        chart(init_opts=opts.InitOpts(theme=themeType))
        .add_xaxis(lableList)
    )
    for i in range(len(valueList)):
        c.add_yaxis(legendsOpts[i], valueList[i], stack="stack1", category_gap="50%")
    if isShowPercentage!=None and isShowPercentage== True:
        c.set_series_opts(
                label_opts=opts.LabelOpts(
                position="right",
                formatter=JsCode(
                    "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
                ),
            )
        )
    xaxis_opts = None
    if max(lableList)>=5:
        xaxis_opts= opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
        
    c.set_global_opts(
                xaxis_opts,
                title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
                tooltip_opts=opts.TooltipOpts(is_show=True, trigger="axis", axis_pointer_type="shadow"),
        )
    return c    
