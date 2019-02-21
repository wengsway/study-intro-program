#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:50 PM 
# File  : city_try.py 
# IDE   : PyCharm


citis = ['beijing', 'shanghai', 'nanjing', 'hangzhou', 'xiamen', 'guangzhou']
print(citis[0])

citis.append('shenzhen')
print(citis)

citis.insert(0, 'wuhan')
print(citis)

del citis[0]
print(citis)

citis.pop(2)
print(citis)

citis.remove('hangzhou')
print(citis)
print(sorted(citis))

citis.sort(reverse=True)
print(citis)

citis.reverse()
print(citis)
print(len(citis))
