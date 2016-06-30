#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8
import pywikibot
from pywikibot import pagegenerators
import pandas as pd

def getPagesInCategory(category, amount):
	cat = pywikibot.Category(site, category)
	gen = pagegenerators.CategorizedPageGenerator(cat, recurse=True, total=amount)
	arr = []
	for page in gen:
		arr.append(page.text)
	return arr

def getRecentPages(num):
    return pagegenerators.RecentChangesPageGenerator(total=num)
