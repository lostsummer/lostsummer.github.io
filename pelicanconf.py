#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lostsummer'
SITENAME = u'$ kill -1'
SITESUBTITLE = u'code less talk more :)'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'en'
CC_LICENSE = "CC-BY-NC-SA"

PATH = 'content'
PLUGIN_PATHS = ['plugins']
STATIC_PATHS = ['images', 'extra']
FAVICON = 'images/favicon.ico'
PLUGINS = ['pelican-toc', 'i18n_subsites']
THEME = 'themes/pelican-twitchy'
BOOTSTRAP_THEME = 'journal'
# THEME = 'themes/pelican-bootstrap3'
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# I18N_TEMPLATES_LANG = 'en'

TYPOGRIFY = True

CHECK_MODIFIED_METHOD = "mtime"

DISPLAY_TAGS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_RECENT_POSTS_ON_MENU = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
NEWEST_FIRST_ARCHIVES = True
RESPONSIVE_IMAGES = True

#SUMMARY_MAX_LENGTH = 20
EXPAND_LATEST_ON_INDEX = 1
RECENT_POST_COUNT = 5


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = 'lostsummer'
#DISQUS_LOAD_LATER = True

# Blogroll
LINKS = (
          ('MY LIFE BLOG', 'http://1984.love/'),
          ('MY WIKI', 'http://wiki.lostsummer.love/'),
        )

# Code syntax
PYGMENTS_STYLE = 'emacs'

#CUSTOM_CSS = "extra/custom.css"

# Social widget
SOCIAL = (('github', 'https://github.com/lostsummer'),
        ('google+','https://plus.google.com/+FisherWong'),
        ('twitter','https://twitter.com/lostsummer'),
        ('facebook', 'https://www.facebook.com/fisher.wong.3'),
        ('Email', 'mailto:lostsummer@gmail.com'))

DEFAULT_PAGINATION = False

SHARE = True


TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

