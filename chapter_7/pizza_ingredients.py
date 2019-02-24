#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:09 PM 
# File  : pizza_ingredients.py 
# IDE   : PyCharm

# 7-4 and 7-6

promt = "\nPlease input a series of ingredients one by one,"
promt += "\nClick 'Enter' when you input one ingredient, "
promt += "Input 'quit' to quit input:"
message = ""
while message != 'quit':
    message = input(promt)
    if message == 'quit':
        break
    print("We will add " + message + " in pizza.")
