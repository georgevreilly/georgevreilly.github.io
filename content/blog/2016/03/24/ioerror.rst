---
title: "Raising IOError for 'file not found'"
date: "2016-03-24"
permalink: "/blog/2016/03/24/RaisingIOErrorForFileNotFound.html"
tags: [python, til]
---



I wanted to raise Python's IOError_ for a file-not-found condition,
but it wasn't obvious what the parameters to the exception should be.

.. code:: python

    from errno import ENOENT

    if not os.path.isfile(source_file):
        raise IOError(ENOENT, 'Not a file', source_file)
    with open(source_file) as fp:
        return fp.read()

``IOError`` can be instantiated with 1, 2, or 3 arguments:

``IOError(errno, strerror, filename)``
   These arguments are available
   on the ``errno``, ``strerror``, and ``filename`` attributes of the exception object,
   respectively, in both Python 2 and 3.
   The ``args`` attribute contains the verbatim constructor arguments as a tuple.

``IOError(errno, strerror)``
   These are available on the ``errno`` and ``strerror`` attributes of the exception,
   respectively, in both Python 2 and 3,
   while the ``filename`` attribute is ``None``.

``IOError(errmsg)``
   In Python 2, ``errmsg`` is available
   on the deprecated ``message`` attribute of the exception.
   There is no ``message`` attribute on the exception object in Python 3;
   you must obtain ``errmsg`` from the ``args`` attribute.
   The ``errno``, ``strerror``, and ``filename`` attributes are all ``None``.

I used ``errno.ENOENT`` above.
You can obtain all the ``errno`` error codes and descriptions with
``[(k,v, os.strerror(k)) for k,v in os.errno.errorcode.items()]``.

You may object that opening a file only after checking for its existence
is fragile because there's a small window between checking and opening
where the file could be removed by another process.
You'd be right.
In such a case, ``open(filename)`` will raise
``IOError(ENOENT, "No such file or directory", filename)``.
Still, there are other cases where it's useful to raise the 2- or 3-argument
form of ``IOError``.


.. _IOError:
    https://docs.python.org/2/library/exceptions.html#exceptions.IOError

.. _permalink:
    /blog/2016/03/24/RaisingIOErrorForFileNotFound.html
