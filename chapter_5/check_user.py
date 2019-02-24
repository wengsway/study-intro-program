#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:00 PM 
# File  : check_user.py
# IDE   : PyCharm

# 5-10

current_users = ['admin', 'weng', 'quan', 'sway', 'office']
new_users = ['admin', 'Weng', 'John', 'Mary', 'Jack']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to input another user name.")
    else:
        print("This user name has not been used.")
