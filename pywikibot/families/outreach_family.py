# -*- coding: utf-8  -*-
"""Family module for Wikimedia outreach wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 412a273847ff5204ff85ff39cb6a6345810af1fe $'

from pywikibot import family


# Outreach wiki custom family
class Family(family.WikimediaOrgFamily):

    """Family class for Wikimedia outreach wiki."""

    name = 'outreach'

    def __init__(self):
        """Constructor."""
        super(Family, self).__init__()

        self.interwiki_forward = 'wikipedia'
