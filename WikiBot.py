#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8
import sys
from algorithms import cwe
from algorithms import tfidf
import pageLoader

try:
    reload(sys)
    sys.setdefaultencoding('utf8')  # python2
except NameError:
    pass


import pywikibot
from pywikibot import pagegenerators


site = pywikibot.Site("he", "wikipedia")
cwe = cwe()

'''
ps1 = pageLoader.getPagesInCategory(u"קטגוריה:סרטים", 50)
ps2 = pageLoader.getPagesInCategory(u"קטגוריה:סדרות טלוויזיה", 50)
ps3 = pageLoader.getPagesInCategory(u"קטגוריה:אישים", 50)
ps4 = pageLoader.getPagesInCategory(u"קטגוריה:מדינות העולם", 50)
'''
'''
cwe.resetTable()

cwe.insertWords(cwe.findSimilarity(ps1, 0.75), "Movies")
cwe.insertWords(cwe.findSimilarity(ps2, 0.75), "TV Series")
cwe.insertWords(cwe.findSimilarity(ps3, 0.75), "People")
cwe.insertWords(cwe.findSimilarity(ps4, 0.75), "Countries")

cwe.fixValues()
'''
'''
tfidf.resetTable()
tfidf.getValues("Movies", ps1)
tfidf.getValues("TV Series", ps2)
tfidf.getValues("People", ps3)
tfidf.getValues("Countries", ps4)
'''

p = pywikibot.Page(site, u"נפתלי בנט").text

#print("The category is: " + tfidf.getMax(p, {"Movies" : cwe.getWords("Movies"), "TV Series" : cwe.getWords("TV Series"), "People": cwe.getWords("People"), "Countries" : cwe.getWords("Countries")}))

print("The category is: " + cwe.getMax(p, {"Movies" : cwe.getWords("Movies"), "TV Series" : cwe.getWords("TV Series"), "People": cwe.getWords("People"), "Countries" : cwe.getWords("Countries")}))


#print(findSimilarity(pt, 0.75))
