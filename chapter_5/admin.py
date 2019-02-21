#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:00 PM 
# File  : admin.py 
# IDE   : PyCharm

user_names = ['admin', 'weng', 'quan', 'sway', 'office']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello " + user_name + ", would you like to see a status report?")
        else:
            print("Hello " + user_name + ", thank you for logging in again.")
else:
    print("We need to find some users!")
