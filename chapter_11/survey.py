#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/22/2019 8:11 PM 
# File  : survey.py 
# IDE   : PyCharm

class AnonymousSurvey():
    """收集匿名调茶问卷的答案"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调茶问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response.title())

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
