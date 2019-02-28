#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 2:02 PM 
# File  : practice_two_packages.py 
# IDE   : PyCharm

# 15-10

import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk
from die import Die

"""
# Part_1
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_values = [str(x) for x in range(1, 7)]
plt.scatter(x_values, frequencies, s=50, edgecolors='none')
plt.title("Matplotlib for Rolling Die 100 times", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)
plt.show()
"""
# Part_2

rw = RandomWalk(1000)
rw.fill_walk()

hist = pygal.XY()
hist.title = "Pygal for Random Walk"
hist.add('Random Walk', [(rw.x_values[i], rw.y_values[i]) for i in range(len(rw.x_values))])
hist.render_to_file("pygal_for_randomwalk.svg")

