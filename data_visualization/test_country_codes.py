#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/2/2019 2:29 PM 
# File  : test_country_codes.py 
# IDE   : PyCharm

# 16-8

import unittest

from country_codes import get_country_code


class TestGetCountryCode(unittest.TestCase):
    """测试 country_codes.py"""

    def test_country_codes_singer(self):
        country_name = 'China'
        code = get_country_code(country_name)
        self.assertEqual(code, 'cn')

    def test_country_codes_inner(self):
        country_name = 'Iran, Islamic Republic of'
        code = get_country_code(country_name)
        self.assertEqual(code, 'ir')

    def test_country_codes_two_words(self):
        country_name = 'United Kingdom'
        code = get_country_code(country_name)
        self.assertEqual(code, 'gb')


if __name__ == '__main__':
    unittest.main()
