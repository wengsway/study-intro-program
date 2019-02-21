#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 1:45 PM 
# File  : pizza.py 
# IDE   : PyCharm


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())

make_pizza(16,'apple')
make_pizza(12,'apple','peppers','water')
