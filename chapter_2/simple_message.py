#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:40 PM 
# File  : simple_message.py 
# IDE   : PyCharm

# name
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
message = "hello," + full_name.title() + "!"
print(message)

"""
# name_case_1
name = "Eric"
message = "Hello " + name + "," + " would you like to learn some Python today?"
print(message)
"""

"""
# name_case_2
name = "weng sway"
print(name.lower())
print(name.upper())
print(name.title())
"""

"""
# name_case_3
name = "jack ma"
first_message = name.title() + " " + "once said,"
last_message = '"I do not like money."'
full_message = first_message + last_message
print(full_message)
"""

"""
# name_case_4
name = " \tweng \n\tsway "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
"""

# 简单的数字运算
print(5+3)
print(10-2)
print(2*4)
print(int(16/2))

# 打印自己喜欢的数字
favorite_number = 8
message = "My favorite number is " + str(favorite_number) + "."
print(message)

# 打印简单的语句
a = "this is first line message"
b = "this is second line message"
print(a)
print(b)
messages = "One of Python's strengths is its diverse community."
print(messages)
