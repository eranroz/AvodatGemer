#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pywikibot
import time
from pywikibot.xmlreader import XmlDump
from pywikibot import pagegenerators
from algorithms import cwe
from algorithms import tfidf

#dump = XmlDump('hewiki-20160501-pages-articles.xml.bz2')
dump = XmlDump("More Movies.xml")
cwe = cwe()
a = 0
s = 0
print "movies classified as not movies: \n"
for page in dump.parse():
    s += 1
    #cat = cwe.getMax(page.text, {"Movies" : cwe.getWords("Movies"), "TV Series" : cwe.getWords("TV Series"), "People": cwe.getWords("People"), "Countries" : cwe.getWords("Countries")})
    cat = tfidf.getMax(page.text, {"Movies" : cwe.getWords("Movies"), "TV Series" : cwe.getWords("TV Series"), "People": cwe.getWords("People"), "Countries" : cwe.getWords("Countries")})
    if cat != "Movies":
        a += 1
        print str(a) + "." + page.title + ", " + cat
print "Total pages: " + str(s)
