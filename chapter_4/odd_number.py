#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:58 PM 
# File  : odd_number.py 
# IDE   : PyCharm

odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)
print("The first three items in the list are:")
print(odd_numbers[:3])
print("Three items from the middle of the list are:")
print(odd_numbers[4:7])
print("The last three items in the list are:")
print(odd_numbers[-3:])
