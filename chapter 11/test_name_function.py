#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_name_function.py
@Time    :   2020/10/05 15:13:04
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试 name_function.py"""

    def test_first_last_name(self):
        """"""
        formatted_name = get_formatted_name('jains','joplin')
        self.assertEqual(formatted_name,'Jains Joplin')

if __name__ == '__main__':
    unittest.main()
