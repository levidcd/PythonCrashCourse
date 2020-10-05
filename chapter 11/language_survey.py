#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   language_survey.py
@Time    :   2020/10/05 15:51:35
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
from survey import AnonymousSurvey


question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('Enter q at any time to quit.\n')
while True:
    response = input('Language:')
    if response == 'q':
      break
    my_survey.store_response(response)

print("Thanks you to everyone who partcipated in the survey")
my_survey.show_results()