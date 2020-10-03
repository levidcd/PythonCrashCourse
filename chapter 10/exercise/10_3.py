#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   10_3.py
@Time    :   2020/10/03 14:02:28
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :   写入文件   
'''
# Start typing your code from here
name = input('what is your name?\n')

filename = 'guest.txt'
with open(filename, 'w') as file_object:
    print('ok')
