#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:01 PM 
# File  : conditional_test.py 
# IDE   : PyCharm

# 5-1 and 5-2

name_1 = 'weng quan'
name_2 = 'Weng sway'
print(name_1 == name_2)
if name_2.lower() == name_1:
    print(True)
else:
    print(False)
a = 20
b = 30
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
if (a > 10) and (b > 10):
    print(True)
if (a > 10) or (b > 40):
    print(True)
numbers = [1, 2, 3, 4, 5, 6]
if 2 in numbers:
    print(True)
else:
    print(False)
