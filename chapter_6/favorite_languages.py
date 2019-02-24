#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:04 PM 
# File  : favorite_languages.py 
# IDE   : PyCharm

# 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
should_poll = ['jen', 'weng', 'phil', 'sway']
for name in should_poll:
    if name in favorite_languages.keys():
        print(name.title() + ", Thank you very much.")
    else:
        print(name.title() + ", You should to take poll.")
