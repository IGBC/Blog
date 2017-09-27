#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Segfault'
SITENAME = 'Segfaults\'s Ramblings' 
SITEDESCRIPTION = "\"If it isn't broken... Break it!\""
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['.']

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('IGBC', 'https://www.github.com/IGBC'),
          ('@nasasegcorp', 'https://twitter.com/nasasegcorp'),)

DEFAULT_PAGINATION = 20

THEME = 'themes/flex-sigsegv.tech'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
