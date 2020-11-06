# -*- coding: utf-8 -*-

"""
Google Play Store Scraper

A web scraper for the Google Play Android app store.
"""

from version import VERSION

__version__ = VERSION

import logging

from play_scraper.api import (
    collection,
    details,
    developer,
    search,
    similar,
    suggestions,
    categories,
)


# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


logging.getLogger(__name__).addHandler(NullHandler())
