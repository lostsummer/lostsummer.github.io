#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'lostsummer'
SITENAME = 'LOST IN CODE'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
FAVICON = 'images/favicon.ico'
#SITELOGO = 'images/logo.jpeg'
#SITELOGO_SIZE = 20
#HIDE_SITENAME = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Tech'
PLUGINS = ['tag_cloud']
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 30
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True
#DISPLAY_TAGS_INLINE = True
TAGS_URL='tags.html'
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True


TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

SUMMARY_MAX_LENGTH = None
2
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'pelican-themes/pelican-bootstrap3'

GITHUB_USER = 'lostsummer'
DISQUS_SITENAME = 'lostsummer'

# Blogroll
LINKS = (
          ('Family Blog', 'http://1984.love/'),
          ('Personal Wiki', 'http://wiki.lostsummer.love/'),
        )

# Code syntax
PYGMENTS_STYLE = 'zenburn'

# Social widget
SOCIAL = (('github', 'https://github.com/lostsummer'),
        ('google+','https://plus.google.com/+FisherWong'),
        ('twitter','https://twitter.com/lostsummer'),
        ('facebook', 'https://www.facebook.com/fisher.wong.3'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
