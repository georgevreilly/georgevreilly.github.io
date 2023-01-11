---
title: "Bash: Getting and Setting Default Values"
date: "2016-01-12"
permalink: "/blog/2016/01/12/BashGettingAndSettingDefaultValues.html"
tags: [bash, til]
---



Bash has some handy syntax for getting and setting default values.
Unfortunately, it's a collection of punctuation characters,
which makes it hard to Google when you can't quite remember the syntax.

Getting a default value using ``${var:-fallback}``:

.. code:: bash

    # set $LOGDIR to $1 if $1 has a value; otherwise set $LOGDIR to "/var/log"
    LOGDIR="${1:-/var/log}"

    # use $VERSION unless it's empty or unset; fall back to extracting someprog's version num
    build_version=${VERSION:-$(someprog --version | sed 's/[^0-9.]*\([0-9.]*\).*/\1/')}

The colon-dash construction is known as the
`dog's bollocks <https://en.wikipedia.org/wiki/Dog%27s_bollocks_(typography)>`_
in typography.

Setting a default value, using ``${var:=fallback}``:

.. code:: bash

    $ echo $HOME
    /Users/georgevreilly
    $ echo ${HOME:=/tmp}
    /Users/georgevreilly
    $ unset HOME
    $ echo ${HOME:=/tmp}
    /tmp
    $ echo $HOME
    /tmp
    $ cd; pwd
    /tmp

Note: ``:=`` uses the new value in two cases.
First, when the shell variable is not set;
second, when the variable is set but empty.

If you want to assign the variable only when it's previously unset, omit the colon,
``${var=fallback}``.

.. _permalink:
    /blog/2016/01/12/BashGettingAndSettingDefaultValues.html
