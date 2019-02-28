#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 12:22 PM 
# File  : rw_visual.py 
# IDE   : PyCharm

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1, edgecolors='none')
    plt.plot(rw.x_values, rw.y_values, linewidth=3)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Mmake another walk ? (y/n): ")
    if keep_running == 'n':
        break
