#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   names.py
@Time    :   2020/10/05 15:20:00
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here

from name_function import get_formatted_name
print("Enter 'q' at any time to quit")
while True:
    first = input("please give a first name\n")
    if first == 'q':
        break
    last = input("please give a last name\n")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("Neatly: " + formatted_name)
