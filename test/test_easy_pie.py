import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_pyechart import easy_pie


source=[
            ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
            ["Matcha Latte", 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
            ["Milk Tea", 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
            ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
            ["Walnut Brownie", 55.2, 67.1, 69.2, 72.4, 53.9, 39.1],
        ]
layOutCenter=[
        ["25%", "30%"],
        ["75%", "30%"],
        ["25%", "75%"],
        ["75%", "75%"],
]        
easy_pie.epie(title='测试一把',sourceList=source,layOutCenter=layOutCenter).dataset_pie().render("dataset_pie.html")