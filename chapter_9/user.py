#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 3:23 PM 
# File  : user.py 
# IDE   : PyCharm

# 9-3 and 9-5


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


user_1 = User('weng', 'quan', 0, 'wuhan')
user_2 = User('abc', 'efg', 0, 'shanghai')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()

user_2.increment_login_attempts()
print(user_2.login_attempts)
user_2.increment_login_attempts()
print(user_2.login_attempts)
user_2.increment_login_attempts()
print(user_2.login_attempts)
user_2.reset_login_attempts()
print(user_2.login_attempts)
