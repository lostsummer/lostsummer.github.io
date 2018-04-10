#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lostsummer'
SITENAME = u'# kill -1'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['plugins']
STATIC_PATHS = ['images', 'extra']
FAVICON = 'images/favicon.ico'
SITELOGO = 'images/logo.jpeg'
SITELOGO_SIZE = 20
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Learning'
PLUGINS = ['extract_toc']
DISPLAY_TAGS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_MENU = True
EXPAND_LATEST_ON_INDEX = True


TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

SUMMARY_MAX_LENGTH = 5

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'themes/pelican-twitchy'

DISQUS_SITENAME = 'lostsummer'
DISQUS_LOAD_LATER = True

# Blogroll
LINKS = (
          ('MY LIFE BLOG', 'http://1984.love/'),
          ('MY WIKI', 'http://wiki.lostsummer.love/'),
        )

# Code syntax
PYGMENTS_STYLE = 'monokai'
BOOTSTRAP_THEME = 'slate'
SHARE = True
CUSTOM_CSS = "extra/custom.css"

# Social widget
SOCIAL = (('github', 'https://github.com/lostsummer'),
        ('google+','https://plus.google.com/+FisherWong'),
        ('twitter','https://twitter.com/lostsummer'),
        ('facebook', 'https://www.facebook.com/fisher.wong.3'),
        ('Email', 'mailto:lostsummer=at=gmail.com'))

DEFAULT_PAGINATION = False

TYPOGRIFY = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.toc': {
            'anchorlink': True
        },
    }
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

