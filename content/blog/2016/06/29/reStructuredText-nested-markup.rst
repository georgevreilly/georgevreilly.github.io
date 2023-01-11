---
title: "reStructuredText Nested Markup"
date: "2016-06-29"
permalink: "/blog/2016/06/29/reStructuredTextNestedMarkup.html"
tags: [reStructuredText, til]
---



I use reStructuredText__ for both this blog and the `MetaBrite DevBlog`__.
This blog is built with `Acrylamid`__, while the MetaBrite blog is built with `Nikola`__.

__ https://en.wikipedia.org/wiki/ReStructuredText
__ http://www.metabrite.com/devblog/
__ https://posativ.org/acrylamid/
__ https://getnikola.com/

Yesterday__ I used a link (|~/.pgpass|_) that styled the link as an *inline literal*;
i.e., in the ``code`` font.
ReStructuredText doesn't support nested markup,
but you can `pull it together`__ with a two-step `substitution reference`__::

    Here you have |optparse.OptionParser|_.

    .. |optparse.OptionParser| replace:: ``optparse.OptionParser`` documentation
    .. _optparse.OptionParser: http://docs.python.org/library/optparse.html

__ /blog/2016/06/28/CreatingANewPostgreSQLDatabaseAtRDS.html
__ http://stackoverflow.com/a/4836544/6364
__ http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-references

This is tedious as you have to create a pair of directives
for every such link that you wish to style.

Nested inline markup has been on the todo list for 15 years—it ain't happening.

.. |~/.pgpass| replace:: ``~/.pgpass``
.. _~/.pgpass:
    https://blog.sleeplessbeastie.eu/2014/03/23/how-to-non-interactively-provide-password-for-the-postgresql-interactive-terminal/

.. _permalink:
    /blog/2016/06/29/reStructuredTextNestedMarkup.html
