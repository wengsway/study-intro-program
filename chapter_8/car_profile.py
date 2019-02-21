#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 2:09 PM 
# File  : car_profile.py 
# IDE   : PyCharm


def car_profile(manufacturer, model, **other_info):
    car = {}
    car['manufacturer'] = manufacturer.title()
    car['model'] = model.title()
    for key, value in other_info.items():
        car[key] = value.title()
    return car


car = car_profile('BMW', 'x five', color='black', money='million')
print(car)