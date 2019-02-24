#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 3:13 PM 
# File  : survey.py 
# IDE   : PyCharm

# 10-5

filename = 'survey.txt'

while True:
    print("Please enter the reason why you love programming ?")
    print("Enter q at any time to quit.")
    answer = input("Why you love programming: ")
    if answer != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(answer + "\n")
    else:
        break