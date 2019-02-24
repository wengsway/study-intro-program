#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 2:53 PM 
# File  : guest.py 
# IDE   : PyCharm

# 10-4

filename = 'guest.txt'
"""
with open(filename, 'w') as file_object:
    guest_name = input("Please enter your name: ")
    file_object.write(guest_name)
"""
while True:
    print("Please enter your name in this program.")
    print("Enter q at any time to quit.")
    guest_name = input("Enter your name: ")
    if guest_name != 'q':
        print("Hello, " + guest_name + ".")
        with open(filename, 'a') as file_object:
            file_object.write(guest_name.title() + " visits here.\n")
    else:
        break
