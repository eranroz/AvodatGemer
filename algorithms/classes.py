#!/usr/bin/python
# -*- coding: utf-8 -*-

# encoding=utf8
class CategorizedPage:
    value = u""
    isTrue = False
    def __init__(self, value, isTrue):
        self.value = value
        self.isTrue = isTrue

#kldavenport.com/pure-python-decision-trees
class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col
        self.value=value
        self.results=results
        self.tb=tb
        self.fb=fb
