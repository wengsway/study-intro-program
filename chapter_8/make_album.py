#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 11:19 AM 
# File  : make_album.py 
# IDE   : PyCharm


def make_album(singer, album, numbers=''):
    album = {'Singer': singer.title(), 'Album': album.title()}
    if numbers:
        album['numbers'] = numbers
    return album


while True:
    print("\nPlease input a singer's name and his/her album's name")
    print("Input q at any time to quit")
    singer_name = input("singer's name: ")
    if singer_name == 'q':
        break

    album_name = input("album's name: ")
    if album_name == 'q':
        break

    album = make_album(singer_name,album_name)
    print(album)


'''
album_1 = make_album('Avril Lavigne', 'Let Go')
print(album_1)
album_2 = make_album('britney spears', 'femme fatale')
print(album_2)
album_3 = make_album('coldplay', 'yellow')
print(album_3)
album_4 = make_album('ed sheeran', 'deluxe', 8)
print(album_4)
'''