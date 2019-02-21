#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 8:36 PM 
# File  : restaurant_module.py 
# IDE   : PyCharm


class Restaurant:
    """描述餐馆的名字、类型和是否营业"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name.title() +
              " and its cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening !")

    def set_number_served(self, numbers):
        self.number_served = numbers

    def increment_number_served(self, add_number):
        self.number_served += add_number
