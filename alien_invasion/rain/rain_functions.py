#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:41 PM 
# File  : rain_functions.py
# IDE   : PyCharm

# 13-3 and 13-4

import sys
import pygame

from rain import Rain


def check_keys():
    """检测响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, rains):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(settings.bg_color)
    rains.draw(screen)
    pygame.display.flip()


def get_number_rains_x(settings, rain_width):
    """计算每行可容纳多少个雨滴"""
    available_space_x = settings.screen_width - rain_width
    number_rains_x = int(available_space_x / (2 * rain_width))
    return number_rains_x


def get_number_rows(settings, rain_height):
    """计算屏幕可容纳多少行雨滴"""
    available_space_y = settings.screen_height - rain_height
    number_rows = int(available_space_y / (2 * rain_height))
    return number_rows


def create_rain(settings, screen, rains, rain_number, row_number):
    """创建一个雨滴并将其放在当前行"""
    rain = Rain(settings, screen)
    rain_width = rain.rect.width
    rain.x = rain_width + 2 * rain_width * rain_number
    rain.rect.x = rain.x
    rain.rect.y = rain.rect.y + 2 * rain.rect.height * row_number
    rains.add(rain)


def create_fleet(settings, screen, rains):
    """创建雨滴群"""
    # 创建一个雨滴，并计算一行可容纳多少个雨滴
    rain = Rain(settings, screen)
    number_rains_x = get_number_rains_x(settings, rain.rect.width)
    number_rows = get_number_rows(settings, rain.rect.height)

    for row_number in range(number_rows):
        for rain_number in range(number_rains_x):
            create_rain(settings, screen, rains, rain_number, row_number)


def change_direction(settings, rains):
    """用于设置方向"""
    for rain in rains.sprites():
        rain.rect.y += settings.drop_speed


def continue_rains(settings, screen, rains):
    for rain in rains.sprites():
        if rain.check_edges():
            new_rain = Rain(settings, screen)
            new_rain.rect.x = rain.rect.x
            rains.remove(rain)
            rains.add(new_rain)

