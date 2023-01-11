---
title: "Doctests, Unicode Literals, and Python 2/3 Compatibility"
date: "2016-04-05"
permalink: "/blog/2016/04/05/DoctestsUnicodeLiteralsPython2_3Compat.html"
tags: [python, til]
---



I rarely use `doctests`_, but I do have `some code`_ that uses them.

Although I still mostly write Python 2,
I usually import several features of Python 3:

.. code:: python

    from __future__ import unicode_literals, print_function, absolute_import

Unfortunately `unicode_literals`_ doesn't play well with doctests.

The following code will pass with ``python2 -m doctest demo.py``,
but not with ``python3``:

.. code:: python

    from __future__ import unicode_literals, print_function, absolute_import

    def upper(s):
        """
        Convert `s` to upper case.

        >>> upper('Hello!')
        u'HELLO!'
        """
        return s.upper()

Python 3 complains::

    Failed example:
        upper('Hello!')
    Expected:
        u'HELLO!'
    Got:
        'HELLO!'

The problem is that Python 2's ``repr`` for a Unicode string
prefixes the string with ``u``,
while Python 3's repr does not
(all strings are Unicode).

The test can be made to pass by removing ``unicode_literals``
from the ``from __future__ import``,
but this also removes the benefit of implicitly forcing all string literals to be Unicode.

Another workaround is to use six_ thus:

.. code:: python

    from __future__ import unicode_literals, print_function, absolute_import

    import six

    def upper(s):
        """
        Convert `s` to upper case.

        >>> upper('Hello!') == six.text_type(u'HELLO!')
        True
        """
        return s.upper()

This works, but is less clear.
If the assertion fails,
complaining about ``True`` instead of ``HELLO!`` is far less clear.

Lennart Regebro has a good discussion of other `doctest migration problems`_.
If you're willing to use a more sophisticated method of running doctests,
you can try a `doctest output checker`_ or a `nose plugin`_.

.. _doctests:
    https://pymotw.com/2/doctest/
.. _some code:
    https://code.activestate.com/recipes/578031-sorting-a-dicts-items-and-keys/
.. _unicode_literals:
    http://python-future.org/unicode_literals.html
.. _six:
    https://pythonhosted.org/six/
.. _doctest migration problems:
    http://python3porting.com/problems.html#running-doctests
.. _doctest output checker:
    https://dirkjan.ochtman.nl/writing/2014/07/06/single-source-python-23-doctests.html
.. _nose plugin:
    https://github.com/gnublade/doctest-ignore-unicode

.. _permalink:
    /blog/2016/04/05/DoctestsUnicodeLiteralsPython2_3Compat.html
