#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:53 PM 
# File  : motocycles.py 
# IDE   : PyCharm


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('yamaha')
print(motorcycles)
