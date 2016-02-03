# -*- coding: utf-8 -*-
"""Family module for Wikimedia chapter wikis."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: a6a515ab211312fa50c13db8f153e69952ed2b0c $'

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.SubdomainFamily, family.WikimediaFamily):

    """Family for Wikimedia chapters hosted on wikimedia.org."""

    name = 'wikimediachapter'
    code_aliases = {}

    codes = [
        'ar', 'br', 'bd', 'co', 'dk', 'fi', 'mk', 'mx', 'nl', 'no',
        'nyc', 'pl', 'rs', 'ru', 'se', 'ua', 'uk', 've',
    ]

    @property
    @deprecated
    def countries(self):
        """Deprecated."""
        return self.codes
