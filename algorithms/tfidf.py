#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import re
import string
import math
import time

conn = sqlite3.connect('cats.db')
cursor = conn.cursor()

def filterString(document):
    whitelist = u'אבגדהוזחטיכלמנסעפצקרשתךםןףץ '
    document = ''.join(c for c in document if c in whitelist)
    return document

def tf(term, documents):
    if(len(documents) == 0):
        return 0
    freqSum = 0.0
    for document in documents:
        #document = filterString(document)
        appearances = 0.0
        for word in document.split():
            if(word == term):
                appearances += 1.0
        freqSum += appearances/len(document)
    return freqSum/len(documents)

def idf(term, documents):
    count = 0.0
    if len(documents) == 0:
        return 0
    for document in documents:
        #document = filterString(document)
        if term in document.split():
            count += 1.0
    if count == 0:
        return 0
    return math.log10(len(documents)/count)

def tfidf(term, documents):
    return tf(term, documents) * (idf(term, documents) + 1)

def getValues(category, documents):
    values = {}
    maximum = -2147483648
    minimum = 2147438647
    for document in documents:
        document = filterString(document)
        words = []
        for word in document.split():
            if not word in words:
                values[word] = tfidf(word, documents)
                if(values[word] > maximum):
                    maximum = values[word]
                if(values[word] < minimum):
                    minimum = values[word]
                words.append(word)
    print("maximum: " + str(maximum) + ", minimum: " + str(minimum))
    for value in values:
        values[value] = (values[value]-minimum)/(maximum-minimum)
        if(values[value]>=0.25):
            sql="INSERT INTO tfidfWords (Category, Word, Value) VALUES ('" + category + "','" + value + "'," + str(values[value]) + ")"
            print("Executing: " + sql)
            cursor.execute(sql)
    conn.commit()

def checkDB():
    conn.execute("""CREATE TABLE IF NOT EXISTS tfidfWords
    (
    ID Integer PRIMARY KEY NOT NULL,
    Category Text NOT NULL,
    Word Text NOT NULL,
    Value Real NOT NULL
    )""")
    conn.commit()

def resetTable():
    sql = "DROP TABLE IF EXISTS tfidfWords"
    conn.execute(sql)
    conn.commit()
    checkDB()

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def evaluate(page, cat):
    page = filterString(page)
    words = page.split()
    value = 0.0
    for word in cat:
        if word in words:
            value += cat[word]
    return value

def getMax(page, cats):
    values = {}
    for cat in cats:
        values[cat] = evaluate(page, cats[cat]) / len(cats[cat])
    #print values
    print(values)
    return max(values, key=values.get)
