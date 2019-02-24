#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 4:34 PM 
# File  : common_words.py 
# IDE   : PyCharm

# 10-10


def common_words(filename):
    """计算一个文件包含多少个指定的单词"""
    try:
        with open(filename) as f_obj:
            counts = 0
            for line in f_obj:
                counts += line.lower().count('the')
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print("The file " + filename + " has about " + str(counts) + " 'the'.")


filename = 'hamlet.txt'
common_words(filename)
