#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:58 PM 
# File  : pizza.py 
# IDE   : PyCharm

pizzas = ['beef pizza', 'chicken pizza', 'original pizza']
for pizza in pizzas:
    print("I like " + pizza.title())
print("\nI really love pizza")
friend_pizzas = pizzas[:]
pizzas.append("dark pizza")
friend_pizzas.append("white pizza")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
