#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:10 PM 
# File  : vacation_spot.py 
# IDE   : PyCharm

vacation_spot = {}
promt = "If you could visit one place in the world, where would you go?"
active = True
while active:
    name = input("Please input your name: ")
    vacation = input(promt)
    vacation_spot[name] = vacation
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        active = False
print("\n--- Survey Result ---")
for name, vacation in vacation_spot.items():
    print(name.title() + " would like go to " + vacation.title() + ".")
