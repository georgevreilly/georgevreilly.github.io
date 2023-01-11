---
title: "io.StringIO and UnicodeCSV DictWriter"
date: "2016-04-13"
permalink: "/blog/2016/04/13/io.StringIOAndUnicodeCSV_DictWriter.html"
tags: [python, til]
---



I like to use `io.StringIO`_ rather than the older `cStringIO.StringIO`_,
as it's Python 3–ready
``io.StringIO`` is also a `context manager`_:
if you use it in a ``with`` statement,
the string buffer is automatically ``close``\ d as you go out of scope.

I tried using ``io.StringIO`` with unicodecsv_,
as I wanted to capture the CSV output into a string buffer
for use with unit tests.
``unicodecsv`` is a drop-in replacement for Python's built-in ``csv`` module,
which supports Unicode strings.

.. code:: python

    with io.StringIO() as csv_file:
        write_csv_rows(csv_file)
        lines = csv_file.getvalue().split('\r\n')
        return lines[:-1]  # drop empty line after trailing \r\n

It failed horribly with
``TypeError: unicode argument expected, got 'str'``.

I managed to fix it by using ``cStringIO.StringIO`` and `contextlib.closing`_

.. code:: python

    with contextlib.closing(cStringIO.StringIO()) as csv_file:
        ...

Writing this post, however,
I realized how to fix it properly.
Use `io.BytesIO`_:

.. code:: python

    with io.BytesIO() as csv_file:
        ...

I now realize that ``io.StringIO`` is expecting a Unicode string,
while the classic ``cStringIO.StringIO`` is expecting a byte string.
UnicodeCSV implicitly takes care of the character encoding,
so we have a byte stream that's being written.

There are examples with the old ``StringIO`` in the ``unicodecsv`` code,
but somehow I missed that ``io.BytesIO`` is used in ``unicodecsv``'s GitHub README.

cStringIO: “Unlike the StringIO module, this module is not able to accept Unicode strings
that cannot be encoded as plain ASCII strings.”

UnicodeCSV: “Note that unicodecsv expects a bytestream, not unicode.”

io: “Since this module has been designed primarily for Python 3.x,
you have to be aware that all uses of “bytes” in this document
refer to the ``str`` type (of which bytes is an alias),
and all uses of “text” refer to the ``unicode`` type.
Furthermore, those two types are not interchangeable in the io APIs.”


.. _io.StringIO:
    https://docs.python.org/2/library/io.html#io.StringIO
.. _cStringIO.StringIO:
    https://docs.python.org/2/library/stringio.html#cStringIO.StringIO
.. _context manager:
    https://docs.python.org/2/reference/datamodel.html#context-managers
.. _unicodecsv:
    https://github.com/jdunck/python-unicodecsv
.. _contextlib.closing:
    https://docs.python.org/2/library/contextlib.html#contextlib.closing
.. _io.BytesIO:
    https://docs.python.org/2/library/io.html#io.BytesIO

.. _permalink:
    /blog/2016/04/13/io.StringIOAndUnicodeCSV_DictWriter.html
