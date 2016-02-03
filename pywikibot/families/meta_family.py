# -*- coding: utf-8  -*-
"""Family module for Meta Wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: f59c79b46cecd252709e76fd134a78c4659e3a06 $'

from pywikibot import family


# The meta wikimedia family
class Family(family.WikimediaOrgFamily):

    """Family class for Meta Wiki."""

    name = 'meta'

    def __init__(self):
        """Constructor."""
        super(Family, self).__init__()

        self.interwiki_forward = 'wikipedia'
        self.cross_allowed = ['meta', ]
