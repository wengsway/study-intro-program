#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 4:51 PM 
# File  : remember_me.py 
# IDE   : PyCharm

# 10-13

import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name ? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    print("Is this username " + username + " right ?")
    key = input("Please enter y/n: ")
    if key == 'y':
        print("Welcome back, " + username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username.title() + ".")


greet_user()
