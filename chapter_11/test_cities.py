#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 7:53 PM 
# File  : test_cities.py 
# IDE   : PyCharm

# 11-2

import unittest
from city_function import city_function


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        string = city_function('santiago', 'chile')
        self.assertEqual(string, 'Santiago, Chile')

    def test_city_country_population(self):
        string = city_function('santiago', 'chile', population=5000000)
        self.assertEqual(string, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
