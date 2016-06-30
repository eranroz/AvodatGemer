# -*- coding: utf-8  -*-
"""Family module for Wikitech."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: f21ba2b404a402390520a882bbabb8dcf7aa32d9 $'

from pywikibot import family


# The Wikitech family
class Family(family.WikimediaOrgFamily):

    """Family class for Wikitech."""

    name = 'wikitech'
    code = 'en'

    def protocol(self, code):
        """Return the protocol for this family."""
        return 'https'
