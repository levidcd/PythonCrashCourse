#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_survey.py
@Time    :   2020/10/05 16:10:24
@Author  :
@Version :   1.0
@Contact :
@WebSite :
@Desc    :
'''
# Start typing your code from here
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['a', 'b', 'c']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.response)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.response)


if __name__ == '__main__':
    unittest.main()
