#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 4:16 PM 
# File  : electric_car.py 
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


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, batteru_size=70):
        """初始化电瓶的属性"""
        self.battery_size = batteru_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_ranges(self):
        """打印一条消息，支出电瓶的续航里程"""
        global ranges
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270
        message = "This car can go approximately " + str(ranges) + " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """对电瓶进行升级"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', '2017')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_ranges()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_ranges()
