# -*- coding: utf-8  -*-
"""Family module for Battlestar Wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 685d7b17d1d0c91b6925556b7161a8ad11ab12b8 $'

from pywikibot import family


# The Battlestar Wiki family, a set of Battlestar wikis.
class Family(family.SubdomainFamily):

    """Family class for Battlestar Wiki."""

    name = 'battlestarwiki'
    domain = 'battlestarwiki.org'

    codes = ['en', 'de']

    interwiki_removals = ['fr', 'zh', 'es', 'ms', 'tr', 'simple']
