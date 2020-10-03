#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   10_1.py
@Time    :   2020/10/03 13:38:26
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(len(contents))
print(contents.rstrip())
print(len(contents.rstrip()))
