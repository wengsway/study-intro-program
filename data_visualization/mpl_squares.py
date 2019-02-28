#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 10:43 AM 
# File  : mpl_squares.py 
# IDE   : PyCharm

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set the Title and  add Label
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# Set sacle size
plt.tick_params(axis='both', labelsize=14)

plt.show()
