#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 9:08 PM 
# File  : test_employee.py 
# IDE   : PyCharm

# 11-3

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """对Employee的测试"""

    def setUp(self):
        """创建雇员信息，用于后续的测试方法"""
        self.my_employee = Employee('weng', 'sway', 10000)

    def test_give_default_raise(self):
        new_salary = self.my_employee.give_raise()
        self.assertEqual(15000, new_salary)

    def test_give_custom_raise(self):
        new_salary = self.my_employee.give_raise(10000)
        self.assertEqual(20000, new_salary)


if __name__ == '__main__':
    unittest.main()
