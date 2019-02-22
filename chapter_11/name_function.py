#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 6:45 PM 
# File  : name_function.py 
# IDE   : PyCharm


def get_formatted_name(first, last, middle=''):
    """Generate a neatly-formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
