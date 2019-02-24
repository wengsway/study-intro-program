#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:41 PM 
# File  : rain_functions.py
# IDE   : PyCharm

# 13-1 and 13-2

import sys
import pygame
from random import randint

from star import Star


def check_keys():
    """检测响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, stars):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()


def get_number_stars_x(settings, star_width):
    """计算每行可容纳多少个星星"""
    available_space_x = settings.screen_width - star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x


def get_number_rows(settings, star_height):
    """计算屏幕可容纳多少行星星"""
    available_space_y = settings.screen_height - star_height
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows

# def create_star(screen, stars, star_number, row_number):
def create_star(screen, stars, star_number):
    """创建一个星星并将其放在当前行"""
    star = Star(screen)
    star_width = star.rect.width
    # star.x = star_width + 2 * star_width * star_number
    star.x = randint(0, 1000) + star_width
    star.rect.x = star.x
    # star.y = star.rect.height + 2 * star.rect.height * row_number
    star.rect.y = randint(0, 1000) + star.rect.height
    stars.add(star)


def create_fleet(settings, screen, stars):
    """创建星星群"""
    # 创建一个星星，并计算一行可容纳多少个星星
    star = Star(screen)
    number_stars_x = get_number_stars_x(settings, star.rect.width)
    # number_rows = get_number_rows(settings, star.rect.height)

    # for row_number in range(number_rows):
    for star_number in range(number_stars_x):
        create_star(screen, stars, star_number)

