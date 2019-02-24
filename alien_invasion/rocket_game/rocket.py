#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 10:52 PM 
# File  : rocket.py 
# IDE   : PyCharm

# 12-3

import pygame


class Rocket:

    def __init__(self, screen):
        """初始化火箭并设置其初始位置"""
        self.screen = screen

        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将火箭放在屏幕中央
        self.rect.center = self.screen_rect.center

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1


    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)