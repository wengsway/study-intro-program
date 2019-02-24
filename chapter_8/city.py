#!/usr/bin/env python  
# -*- coding:utf-8 _*-
# Author: Wengs
# Time  : 2/20/2019 10:53 AM 
# File  : city.py
# IDE   : PyCharm

# 8-5


def describe_city(city, country='China'):
    print(city.title() + " is in " + country.title() + ".")


describe_city('shanghai')
describe_city('wuhan')
describe_city('london', 'england')
