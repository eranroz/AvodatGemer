# -*- coding: utf-8 -*-
"""Family module for Wikivoyage."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 5f5a4dd97ee174655a276d7585e97000c9c58f8d $'

# The new wikivoyage family that is hosted at wikimedia

from pywikibot import family


class Family(family.SubdomainFamily, family.WikimediaFamily):

    """Family class for Wikivoyage."""

    name = 'wikivoyage'

    def __init__(self):
        """Constructor."""
        self.languages_by_size = [
            'en', 'de', 'fr', 'it', 'nl', 'pt', 'pl', 'ru', 'he', 'es', 'vi',
            'sv', 'zh', 'el', 'ro', 'uk', 'fa',
        ]

        super(Family, self).__init__()

        # Global bot allowed languages on
        # https://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = ['es', 'ru', ]
