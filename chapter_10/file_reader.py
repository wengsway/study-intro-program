#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 10:58 AM 
# File  : file_reader.py 
# IDE   : PyCharm

"""
# 读取整个文件，用print函数输出并删去多余的空行
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
"""
"""
# 用for循环逐行打印文件内容，删去多余的空行
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
"""
# 将文件各行内容存储在列表中，在with代码块之外仍可以使用该列表。
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())