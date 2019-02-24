#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 9:51 PM 
# File  : for_dinner.py 
# IDE   : PyCharm


# 3-4
names = ['weng quan', 'jack ma', 'tony']
print(names[0].title() + "," + " let's for dinner!")
print(names[1].title() + "," + " let's for dinner!")
print(names[2].title() + "," + " let's for dinner!")
print("The guest " + names[2].title() + " cannot take dinner with me!")
# 3-5
names[2] = "trump"
print(names)
print(names[0].title() + "," + " let's for dinner!")
print(names[1].title() + "," + " let's for dinner!")
print(names[2].title() + "," + " let's for dinner!")
# 3-6
print("I get a big table!")
names.insert(0, "wang jianlin")
names.insert(2, "ao bama")
names.append("mo keer")
print(names)
print(names[0].title() + "," + " let's for dinner!")
print(names[1].title() + "," + " let's for dinner!")
print(names[2].title() + "," + " let's for dinner!")
print(names[3].title() + "," + " let's for dinner!")
print(names[4].title() + "," + " let's for dinner!")
print(names[5].title() + "," + " let's for dinner!")
# 3-9
print("I invite " + str(len(names)) + " guests for dinner!")
# 3-7
print("Sorry,I can only take dinner with two guys together.")
popped_names = names.pop()
print(popped_names.title() + "," + " sorry,I cannot invite you to dinner with me!")
popped_names = names.pop()
print(popped_names.title() + "," + " sorry,I cannot invite you to dinner with me!")
popped_names = names.pop()
print(popped_names.title() + "," + " sorry,I cannot invite you to dinner with me!")
popped_names = names.pop()
print(popped_names.title() + "," + " sorry,I cannot invite you to dinner with me!")

print(names[0].title() + "," + "hey,you are still in my invitation list.")
print(names[1].title() + "," + "hey,you are still in my invitation list.")
del names[0]
del names[0]
print(names)
