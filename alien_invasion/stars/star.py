#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:41 PM 
# File  : rain.py
# IDE   : PyCharm

# 13-1 and 13-2

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """表示星星的类"""

    def __init__(self, screen):
        """初始化星星并设置其起始位置"""
        super().__init__()
        self.screen = screen

        # 加载星星图像，并设置其rect属性
        self.image = pygame.image.load("E:/Desktop/python_introduction_to_programming/alien_invasion/images/star.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每个星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
