#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 10:35 AM 
# File  : sideshot_ship.py 
# IDE   : PyCharm

# 12-5

import pygame


class Ship:

    def __init__(self, ss_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ss_settings = ss_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕左侧中央
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centery)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ss_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ss_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centery = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)