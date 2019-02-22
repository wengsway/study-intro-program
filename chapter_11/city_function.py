#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 7:51 PM 
# File  : city_function.py 
# IDE   : PyCharm


def city_function(city, country, population=''):
    if population:
        string = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        string = city.title() + ', ' + country.title()
    return string
