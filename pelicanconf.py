#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Segfault'
SITENAME = 'Segfaults\'s Ramblings' 
SITEDESCRIPTION = ""
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['.', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}


TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

PLUGINS = ['neighbors']

# URL Settings
AUTHOR_URL = '' 
AUTHOR_SAVE_AS = '' # Turn Author Pages Off
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_LANG_URL = 'articles/{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{lang}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('@IGBC', 'https://www.github.com/IGBC'),
          ('@IGBC', 'https://gitlab.com/IGBC'),
          ('@altsegcat', 'https://twitter.com/altsegcat'),)

THEME = 'themes/flex-sigsegv.tech'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
