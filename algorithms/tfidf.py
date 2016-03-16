#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import re
import string
import math

conn = sqlite3.connect('cats.db')
cursor = conn.cursor()

def filter(document):
    whitelist = 'אבגדהוזחטיכלמנסעפצקרשת' + ' ' + 'ךםןףץ'
    document = ''.join(c for c in document if c in whitelist)
    return document

def tf(term, document):
    count = 0
    document = filter(document)
    for word in document.split():
        if(word==term):
            count += 1
    return count

def idf(term, documents):
    count = 0.0
    if len(documents) == 0:
        return 0
    for document in documents:
        document = filter(document)
        print document
        if term in document.split():
            count += 1.0
    if count == 0:
        return 0
    return math.log10(len(documents)/count)

def tfidf(term, document, documents):
    return tf(term, document) * (idf(term, documents) + 1)

def getValues(category, documents):
    values = {}
    occurances = {}
    for document in documents:
        words = []
        for word in filter(document):
            if not word in words:
                if not word in values:
                    values[word] = tfidf(word, document, documents)
                    occurances[word] = 1
                else:
                    values[word] += tfidf(word, documents, documents)
                    occurances[word] += 1
                words.append(word)
    for value in values:
        sql="INSERT INTO tfidfWords (Category, Word, Value) VALUES ('" + category + "','" + value + "'," + str(values[value]/occurances[value]) + ")"
        print "Executing: " + sql
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
