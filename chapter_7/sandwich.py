#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:11 PM 
# File  : sandwich.py 
# IDE   : PyCharm

# 7-8

sandwich_orders = ['tuna', 'yama', 'haha']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)
