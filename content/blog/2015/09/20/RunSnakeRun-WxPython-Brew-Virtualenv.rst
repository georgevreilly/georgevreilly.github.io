---
title: "RunSnakeRun (wxPython) apps in a Brew Virtualenv"
date: "2015-09-20"
permalink: "/blog/2015/09/20/RunSnakeRun-WxPython-Brew-Virtualenv.html"
tags: [python, mac, til]
---



.. image:: https://www.vrplumber.com/programming/runsnakerun/screenshot-2.0.png
    :alt: RunSnakeRun logo
    :class: right-float

I'm doing some Python profiling
and I wanted to use the RunSnakeRun_ utility to view the profile data.
Unfortunately, that's not straightforward on Mac OS X if you use a virtualenv_,
and it's even less easy if you're using the Python
installed by the Homebrew_ (``brew``) package manager.

There are several problems:

* Installing wxPython_ on OS X 10.10.
  This is the cross-platform GUI API toolkit used by RunSnakeRun.
* Getting wxPython installed in a virtualenv
* Running wxPython apps in a virtualenv on the Mac.

Installing wxPython
-------------------

I downloaded ``wxPython3.0-osx-3.0.2.0-cocoa-py2.7.dmg``,
released in November 2014.

If you open the DMG and attempt to run the PKG,
you will likely get a misleading error message from OS X:

    “wxPython3.0-osx-cocoa-py2.7.pkg” is damaged and can’t be opened.
    You should eject the disk image.

Open the *System Preferences* app, click *Security & Privacy*, then *General*.
Click the *Lock* icon to make changes,
then change *Allow apps downloaded from* to *Anywhere*.
Now try running the wxPython PKG again to install wxPython.
Afterwards, you should reset *Allow apps downloaded from* to its previous value.

Installing and running wxPython in a virtualenv
-----------------------------------------------

As I learned from earlier work by `Mike Soulier`_ and `Robin Dunn`_,
there are two issues in running wxPython apps in a virtual environment.

First, you need the ``wx.pth`` `path configuration file`_ to be in your
virtualenv's ``site-packages`` directory.
The solution is to copy the installed ``wxredirect.pth``.

Second, the Python binary installed in the virtualenv is not a framework_ binary,
and so wxPython cannot access the display or create GUI objects.
The solution is to set ``PYTHONHOME`` to the virtualenv,
then use the framework binary to run the wxPython app.

The following has been tested with

* OS X 10.10.5
* Brew Python 2.7.10
* wxPython 3.0.2
* virtualenv 13.1.0

.. code-block:: bash

    #!/bin/bash -ex

    WXPYTHON_APP="runsnakerun/runsnake.py"
    PYVER=2.7

    if [ -z "$VIRTUAL_ENV" ] ; then
        echo "You must activate your virtualenv: set '$VIRTUAL_ENV'"
        exit 1
    fi

    SYSTEM_FRAMEWORK_PYTHON_ROOT="/Library/Frameworks/Python.framework/Versions/$PYVER"
    # OS X 10.10
    SYSTEM_FRAMEWORK_PYTHON_ROOT="/System$SYSTEM_FRAMEWORK_PYTHON_ROOT"

    PYSUBVER="$(python --version 2>&1 | cut -d ' ' -f2)"  # e.g., 2.7.10
    BREW_PYTHON_ROOT="$(brew --prefix)/Cellar/python/$PYSUBVER/Frameworks/Python.framework/Versions/$PYVER"

    PYTHON_BINARY="bin/python$PYVER"
    #FRAMEWORK_PYTHON="$SYSTEM_FRAMEWORK_PYTHON_ROOT/$PYTHON_BINARY"

    FRAMEWORK_PYTHON="$BREW_PYTHON_ROOT/$PYTHON_BINARY"

    VENV_SITE_PACKAGES="$VIRTUAL_ENV/lib/python$PYVER/site-packages"

    # Ensure wx.pth is set up in the virtualenv
    cp "/Library/Python/$PYVER/site-packages/wxredirect.pth" "$VENV_SITE_PACKAGES/wx.pth"

    # Use the Framework Python to run the app
    export PYTHONHOME=$VIRTUAL_ENV
    exec "$FRAMEWORK_PYTHON" "$VENV_SITE_PACKAGES/$WXPYTHON_APP" $*


