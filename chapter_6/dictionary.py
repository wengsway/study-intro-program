#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:03 PM 
# File  : dictionary.py 
# IDE   : PyCharm

# 6-3 and 6-4

ci_hui = {
    'print': 'output the message',
    'if': 'to do conditional test',
    'for': 'use for loop function'
}
for key, value in ci_hui.items():
    print(key + ": " + value + ".")
