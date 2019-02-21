#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:05 PM 
# File  : favorite_places.py 
# IDE   : PyCharm

favorite_places = {
    'weng': ['home', 'shanghai', 'beijing'],
    'quan': ['shanghai', 'hangzhou', 'shenzhen'],
    'sway': ['xiamen', 'nanjing', 'shenzhen']}
for name, places in favorite_places.items():
    print(name.title() + "'s favorite place are: ")
    for place in places:
        print("\t" + place.title())
