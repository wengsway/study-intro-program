#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 4:45 PM 
# File  : number_writer.py 
# IDE   : PyCharm

import json

numbers = [2, 3, 4, 5, 6, 7, 8]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
