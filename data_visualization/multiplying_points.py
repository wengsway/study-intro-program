#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 1:46 PM 
# File  : multiplying_points.py 
# IDE   : PyCharm

# 15-9

import pygal

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(5000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果
possible_result = []
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for x in range(1, die_1.num_sides+1):
    for y in range(1, die_2.num_sides+1):
        possible_result.append(x * y)

possible_result = list(set(possible_result))
possible_result.sort()
for value in possible_result:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 5000 times."
hist.x_labels = [str(x) for x in possible_result]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual_d6d6.svg')
