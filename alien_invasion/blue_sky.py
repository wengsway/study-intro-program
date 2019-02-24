#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 8:47 PM 
# File  : blue_sky.py 
# IDE   : PyCharm

# 12-1

import pygame


def blue_sky():
    """创建一个背景为蓝色的pygame窗口"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    screen.fill((0, 0, 255))
    pygame.display.set_caption("Blue Sky")
    pygame.display.flip()


blue_sky()
