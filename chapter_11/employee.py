#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 9:03 PM 
# File  : employee.py 
# IDE   : PyCharm

# 11-3


class Employee():
    """关于年薪管理的一次模拟"""

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, money=5000):
        self.salary += money
        return self.salary
