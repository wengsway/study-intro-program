#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 11:30 AM 
# File  : learning_python.py 
# IDE   : PyCharm

# 10-1 and 10-2

filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

"""
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
"""
"""
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
"""
print("-----")
print(contents.replace('Python', 'C'))
print("-----")
print(contents)

