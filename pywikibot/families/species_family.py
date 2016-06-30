# -*- coding: utf-8  -*-
"""Family module for Wikimedia species wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 204b39a96a28cfd425c498b781386771f58f1fb7 $'

from pywikibot import family


# The wikispecies family
class Family(family.WikimediaOrgFamily):

    """Family class for Wikimedia species wiki."""

    name = 'species'

    def __init__(self):
        """Constructor."""
        super(Family, self).__init__()

        self.interwiki_forward = 'wikipedia'
