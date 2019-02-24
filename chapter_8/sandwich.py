#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 2:04 PM 
# File  : sandwich.py
# IDE   : PyCharm

# 8-12


def make_sandwich(*toppings):
    print("\nMaking a sandwich with following toppings:")
    for topping in toppings:
        print("- " + topping.title())


make_sandwich('apple', 'pear', 'beef')
make_sandwich('apple', 'water', 'pear', 'beef')
make_sandwich('pear', 'beef')
