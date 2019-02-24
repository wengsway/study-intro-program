#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 4:01 PM 
# File  : add.py 
# IDE   : PyCharm

# 10-6 and 10-7

print("Give me two numbers, I'll add them to a number.")
print("The numbers you entered are both 0, quit.")
while True:
    first_number = input("First number: ")
    second_number = input("Second number: ")
    if first_number == '0' and second_number == '0':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("The numbers you entered are not all numbers !")
    else:
        print(answer)