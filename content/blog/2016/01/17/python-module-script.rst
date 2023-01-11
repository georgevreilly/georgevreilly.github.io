---
title: "Relative Imports in a Python Script"
date: "2016-01-17"
permalink: "/blog/2016/01/17/RelativeImportsInAPythonScript.html"
tags: [python, til]
---



Have you ever attempted a `relative import`_ in a Python script?

.. code:: bash

    $ ./foo/bar/script.py some parameters
    Traceback (most recent call last):
      File "foo/bar/script.py", line 16, in <module>
        from .quux import find_vcs
    ValueError: Attempted relative import in non-package

I prefer to use `absolute imports`_ to minimize ambiguity and confusion,
and most of my Python modules begin with:

.. code:: python

    from __future__ import absolute_import, unicode_literals, print_function

(Using `unicode_literals`_ and `print_function`_ makes porting to Python 3 easier.)

I recently read the accepted answer to `Python relative imports for the billionth time`_
and the solution to the above ``ValueError`` occurred to me:
Use ``python -m package`` instead:

.. code:: bash

    $ python -m foo.bar.script some parameters

(Assuming that package ``foo`` exists.)


.. _relative import:
.. _absolute imports:
    https://www.python.org/dev/peps/pep-0328/
.. _unicode_literals:
    https://www.python.org/dev/peps/pep-3112/
.. _print_function:
    https://www.python.org/dev/peps/pep-3105/
.. _Python relative imports for the billionth time:
    http://stackoverflow.com/questions/14132789/python-relative-imports-for-the-billionth-time

.. _permalink:
    /blog/2016/01/17/RelativeImportsInAPythonScript.html
