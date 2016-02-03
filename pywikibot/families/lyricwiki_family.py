# -*- coding: utf-8  -*-
"""Family module for LyricWiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 9483c6550b5ad688dfa27a0f99601d2f8b90d09f $'

from pywikibot import family


# The LyricWiki family

# user_config.py:
# usernames['lyricwiki']['en'] = 'user'
class Family(family.SingleSiteFamily, family.WikiaFamily):

    """Family class for LyricWiki."""

    name = 'lyricwiki'
    code = 'en'
    domain = 'lyrics.wikia.com'
