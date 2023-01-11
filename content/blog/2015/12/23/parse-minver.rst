---
title: "Checking minimum version numbers in Bash"
date: "2015-12-23"
permalink: "/blog/2015/12/23/ParseMinVerBash.html"
tags: [bash, python, til]
---



.. image:: https://cube-drone.com/media/optimized/161.png
    :alt: Version Sacrifice
    :target: http://cube-drone.com/comics/c/version-sacrifice

I worked on a Bash script today that sets up various prerequisites for our build.
We need a recent version of Docker
but our Bamboo_ build agents are running on Ubuntu 14.04,
which has a very old version of Docker.
The script upgrades Docker when it's first run.
The script may be run more than once during the lifetime of the agent,
so the second and subsequent calls should not upgrade Docker.

Basically, I wanted

.. code:: bash

    if $DOCKER_VERSION < 1.9; then upgrade_docker; fi

Unfortunately, it's not that easy in Bash.
Here's what I came up with.

.. code:: bash

    install_latest_docker() {
        if docker --version | python -c "min=[1, 9]; import sys; ↩  
    v=[int(x) for x in sys.stdin.read().split()[2].split(',')[0].split('.')]; ↩  
    sys.exit(v < min)";
        then
            echo "Docker up to date"
            return
        fi
        # Install Docker ...

Let's unpack that ugly ``if`` one-liner.
Note: the ``↩`` denotes linebreaks introduced for presentation purposes; it's all one line.

.. code:: bash

    $ docker --version
    Docker version 1.9.1, build a34a1d5

.. code:: python

    $ ipython

    In [1]: dv = 'Docker version 1.9.1, build a34a1d5'

    In [2]: dv.split()
    Out[2]: ['Docker', 'version', '1.9.1,', 'build', 'a34a1d5']

    In [3]: dv.split()[2]
    Out[3]: '1.9.1,'

    In [4]: # Remove trailing comma

    In [5]: dv.split()[2].split(',')
    Out[5]: ['1.9.1', '']

    In [6]: dv.split()[2].split(',')[0]
    Out[6]: '1.9.1'

    In [7]: # Break apart at dots

    In [8]: dv.split()[2].split(',')[0].split('.')
    Out[8]: ['1', '9', '1']

    # String comparisons aren't good enough for version numbers
    In [9]: ['1', '10'] < ['1', '9']
    Out[9]: True

    # We have to convert each token to an integer, then lexicographically compare
    In [10]: [1, 10] < [1, 9]
    Out[10]: False

    # Convert to list of integers
    In [11]: version = [int(x) for x in dv.split()[2].split(',')[0].split('.')]

    In [12]: min = [1, 9]

    In [13]: version, min
    Out[13]: ([1, 9, 1], [1, 9])

    In [14]: version < min
    Out[14]: False

    In [15]: [1, 4, 2] < min
    Out[15]: True

    In [16]: int(version < min)
    Out[16]: 0

    In [17]: int([1, 4, 2] < min)
    Out[17]: 1

The ugly triple split inside the list comprehension
produces a list of integers,
which can be compared lexicographically against
``min``, another list.
``sys.exit`` is called with ``1`` when Docker's version is less than ``min``.

When ``$?`` is non-zero in Bash, then ``if some_command`` fails
and the ``else`` clause (none here) is executed.

I came across `Python Oneliner`_, while debugging my script.
I might use Oneliner in other circumstances.

.. _Bamboo:
    https://www.atlassian.com/software/bamboo/
.. _Python Oneliner:
    http://python-oneliner.readthedocs.org/en/latest/

.. _permalink:
    /blog/2015/12/23/ParseMinVerBash.html
