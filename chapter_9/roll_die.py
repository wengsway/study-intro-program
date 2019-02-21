#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:15 PM 
# File  : roll_die.py 
# IDE   : PyCharm

from random import randint


class Die:

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        i = 1
        while i <= 10:
            print(randint(1, self.sides))
            i += 1


six_die = Die()
six_die.roll_die()

ten_die = Die()
ten_die.sides = 10
print("\n")
ten_die.roll_die()

twenty_die = Die()
twenty_die.sides = 20
print("\n")
twenty_die.roll_die()
