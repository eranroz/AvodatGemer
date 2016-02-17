#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms import tfidf as alg

d1 = "קוראים לי ניב גוברין, קוראים לי ניב גוברין, קוראים לי ניב גוברין"
d2 = "שלום! קוראים לי ניב, מה נשמע?"

term = "שלום"

print alg.tfidf(term, d1, [d1, d2])
