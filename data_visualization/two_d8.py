#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 1:39 PM 
# File  : two_d8.py 
# IDE   : PyCharm

# 15-7

import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D8 1000 times."
hist.x_labels = [str(x) for x in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual_two_d8.svg')
