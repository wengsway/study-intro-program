#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 3:33 PM 
# File  : cars.py 
# IDE   : PyCharm


class Car:
    """模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """"返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """打印一条支出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, miles):
        """
        将里程表数量设置为指定的值
        禁止将里程表读数往回调
        """
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mile):
        """将里程数增加指定的量"""
        self.odometer_reading += mile


my_new_car = Car('audi', 'a4', '2017')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""
# 修改属性值的方法之一：通过实例直接访问该属性并进行修改
your_new_car = Car('bmw', 'q5', '2018')
print(your_new_car.get_descriptive_name())
your_new_car.odometer_reading = 30
your_new_car.read_odometer()
"""
"""
# 修改属性值的方法之二：通过方法修改属性的值，在实例中调用该方法并输入新的数值
my_new_car.update_odometer(35)
my_new_car.read_odometer()
# 用于检验禁止回调里程数的功能是否正常
my_new_car.update_odometer(20)
my_new_car.read_odometer()
"""
"""
# 修改属性值的方法之三：通过新增一个方法对属性的值进行递增
my_used_car = Car('subaru', 'outback', '2013')
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
"""
