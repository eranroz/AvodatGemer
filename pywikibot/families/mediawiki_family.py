# -*- coding: utf-8  -*-
"""Family module for MediaWiki wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 069634dc27f187935a10669db6651a04d8fc125d $'

from pywikibot import family


# The MediaWiki family
class Family(family.WikimediaFamily, family.SingleSiteFamily):

    """Family module for MediaWiki wiki."""

    name = 'mediawiki'
    domain = 'www.mediawiki.org'
