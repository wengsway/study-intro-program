#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 1:41 PM 
# File  : three_d6.py 
# IDE   : PyCharm

# 15-8

import pygal

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling three D6 5000 times."
hist.x_labels = [str(x) for x in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual_three_d6.svg')