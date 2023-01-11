---
title: "Python: Joining URLs with posixpath.join"
date: "2016-07-12"
permalink: "/blog/2016/07/12/PythonJoiningUrlsWithPosixpathJoin.html"
tags: [python, til]
---



On Mac/Linux, `os.path.join`__ is an alias for ``posixpath.join``,
which always joins path segments with ``/``.
On Windows, ``os.path.join`` is an alias for ``ntpath.join``,
which always uses ``\``.
When dealing with URLs, we always want forward slashes,
regardless of platform, so ``posixpath.join`` should be used to build URL paths.

__ https://docs.python.org/2/library/os.path.html#os.path.join

Running:

.. code:: python

    from __future__ import print_function

    from six.moves.urllib_parse import urljoin as abs_urljoin
    from posixpath import join as path_urljoin

    def urljoin(site, path):
        return abs_urljoin(site, path)

    def test_join(site, path):
        result = urljoin(site, path)
        print("'{0}' + '{1}'\n\t-> '{2}'".format(site, path, result))
        return result

    local_path = path_urljoin('2016', '07', '12', 'release', 'index.html')

    test_join('https://www.example.com', 'foo/bar/quux.js')
    test_join('https://www.example.com', local_path)
    test_join('https://www.example.com/', local_path)
    test_join('https://www.example.com/prefix', local_path)

Yields::

    'https://www.example.com' + 'foo/bar/quux.js'
            -> 'https://www.example.com/foo/bar/quux.js'
    'https://www.example.com' + '2016/07/12/release/index.html'
            -> 'https://www.example.com/2016/07/12/release/index.html'
    'https://www.example.com/' + '2016/07/12/release/index.html'
            -> 'https://www.example.com/2016/07/12/release/index.html'
    'https://www.example.com/pre/fix' + '2016/07/12/release/index.html'
            -> 'https://www.example.com/2016/07/12/release/index.html'

The last one is a problem,
as the path after the hostname, ``/pre/fix``, is lost.

We can fix it using `urlparse`__ to separate that path from the hostname:

__  https://docs.python.org/2/library/urlparse.html#urlparse.urlparse

.. code:: python

    from six.moves.urllib_parse import urljoin as abs_urljoin, urlparse

    def urljoin(site, path):
        return abs_urljoin(site, path_urljoin(urlparse(site).path, path))

which yields::

    'https://www.example.com' + 'foo/bar/quux.js'
            -> 'https://www.example.com/foo/bar/quux.js'
    'https://www.example.com' + '2016/07/12/release/index.html'
            -> 'https://www.example.com/2016/07/12/release/index.html'
    'https://www.example.com/' + '2016/07/12/release/index.html'
            -> 'https://www.example.com/2016/07/12/release/index.html'
    'https://www.example.com/pre/fix' + '2016/07/12/release/index.html'
            -> 'https://www.example.com/pre/fix/2016/07/12/release/index.html'

Note that if the ``path`` argument to my ``urljoin`` function is absolute,
any path suffix to ``site`` is discarded::

    'https://www.example.com/pre/fix' + '/abs/path'
            -> 'https://www.example.com/abs/path'

That in turn can be fixed by using ``str.split('/')``
and discarding any empty segments.

.. code:: python

    def urljoin(site, path):
        if isinstance(path, six.string_types):
            segments = [s for s in path.split('/') if s]
        else:
            segments = path  # assume list or tuple
        return abs_urljoin(site, path_urljoin(urlparse(site).path, *segments))

Thus::

    'https://www.example.com/pre/fix' + '/abs/path'
        -> 'https://www.example.com/pre/fix/abs/path'
    'https://www.example.com/pre/fix' + '('one', 'two', 'three')'
        -> 'https://www.example.com/pre/fix/one/two/three'

.. _permalink:
    /blog/2016/07/12/PythonJoiningUrlsWithPosixpathJoin.html
