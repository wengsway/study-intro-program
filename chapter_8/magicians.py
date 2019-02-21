#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 1:28 PM 
# File  : magicians.py 
# IDE   : PyCharm


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    changed_magicians = []
    for magician in magicians:
        changed_magicians.append("the Great " + magician)
    return changed_magicians


magicians = ['I', 'You', 'He', 'She']
show_magicians(make_great(magicians[:]))
show_magicians(magicians)
