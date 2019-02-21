#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:07 PM 
# File  : multiple_ten.py 
# IDE   : PyCharm

number = input("Please input a positive number: ")
number = int(number)
if number % 10 == 0:
    print("The number " + str(number) + " is multiple of ten.")
else:
    print("The number " + str(number) + " is not multiple of ten.")
