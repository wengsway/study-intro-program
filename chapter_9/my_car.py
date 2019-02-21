#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 8:15 PM 
# File  : my_car.py 
# IDE   : PyCharm


from car import Car

my_new_car = Car('audi','a4', '2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()