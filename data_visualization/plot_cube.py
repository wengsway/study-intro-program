#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 11:54 AM 
# File  : plot_cube.py 
# IDE   : PyCharm

# 15-1 and 15-2

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cube of Values", fontsize=14)

plt.show()
