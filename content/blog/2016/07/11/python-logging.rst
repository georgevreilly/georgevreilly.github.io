---
title: "Logging in Python: Don't use new-fangled format"
date: "2016-07-11"
permalink: "/blog/2016/07/11/LoggingInPythonDontUseNew-FangledFormat.html"
tags: [python, til]
---



Python 2.6 introduced the `format method`__ to strings.
In general, ``format`` is now the preferred way to build strings
instead of the old ``%`` formatting operator.

__ https://pyformat.info/

One exception is with the ``logging`` module,
where the best practice is to use ``%s`` and ``%d``.
Why?
First, ``%s`` is the idiomatic way to use ``logging``,
which was built years before ``format`` was introduced.
Second, if there's a literal ``%`` in the interpolated values,
``logging`` will be unhappy,
since there won't be corresponding arguments in the call.
It won't fall over, since
“The logging package is designed to swallow exceptions which occur while logging in production.
This is so that errors which occur while handling logging events
- such as logging misconfiguration, network or other similar errors -
do not cause the application using logging to terminate prematurely.”

In other systems, an `uncontrolled format string`__ can lead to serious vulnerabilities.

__  https://en.wikipedia.org/wiki/Uncontrolled_format_string

TL;DR, write:

.. code:: python

    logging.info("Report: Processing %d annotations for id %s",
                len(annotations), report_id)

not:

.. code:: python

    logging.info("Report: Processing {} annotations for id {}".format(
                len(annotations), report_id))

.. _permalink:
    /blog/2016/07/11/LoggingInPythonDontUseNew-FangledFormat.html
