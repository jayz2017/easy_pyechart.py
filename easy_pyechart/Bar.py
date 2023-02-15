from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
import easy_pyechart.constants as constants
from easy_pyechart import _get_base_example


class Stack_bar_percent:

    def __init__(self,
                 title=None,
                 subTitle=None,
                 lableList=[],
                 valueList=[],
                 legendsOpts=[],
                 themeType=constants.defualt_theme,
                 isShowPercentage=False,
                 ):
        self.legend = _get_base_example(Bar, 
                                        title,
                                        subTitle,
                                        lableList, 
                                        valueList, 
                                        legendsOpts, 
                                        themeType,
                                        isShowPercentage
                                        )

    def _stack_bar_percent(self):
        self.legend.render("multiple_y_axes.html")
    
Stack_bar_percent._stack_bar_percent()