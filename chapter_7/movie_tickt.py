#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:07 PM 
# File  : movie_tickt.py 
# IDE   : PyCharm

# 7-5

while True:
    age=input('Please input your age:')
    age=int(age)
    if age < 3:
        print("The cost is 0.")
    elif age <= 12:
        print("The cost is 10 dollar.")
    else:
        print("The cost is 15 dollar.")
    break
