# -*- coding: utf-8  -*-
"""Family module for Incubator Wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 493ef9b692599bcea93b2a28399809c2f5b14f04 $'

from pywikibot import family


# The Wikimedia Incubator family
class Family(family.WikimediaOrgFamily):

    """Family class for Incubator Wiki."""

    name = 'incubator'
