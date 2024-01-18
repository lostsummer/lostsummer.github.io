#!/usr/bin/env python3

AUTHOR = 'lostsummer'
SITENAME = '$ kill -1'
SITESUBTITLE = 'code less talk more :)'
SITEURL = 'https://www.lostsummer.love'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'
CC_LICENSE = "CC-BY-NC-SA"

PATH = 'content'
PLUGIN_PATHS = ['plugins']
STATIC_PATHS = ['images', 'extra']
FAVICON = 'images/favicon.ico'
PLUGINS = ['tag_cloud', 'i18n_subsites']
I18N_TEMPLATES_LANG = 'en'

THEME = 'themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False


TYPOGRIFY = True

CHECK_MODIFIED_METHOD = "mtime"

MENUITEMS = [
    ('Wiki', 'https://wiki.lostsummer.love/'),
]

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

DISQUS_SITENAME = 'lostsummer'

# Code syntax
PYGMENTS_STYLE = 'emacs'

# for zh fonts
CUSTOM_CSS = "extra/custom.css"

SHOW_ARTICLE_AUTHOR  = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = False

# Social widget
SOCIAL = (('github', 'https://github.com/lostsummer'),
        ('google+','https://plus.google.com/+FisherWong'),
        ('twitter','https://twitter.com/lostsummer'),
        ('facebook', 'https://www.facebook.com/fisher.wong.3'))

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

HIDE_SIDEBAR = False
PADDED_SINGLE_COLUMN_STYLE = False

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAGS_URL = 'tags.html'
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True
DISPLAY_AUTHORS_ON_SIDEBAR = True 

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

