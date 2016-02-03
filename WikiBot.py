#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')


import pywikibot
from pywikibot import pagegenerators

import sqlite3

import re
import string


site = pywikibot.Site("he", "wikipedia")
conn = sqlite3.connect("cats.db")

cursor = conn.cursor()

def checkDB():
	conn.execute('''CREATE TABLE IF NOT EXISTS Words
					(
					ID Integer PRIMARY KEY NOT NULL,
					Category Text NOT NULL,
					Word Text NOT NULL,
					Value Real NOT NULL
					)
					''')
	conn.commit()

#Create a page generator with a total of {num} pages
def getRecentPagesGenerator(num):
	return pywikibot.pagegenerators.RecentChangesPageGenerator(total=num)

whitelist = string.letters + "ךםןףץאבגדהוזחטיכלמנסעפצקרשת" + ' '
#Get all the words with percentage of (greater or equal to a*100 %) to be in a text
def findSimilarity(pages, a):
	sWords = {}
	for page in pages:
		page = ''.join(c for c in page if c in whitelist)
		words = []
		for word in page.split():
			if(not word in words):
				words.append(word)
		for word in words:
			if(not word in sWords):
				sWords[word] = 1
			else:
				sWords[word] = sWords[word] + 1
	#for each word, assign value of it's percentage to be in a text
	sWords.update((x,(y*1.0)/len(pages)) for x, y in sWords.items())
	#return all of the words with percentage greater or equal to a*100 %
	return dict((k, v) for (k, v) in sWords.iteritems() if v >= a)

def insertWords(words, category):
	for word in words:
		sql = "INSERT INTO Words (Category, Word, Value) VALUES ('"+category+"', '"+word+"', "+str(words[word])+")"
		print "Executing: "+sql
		cursor.execute(sql)
		conn.commit()

def getWords(category):
	cursor.execute("SELECT Word, Value FROM Words WHERE Category='"+category+"'")
	tmp = {}
	for row in cursor:
		tmp[row[0]] = row[1]
	return tmp

def findNegativeSimilarities():
	cursor.execute("SELECT Word FROM Words")
	words = {}
	for word in cursor:
		if(not word in words):
			words[word] = 1
		else:
			words[word] = words[word]+1
	for word in words:
		cursor.execute("SELECT ID, Value FROM Words WHERE Word='"+word[0]+"'")
		rows = cursor.fetchall()
		for row in rows:
			sql = "UPDATE Words SET Value="+str(row[1]/words[word])+" WHERE ID="+str(row[0])
			print(sql)
			cursor.execute(sql)

def getPagesInCategory(category):
	cat = pywikibot.Category(site, category)
	gen = pagegenerators.CategorizedPageGenerator(cat, recurse=True, total=50)
	arr = []
	for page in gen:
		arr.append(page.text)
	return arr

#Functions from repl.it
#return value of page in category - evaluate(string,dict)
def evaluate(page, cat):
	value = 0.0
	for word in cat:
		if(word in page):
			value = value + cat[word]
	return value

#get the most evaluated category - getMax(array,dict<dict>)
def getMax(page, cats):
    values = {}
    for cat in cats:
        values[cat] = evaluate(page, cats[cat])/len(cats[cat])
    print(values)
    return max(values, key=values.get)

#end Functions from repl.it

#Check the DB for table, should actually do something only at the beginning.
checkDB()

ps1 = getPagesInCategory(u"קטגוריה:סרטים")
ps2 = getPagesInCategory(u"קטגוריה:סדרות טלוויזיה")
ps3 = getPagesInCategory(u"קטגוריה:אישים")
ps4 = getPagesInCategory(u"קטגוריה:מדינות העולם")

insertWords(findSimilarity(ps1, 0.75), "Movies")
insertWords(findSimilarity(ps2, 0.75), "TV Series")
insertWords(findSimilarity(ps3, 0.75), "People")
insertWords(findSimilarity(ps4, 0.75), "Countries")

findNegativeSimilarities()
#getWords("Movies")

p = pywikibot.Page(site, u"דוד בן-גוריון").text

print("The category is: " + getMax(p, {"Movies" : getWords("Movies"), "TV Series" : getWords("TV Series"), "People": getWords("People"), "Countries" : getWords("Countries")}))

#print(findSimilarity(pt, 0.75))
