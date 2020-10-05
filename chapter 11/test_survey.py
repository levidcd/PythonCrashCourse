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
    def test_store_single_response(self):
        question = "language?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.response)

    def test_store_three_response(self):
        question = "language?"
        my_survey = AnonymousSurvey(question)
        responses = ['a', 'b', 'c']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.response)

if __name__ == '__main__':
    unittest.main()