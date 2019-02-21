#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:04 PM 
# File  : favorite_numbers.py 
# IDE   : PyCharm

favorite_numbers = {
    'weng': ['1', '2', '6'],
    'quan': ['2', '3', '8'],
    'sway': ['3', '6', '5'],
    'office': ['4', '9', '10'],
    'word': ['5', '10', '15', '20']
}
for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + number)
