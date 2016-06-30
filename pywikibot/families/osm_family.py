# -*- coding: utf-8  -*-
"""Family module for OpenStreetMap wiki."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: e2311ee8b10fe1fe741f7d32684823f3ad35386a $'

from pywikibot import family


# The project wiki of OpenStreetMap (OSM).
class Family(family.SingleSiteFamily):

    """Family class for OpenStreetMap wiki."""

    name = 'osm'
    domain = 'wiki.openstreetmap.org'
    code = 'en'

    def protocol(self, code):
        """Return https as the protocol for this family."""
        return "https"
