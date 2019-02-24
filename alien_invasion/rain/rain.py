#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:41 PM 
# File  : rain.py
# IDE   : PyCharm

# 13-3 and 13-4

import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """表示雨滴的类"""

    def __init__(self, settings, screen):
        """初始化雨滴并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # 加载雨滴图像，并设置其rect属性
        self.image = pygame.image.load("E:/Desktop/python_introduction_to_programming/alien_invasion/images/rain.bmp")
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """用于检测是否达到屏幕边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
