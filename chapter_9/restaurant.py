#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 3:13 PM 
# File  : restaurant.py 
# IDE   : PyCharm

# 9-1 and 9-2 and 9-4


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


restaurant_1 = Restaurant('zi jingyuan', 'fast food')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('dong one', 'canteen')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant = Restaurant('dong san', 'canteen')
restaurant.number_served = 200
print(str(restaurant.number_served) + " people have eaten at this restaurant!")

restaurant_3 = Restaurant('dong si', 'canteen')
restaurant_3.set_number_served(150)
print(str(restaurant_3.number_served) + " people have eaten at this restaurant!")
restaurant_3.increment_number_served(100)
print(str(restaurant_3.number_served) + " people have eaten at this restaurant!")