Previous Work
-------------

The following is an attempt from last year at setting up wxPython in a virtualenv,
which no longer works.
It sets up a script called ``fwpy`` in the virtualenv,
which allows you to run a wxPython app with the framework Python.

.. code-block:: python

    #!/usr/bin/env python

    # Adapted from http://wiki.wxpython.org/wxPythonVirtualenvOnMac

    import os, sys
    import optparse
    from distutils.sysconfig import get_python_lib

    site_packages = get_python_lib()
    PYTHON_VERSION = sys.version[:3]  # e.g., "2.7"

    if os.getenv('VIRTUAL_ENV'):
        print >> sys.stderr, "ERROR: You must *not* run this inside of a virtualenv. Run 'deactivate' first."
        sys.exit(1)

    parser = optparse.OptionParser(
        description="virtualenv-aware wrapper for wxPython.",
        usage="usage: %prog virtualenv-name-or-path")
    (options, args) = parser.parse_args()

    venv = args and args[0]

    def valid_virtualenv_dir(venv):
        return venv and os.path.exists(os.path.join(venv, "bin", "activate"))

    if not valid_virtualenv_dir(venv):
        # Using virtualenvwrapper?
        if os.getenv("WORKON_HOME"):
            venv = os.path.join(os.getenv("WORKON_HOME"), venv)

    if not valid_virtualenv_dir(venv):
        print "Can't find virtualenv", venv
        sys.exit(1)

    framework_python = """\
    #!/bin/bash
    # Invoke Framework Python inside of a virtualenv; e.g., for wxPython

    [ -z "$VIRTUAL_ENV" ] && echo "Not running inside of a virtualenv" && exit 1

    PYTHONHOME="$VIRTUAL_ENV" exec "%s" "$@"
    """ % sys.executable

    wx_pth = None

    for wx_pth_file in [
            os.path.join(site_packages, 'wx.pth'),
            '/Library/Python/2.7/site-packages/wxredirect.pth'
        ]:
        if os.path.exists(wx_pth_file):
            with open(wx_pth_file) as f:
                wx_pth = f.read().splitlines()[0]
                break

    # This is the value of wx.pth for the system python
    abs_wx_pth = os.path.join(site_packages, wx_pth)

    fwpy = os.path.join(venv, "bin", "fwpy")
    with open(fwpy, "w") as f:
        f.write(framework_python)
    os.chmod(fwpy, 0755)
    print "Wrote", fwpy

    # TODO: copy wx.pth
    target_wx_pth = os.path.join(venv, "lib", "python"+PYTHON_VERSION, "site-packages", "wx.pth")
    with open(target_wx_pth, "w") as f:
        f.write(abs_wx_pth)
    print "Wrote", target_wx_pth


.. _RunSnakeRun:
    http://www.vrplumber.com/programming/runsnakerun/
.. _virtualenv:
    https://virtualenv.pypa.io/en/latest/
.. _Homebrew:
    http://brew.sh/
.. _wxPython:
    http://www.wxpython.org/ 
.. _Mike Soulier:
    http://www.but-i-digress.ca/getting-runsnakerun-osx.html
.. _Robin Dunn:
    http://wiki.wxpython.org/wxPythonVirtualenvOnMac
.. _path configuration file:
    https://docs.python.org/2/library/site.html
.. _framework:
    https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WhatAreFrameworks.html

.. _permalink:
    /blog/2015/09/20/RunSnakeRun-WxPython-Brew-Virtualenv.html
