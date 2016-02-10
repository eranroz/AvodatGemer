#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8
import sys
from algorithms import cwe

reload(sys)
sys.setdefaultencoding('utf8')


import pywikibot
from pywikibot import pagegenerators


site = pywikibot.Site("he", "wikipedia")
cwe = cwe()

#Create a page generator with a total of {num} pages
def getRecentPagesGenerator(num):
	return pywikibot.pagegenerators.RecentChangesPageGenerator(total=num)

def getPagesInCategory(category):
	cat = pywikibot.Category(site, category)
	gen = pagegenerators.CategorizedPageGenerator(cat, recurse=True, total=2)
	arr = []
	for page in gen:
		arr.append(page.text)
	return arr

ps1 = getPagesInCategory(u"קטגוריה:סרטים")
ps2 = getPagesInCategory(u"קטגוריה:סדרות טלוויזיה")
ps3 = getPagesInCategory(u"קטגוריה:אישים")
ps4 = getPagesInCategory(u"קטגוריה:מדינות העולם")

cwe.resetTable()

cwe.insertWords(cwe.findSimilarity(ps1, 0.75), "Movies")
cwe.insertWords(cwe.findSimilarity(ps2, 0.75), "TV Series")
cwe.insertWords(cwe.findSimilarity(ps3, 0.75), "People")
cwe.insertWords(cwe.findSimilarity(ps4, 0.75), "Countries")

cwe.findNegativeSimilarities()
#getWords("Movies")

p = pywikibot.Page(site, u"דוד בן-גוריון").text

print("The category is: " + cwe.getMax(p, {"Movies" : cwe.getWords("Movies"), "TV Series" : cwe.getWords("TV Series"), "People": cwe.getWords("People"), "Countries" : cwe.getWords("Countries")}))

#print(findSimilarity(pt, 0.75))
