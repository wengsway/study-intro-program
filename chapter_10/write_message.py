#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 2:43 PM 
# File  : write_message.py 
# IDE   : PyCharm

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    #file_object.write("I love programming.\n")
    #file_object.write("I love creating new game.\n")
    file_object.write("I also love finding meaning in large dataset.\n")
    file_object.write("I love creating apps that can run in browser.\n")
