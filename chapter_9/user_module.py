#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 8:46 PM 
# File  : user_module.py 
# IDE   : PyCharm


class User:
    """描述用户的信息"""

    def __init__(self, first_name, last_name, login_attenpts, location):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attenpts
        self.location = location

    def describe_user(self):
        print("The user's full name is " + self.first_name.title() + " " + self.last_name.title() +
              " and he/she is in " + self.location.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
