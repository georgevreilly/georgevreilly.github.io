# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'George V. Reilly'
WWW_ROOT = 'http://www.georgevreilly.com/'

AUTHOR = 'George V. Reilly'
EMAIL = 'george@reilly.org'

FILTERS = ['reST', 'hyphenate', 'h1']
VIEWS = {
    '/blog/': {
        'filters': ['summarize', 'typography'],
        'view': 'index',
        'pagination': '/blog/page/:num/',
    },

    '/:year/:slug/': {
        'filters': ['typography'],
        'views': ['entry', 'draft'],
    },

    '/tag/:name/': {
        'filters': ['summarize'],
        'view':'tag',
        'pagination': '/tag/:name/:num/',
    },

    '/atom/': {
        'filters': ['h2', 'nohyphenate'],
        'view': 'atom',
    },
    '/rss/': {
        'filters': ['h2', 'nohyphenate'],
        'view': 'rss',
    },

    # # per tag Atom or RSS feed. Just uncomment to generate them.
    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/articles/': {'view': 'archive', 'template': 'articles.html'},

    '/sitemap.xml': {'view': 'sitemap'},

    # # Here are some more examples

    # '/:slug/' is a slugified url of your static page's title
    '/:slug/': {'view': 'page'},

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags},

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'},

    # # translations!
    # '/:year/:slug/:lang/': {'view': 'translation'},
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%Y-%m-%d %H:%M'
METASTYLE = 'native'
STATIC = ["media"]

GH_PAGES_BRANCH = "master" # User & Organization Pages use 'master', not 'gh-pages'

DEPLOYMENT = {
    "default": "ghp-import -b {branch} output && git push origin {branch}".format(branch=GH_PAGES_BRANCH)
}
DISQUS_SHORTNAME = 'georgevreilly'
