---
title: "Quoting in Bash"
date: "2016-03-17"
permalink: "/blog/2016/03/17/QuotingInBash.html"
tags: [bash, til]
---



Various Bash guides recommend putting quotes around just about everything.
I had a script that contained this line:

.. code:: bash

    sudo apt-get install --yes $(cat "$BUILD/install_on_aws_ubuntu.txt")

While refactoring, I put another set of quotes around the ``$(cat ...)``
out of an abundance of caution:

.. code:: bash

    sudo apt-get install --yes "$(cat "$BUILD/install_on_aws_ubuntu.txt")"

Several other changes later, I couldn't figure out why my script had stopped working.

Here's what happened:

.. code:: bash

    $ cat $HOME/tmp/demo.txt
    foo
    bar
    quux

    $ echo $(cat "$HOME/tmp/demo.txt")
    foo bar quux

    $ echo "$(cat $HOME/tmp/demo.txt)"
    foo
    bar
    quux

The new outer quotes retained the newlines;
the original replaced newlines with spaces.

The `Bash FAQ`_ has more: specifically `Command Substition`_ and `Word Splitting`_.

.. _Bash FAQ:
    http://mywiki.wooledge.org/BashFAQ
.. _Command Substition:
    http://mywiki.wooledge.org/CommandSubstitution
.. _Word Splitting:
    http://mywiki.wooledge.org/WordSplitting

.. _permalink:
    /blog/2016/03/17/QuotingInBash.html
