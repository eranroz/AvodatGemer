#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import re
import string
import math

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
