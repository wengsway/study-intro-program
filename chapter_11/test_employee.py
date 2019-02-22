#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 9:08 PM 
# File  : test_employee.py 
# IDE   : PyCharm

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """对Employee的测试"""

    def setUp(self):
        """创建雇员信息，用于后续的测试方法"""
        self.my_employee = Employee('weng', 'sway', 10000)

    def test_give_default_raise(self):
        res = self.my_employee.give_raise()
        self.assertEqual(15000, res)

    def test_give_custom_raise(self):
        res = self.my_employee.give_raise(10000)
        self.assertEqual(20000, res)


if __name__ == '__main__':
    unittest.main()
