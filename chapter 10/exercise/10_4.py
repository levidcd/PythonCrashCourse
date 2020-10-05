#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   10_4.py
@Time    :   2020/10/03 14:06:12
@Author  :
@Version :   1.0
@Contact :
@WebSite :
@Desc    :   写入多行
'''
# Start typing your code from here

filename = 'guest_book.txt'

prompt = 'What is your name:\n'
prompt += "(Enter 'quit' when you are finished.)\n"
while True:
    name = input(prompt)

    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
            print(f'welcome!{name}.')
