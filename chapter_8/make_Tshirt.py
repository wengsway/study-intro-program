#!/usr/bin/env python  
# -*- coding:utf-8 _*-
# Author: Wengs
# Time  : 2/20/2019 10:43 AM 
# File  : make_Tshirt.py
# IDE   : PyCharm

# 8-3 and 8-4

def make_shirt(chima, word):
    print("\nT-shirt's chima is " + chima + ", the word printed are:" + word + ".")


make_shirt('10','My Name is WengSway')
make_shirt(chima='8',word='My name is Weng Quan')


def make_big_shirt(chima,word='I love Python'):
    print("\nT-shirt's chima is " + chima + ", the word printed are:" + word + ".")


make_big_shirt('20')
make_big_shirt('10')
make_big_shirt('5','I am a boy')