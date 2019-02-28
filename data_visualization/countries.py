#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 4:57 PM 
# File  : countries.py 
# IDE   : PyCharm

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
