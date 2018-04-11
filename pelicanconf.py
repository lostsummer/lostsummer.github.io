#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lostsummer'
SITENAME = u'$ kill -1'
SITESUBTITLE = u'code less talk more :)'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'

PATH = 'content'
PLUGIN_PATHS = ['plugins']
STATIC_PATHS = ['images', 'extra']
FAVICON = 'images/favicon.ico'
PLUGINS = ['pelican-toc']
THEME = 'themes/pelican-twitchy'
CHECK_MODIFIED_METHOD = "mtime"
DISPLAY_TAGS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_MENU = True
EXPAND_LATEST_ON_INDEX = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
NEWEST_FIRST_ARCHIVES = True
RESPONSIVE_IMAGES = True
CC_LICENSE = "CC-BY-NC-SA"
SUMMARY_MAX_LENGTH = 0



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = 'lostsummer'
DISQUS_LOAD_LATER = True

# Blogroll
LINKS = (
          ('MY LIFE BLOG', 'http://1984.love/'),
          ('MY WIKI', 'http://wiki.lostsummer.love/'),
        )

# Code syntax
PYGMENTS_STYLE = 'manni'
BOOTSTRAP_THEME = 'paper'
SHARE = True
CUSTOM_CSS = "extra/custom.css"

# Social widget
SOCIAL = (('github', 'https://github.com/lostsummer'),
        ('google+','https://plus.google.com/+FisherWong'),
        ('twitter','https://twitter.com/lostsummer'),
        ('facebook', 'https://www.facebook.com/fisher.wong.3'),
        ('Email', 'mailto:lostsummer@gmail.com'))

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

