#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site("he", "wikipedia")
cat = pywikibot.Category(site, u'קטגוריה:סרטים')
gen = pagegenerators.CategorizedPageGenerator(cat, recurse=True)
for page in gen:
    print page.title
