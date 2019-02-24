#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:12 PM 
# File  : cihui.py 
# IDE   : PyCharm

# 9-13

from collections import OrderedDict

cihui = OrderedDict()

cihui['print'] = 'output the message'
cihui['if'] = 'to do conditional test'
cihui['for'] = 'use for loop function'

for key, value in cihui.items():
    print(key + ": " + value + ".")
