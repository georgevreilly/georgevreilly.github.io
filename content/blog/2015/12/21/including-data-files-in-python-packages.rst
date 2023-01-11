---
title: "Including Data Files in Python Packages"
date: "2015-12-21"
permalink: "/blog/2015/12/21/IncludingDataFilesInPythonPackages.html"
tags: [python, metabrite, til]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

I spent some time today struggling with `setuptools`_,
trying to make a Python source package
not only include a data file,
but also *install* that file.


Building the installer
----------------------

Consider the following source tree layout::

    ├── MANIFEST.in
    ├── README.md
    ├── my_stuff/
    │   ├── bar.py
    │   ├── foo.py
    │   ├── __init__.py
    │   └── quux.py
    ├── models/
    │   └── long_ugly_name_20151221.json
    └── setup.py*

I wanted to create a Python source distribution, ``some_package-N.N.N.tar.gz``,
which contains the code in the ``my_stuff`` directory,
as well as ``models/long_ugly_name_20151221.json``,
using ``python setup.py sdist``.

It's not that hard to get ``models/long_ugly_name_20151221.json``
included in the tarball.
Add an entry in ``MANIFEST.in``::

    include models/*.json

Then be sure to set ``include_package_data=True``
in the call to ``setup()``:

.. code:: python

    from setuptools import setup, find_packages

    setup(
        packages=find_packages(),
        include_package_data=True,
        # ...
    )

Or, if the JSON file is under source control,
you can add ``package_data={'models': ['models/*.json']}``
to the ``setup()`` call.

However, neither is sufficient to have the JSON file *installed*
when you run ``pip install some_package-N.N.N.tar.gz``.
The trick is to convince setuptools that ``models`` is actually a *module*
by placing an empty ``__init__.py`` in the ``models`` source directory::

    models/
    ├── __init__.py
    └── long_ugly_name_20151221.json

More at `setuptools: Including Data Files`_.

Using the JSON file at runtime
------------------------------

As you might guess, the rest of the package doesn't actually know
the actual name of the JSON file.
So how do we discover the name at runtime so that we can load it?
We use `pkg_resources`_:

.. code:: python

    import json
    import pkg_resources

    json_files = [f for f in pkg_resources.resource_listdir('models', '')
                  if f.endswith('.json')]
    model = json.load(pkg_resources.resource_stream('models', json_files[0]))


package_data versus data_files
------------------------------

Note: there are two similarly named arguments to ``setup()`` with distinct semantics,
``package_data`` and ``data_files``.

Use ``package_data`` to install files into the package;
use ``data_files`` to `place files outside the package`_.

This fragment may help to set ``data_files``:

.. code:: python

    data_files=[(d, [os.path.join(d, f) for f in files])
                for d, folders, files in os.walk(datadir)]

.. _MetaBrite Dev Blog:
    https://www.metabrite.com/devblog/posts/including-data-files-in-python-packages/
.. _setuptools:
    https://setuptools.readthedocs.io/en/latest/
.. _setuptools\: Including Data Files:
    https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
.. _pkg_resources:
    https://setuptools.readthedocs.io/en/latest/pkg_resources.html
.. _place files outside the package:
    https://packaging.python.org/guides/distributing-packages-using-setuptools/#data-files

.. _permalink:
    /blog/2015/12/21/IncludingDataFilesInPythonPackages.html
