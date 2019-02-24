#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:06 PM 
# File  : rivers.py 
# IDE   : PyCharm

# 6-5

rivers = {
    'nile': 'egypt',
    'yangte': 'china',
    'Amazon': 'brazil'
}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
