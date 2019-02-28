#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 11:01 AM 
# File  : scatter_squares.py 
# IDE   : PyCharm

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=30, c=y_values, cmap=plt.cm.Blues, edgecolor='none')

# Set title and add label
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set label range
plt.axis([0, 1100, 0, 1100000])

#  Set scale size
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
