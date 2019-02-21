#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:05 PM 
# File  : personal_info.py 
# IDE   : PyCharm

person_0 = {
    'first_name': 'weng',
    'last_name': 'quan',
    'age': '23',
    'city': 'fuding'
}
person_1 = {
    'first_name': 'ma',
    'last_name': 'yun',
    'age': '50',
    'city': 'hangzhou'
}
person_2 = {
    'first_name': 'ma',
    'last_name': 'huateng',
    'age': '49',
    'city': 'shenzhen'
}
people = [person_0, person_1, person_2]
for person in people:
    print(person)
