---
title: "Bash: echo success of previous command"
date: "2017-01-19"
permalink: "/blog/2017/01/19/BashEchoSuccessOfPreviousCommand.html"
tags: [bash, til]
---



C-like languages have a ternary operator,
``cond ? true_result : false_result``.
Python has ``true_result if cond else false_result``.
Bash doesn't have a ternary operator, but there are `various workarounds`__.

I wanted to print ``succeeded`` or ``failed``
based on the exit code of the previous command
in a shell script.
In Unix, all programs exit with an integer status code.
Successful programs exit with ``0``;
all other values, positive or negative, indicate failure__.
In Bash, the `status code`__ of the previous program is held in ``$?``.

.. code-block:: bash

    some/command or-other fer example

    STATUS="$([ "$?" == 0 ] && echo 'succeeded' || echo 'failed')"
    echo "Results: $STATUS"

There are `other ways`__ to handle this.

__ http://stackoverflow.com/a/3953712/6364
__ http://www-numi.fnal.gov/offline_software/srt_public_context/WebDocs/Errors/unix_system_errors.html
__ http://tldp.org/LDP/abs/html/exit-status.html
__ http://stackoverflow.com/a/3953712/6364

.. _permalink:
    /blog/2017/01/19/BashEchoSuccessOfPreviousCommand.html
