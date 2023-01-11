---
title: "For Want of a Nail"
date: "2015-01-03"
permalink: "/blog/2015/01/03/ForWantOfANail.html"
tags: [tech]
---



..

    | For want of a nail the shoe was lost.
    | For want of a shoe the horse was lost.
    | For want of a horse the rider was lost.
    | For want of a rider the message was lost.
    | For want of a message the battle was lost.
    | For want of a battle the kingdom was lost.
    | And all for the want of a horseshoe nail.
    |       — `proverb <http://en.wikipedia.org/wiki/For_Want_of_a_Nail>`_

I want to step down as the webmaster of the `Northwest C++ Users' Group`_
after serving for four years.
The `NWCPP website is built  <http://nwcpp.org/2013-website-refresh.html>`_
with the Pelican_ static site generator.
I don't know who will succeed me as webmaster,
but it's likely that they'll be a Windows user.
Pelican runs fine on Mac and Linux,
but Windows support has never been great in Pelican.

I've been trying to make sure that Pelican can generate the NWCPP website on Windows.
That simple goal cascaded into a series of problems.

First, I had to update the `website README`_,
to clarify the instructions about virtualenvs
and custom installation of various packages.

Then, I had to update my stale `ghp-import pull request`_, which adds Windows support.
Ghp-import is used to publish the website's content on the ``gh-pages`` branch.

After that, I tried to get the website to build on Windows.
It did at one point, I think, about a year ago.
At least, I removed the `gratuitious Unixisms`_ from the Fabfile back in April,
though I only got around to submitting a pull request for it a few weeks ago.

Getting the website to build required several `Windows fixes for Pelican`_.
I had to fix the handling of internal links,
which use the syntax ``{filename}path/to/file``.
Windows backslash path separators worked their way in to various paths,
which broke some file generation.
I thought it was working at that point,
so I built the website and published it with ghp-import,
only to find that http://nwcpp.org was no longer serving content.
I instantly realized that the `CNAME file for GitHub Pages`_ was missing
(having painfully debugged that issue a number of months back).
That meant that I had to fix some other path handling in Pelican.

At that point, I tried to get the Pelican unit tests to pass,
intending to write some new ones for the changes I had made.
When I tried to ``pip install -r dev_requirements.txt``,
I ran into problems trying to install lxml_.
I quickly found `Christoph Gohlke's Windows binary`_,
but then I had a series of problems with `Python Wheels`_
and updating out-of-date installations of Pip and Setuptools and Virtualenv.

The unit tests didn't pass—of course.
The first big problem that I ran into
was that a number of tests generate a tree of content
and use `git diff`_ to compare the output tree
with a reference copy of good output.
After I fixed the invocation of ``git diff``,
I got a ton of errors, most of which were more path separator issues,
Still, I was still getting a lot of errors about
"LF will be replaced by CRLF ... The file will have its original line endings".

I couldn't figure out how to invoke ``git diff`` to ignore CRLF issues,
so I spent a couple of hours trying to compare directory trees
with `dircmp`_ and `difflib`_.
That more or less worked, but I was having difficulty with
both ignoring whitespace differences, yet rendering a legible diff.
Eventually I realized that I should just use ``git diff`` again
but filter the errors to remove the CRLF warnings.
Hey presto, that worked!

While writing this post, I realized that the mysterious accented filenames
that I had been seeing with ``git status`` in my Mac's working copy of Pelican
(``pelican/tests/output/custom_locale/posts/2010/décembre/`` and ``.../201*/février/``)
could be stopped by `setting core.precomposeunicode`_.

All for the want of a nail...

**Update**: `Pull Request for Windows fixes`_.

Today's round of fixes led me through
fixing the remaining tests;
providing a `six-based`_ answer to `converting a filepath to a file URL`_;
more updates to the `website README`_;
fixing some warnings in the NWCPP website;
and finding an `issue in Pip`_ with unzipping paths that are not ASCII.


.. _Northwest C++ Users' Group:
    http://nwcpp.org/
.. _Pelican:
    http://blog.getpelican.com/
.. _website README:
    https://github.com/nwcpp/pelican-site/blob/master/README.rst
.. _ghp-import pull request:
    https://github.com/davisp/ghp-import/pull/25
.. _gratuitious Unixisms:
    https://github.com/getpelican/pelican/pull/1550
.. _Windows fixes for Pelican:
    https://github.com/georgevreilly/pelican/tree/win-paths
.. _CNAME file for GitHub Pages:
    https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/
.. _lxml:
    http://lxml.de/
.. _Christoph Gohlke's Windows binary:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
.. _Python Wheels:
    http://wheel.readthedocs.org/en/latest/
.. _git diff:
    http://git-scm.com/docs/git-diff
.. _dircmp:
    https://docs.python.org/2/library/filecmp.html#filecmp.dircmp
.. _difflib:
    https://docs.python.org/2/library/difflib.html
.. _setting core.precomposeunicode:
.. _Unicode filenames in Git:
    http://makandracards.com/makandra/17827-git-mac-working-with-unicode-filenames
.. _Pull Request for Windows fixes:
    https://github.com/getpelican/pelican/pull/1581
.. _six-based:
    https://pythonhosted.org/six/
.. _converting a filepath to a file URL:
    http://stackoverflow.com/a/14298190/6364
.. _issue in Pip:
    https://github.com/pypa/pip/issues/1140

.. _permalink:
    /blog/2015/01/03/ForWantOfANail.html
