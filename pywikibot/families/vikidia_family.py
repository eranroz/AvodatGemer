# -*- coding: utf-8  -*-
"""Family module for Vikidia."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 0a887445f8eda6ceabdb26d56d9b9f4d9e88e110 $'

from pywikibot import family


class Family(family.SubdomainFamily):

    """Family class for Vikidia."""

    name = 'vikidia'
    domain = 'vikidia.org'

    codes = ['ca', 'en', 'es', 'eu', 'fr', 'it', 'ru', 'scn']

    def protocol(self, code):
        """Return https as the protocol for this family."""
        return "https"

    def ignore_certificate_error(self, code):
        """Ignore certificate errors."""
        return True  # has self-signed certificate for a different domain.
