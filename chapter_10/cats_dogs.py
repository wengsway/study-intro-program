#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 4:20 PM 
# File  : cats_dogs.py 
# IDE   : PyCharm


def read_cat_dog(filename):
    try:
        with open(filename, 'r') as f_obj:
            contents = f_obj.read()
            print(contents.strip() + "\n")
    except FileNotFoundError:
        # print("The file " + filename + " does not exist !")
        pass


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_cat_dog(filename)
