#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:11 PM 
# File  : pastrami.py 
# IDE   : PyCharm

# 7-9

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'yama', 'pastrami', 'haha']
finished_sandwiches = []
print("The pastrami has been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)
