#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   10_5.py
@Time    :   2020/10/03 14:31:25
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
filename = 'programming.txt'

prompt = 'Why you like programming:\n'
prompt += "(Enter 'quit' when you are finished.)\n"
while True:
    name = input(prompt)

    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")