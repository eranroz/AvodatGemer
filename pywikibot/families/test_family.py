# -*- coding: utf-8  -*-
"""Family module for test.wikipedia.org."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 8f8815c7dae03bc7f3ffdd8fbbf14ce0ba7f7145 $'

from pywikibot import family


# The test wikipedia family
class Family(family.SingleSiteFamily, family.WikimediaFamily):

    """Family class for test.wikipedia.org."""

    name = 'test'
    domain = 'test.wikipedia.org'
    test_codes = ('test', )
