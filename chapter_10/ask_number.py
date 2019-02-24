#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 6:01 PM 
# File  : ask_number.py 
# IDE   : PyCharm

# 10-11 and 10-12

import json

filename = 'ask_number.json'


def load_number():
    try:
        with open(filename) as f_obj:
            content = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return content


def get_number():
    number = input("Please enter a number you like: ")
    with open(filename, 'w') as f_obj:
        json.dump(int(number), f_obj)


number = load_number()
if number:
    print("I know your favorite number! It's " + str(number) + ".")
else:
    get_number()


