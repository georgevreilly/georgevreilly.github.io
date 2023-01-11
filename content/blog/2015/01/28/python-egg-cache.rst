---
title: "Python Egg Cache"
date: "2015-01-28"
permalink: "/blog/2015/01/28/PythonEggCache.html"
tags: [python, til]
---



Every so often, one of our Bamboo_ builds would break thus::

    pkg_resources.ExtractionError: Can't extract file(s) to egg cache

    The following error occurred while trying to extract file(s) to the Python egg
    cache:

      [Errno 17] File exists: '/home/bamboo/.python-eggs'

    The Python egg cache directory is currently set to:

      /home/bamboo/.python-eggs

    Perhaps your account does not have write access to this directory?  You can
    change the cache directory by setting the PYTHON_EGG_CACHE environment
    variable to point to an accessible directory.

This occurred while trying to make use of PyCrypto_.

After a little research_, I decided that instead of installing PyCrypto
as a zipped egg (as it does by default) into the build's virtual environment,
to instead force it to unzip itself: ``easy_install --always-unzip pycrypto``.
This seems to have fixed the problem,
as `pkg_resources`_ no longer needs to unpack anything.
Pillow_ was also in the Egg Cache and probably needs similar treatment.

.. _Bamboo:
    https://www.atlassian.com/software/bamboo
.. _research:
    http://stackoverflow.com/questions/2192323/what-is-the-python-egg-cache-python-egg-cache
.. _PyCrypto:
    http://pycrypto.org
.. _pkg_resources:
    https://pythonhosted.org/setuptools/pkg_resources.html
.. _Pillow:
    https://pillow.readthedocs.org/

.. _permalink:
    /blog/2015/01/28/PythonEggCache.html
