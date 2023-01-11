---
title: "Installing Python 2.7.11 on Ubuntu"
date: "2016-01-16"
permalink: "/blog/2016/01/16/InstallingPython2_7_11onUbuntu.html"
tags: [python, linux, til]
---



We deploy on Ubuntu 14.04, the most recent Long Term Support release.
It comes with Python 2.7.6,
but we need Python 2.7.9+ to get the some important SSL fixes
and work with a recent version of the Requests_ library.

Felix Krull maintains a Personal Package Archive for `Python 2.7 Updates`_,
which makes it straightforward to upgrade to Python 2.7.11
on supported versions of Ubuntu.

.. code:: bash

    sudo apt-add-repository ppa:fkrull/deadsnakes-python2.7
    sudo apt-get update
    sudo apt-get install python2.7 python2.7-dev

Be sure not to use Felix Krull's `other Python PPA`_ by mistake.
I did that on a colleague's machine yesterday.
In our attempts to figure out why we still had Python 2.7.6,
we managed to mess up the machine sufficiently
that we had to reinstall Ubuntu.


.. _Requests:
    http://docs.python-requests.org/en/latest/
.. _Python 2.7 Updates:
    https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes-python2.7
.. _other Python PPA:
    https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes

.. _permalink:
    /blog/2016/01/16/InstallingPython2_7_11onUbuntu.html
