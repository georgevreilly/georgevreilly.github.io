---
title: "Patching a Python Wheel"
# date: "2023-08-10"
permalink: "/blog/2023/08/10/PatchingAPythonWheel.html"
tags: [python]
---

Recently, I had to create a new `Python wheel`_ for PyTorch_.
There is a `cyclic dependency`_ between PyTorch 2.0.1 and Triton 2.0.0.
Pip_ is okay with a cyclic dependency.
Bazel_, however, `does not handle`_ cyclic dependencies between packages.

I spent a few days trying to build the PyTorch wheel from source.
It was a *nightmare!*
I ran out of disk space on the root partition on my EC2 devbox
trying to install system packages,
so I had to bring up a custom instance.
Then I ran out of space on the main partition,
trying to compile,
so I had to bring up another custom instance.
Then I realized I had installed CUDA 12.1
and couldn't install CUDA 11.8 over it,
so yet another instance.
Then a long list of other problems.
I was eventually able to get ``python setup.py develop`` to execute,
but it took three hours!
And I had little confidence that I was building the same thing
that was in the official wheels.

Then I had a brainwave:
what if I patch_ the official wheel and simply remove the requirement on Triton?
All the officially built code will remain untouched.
That worked!

This post is adapted from my `writeup on the issue`_.

What is a Wheel?
----------------

A Python wheel_ is a ready-to-install Python package
that requires no compilation at installation time.
Unlike older formats such as source distributions or eggs,
``setup.py`` is not run during installation from a wheel.
The older formats conflated build and install
and required arbitrary code to run.

A wheel is a `Zip archive`_ with a specially formatted filename
and a ``.whl`` extension.
The wheel contains a ``dist-info`` metadata directory
and the installable payload.
A wheel is either pure Python,
which can install on any platform,
or a platform (binary) wheel,
which usually contains compiled Python extension code.

Java JARs, Android APKs, Mozilla XPIs, and many other file types
are also structured Zip archives.

Manual Patching
---------------

The wheel file's contents_ include the
``{distribution}-{version}.dist-info/`` directory,
which contains metadata about the wheel.

In the case of PyTorch 2.0.1,
I had ``torch-2.0.1-cp38-cp38-manylinux1_x86_64.whl``,
a Linux ``x86_64`` wheel for Python 3.8.

I used ``unzip`` to extract the wheel's contents into a directory, ``torch201.2``.
(The ``.2`` denoted my second attempt.)
In the ``torch201.2`` directory was the entire content of the wheel,
including the ``torch-2.0.1.dist-info/`` subdirectory.

.. code:: bash

    unzip -d torch201.2 torch-2.0.1-cp38-cp38-manylinux1_x86_64.whl
    cd torch201.2

    # Rename the `dist-info` directory to include '+stripe.2' as a suffix for `2.0.1`
    mv torch-2.0.1{,+stripe.2}.dist-info/
    cd torch-2.0.1+stripe.2.dist-info/


Normally, when we build wheels for forked version of Python packages at Stripe,
we append ``+stripe.{major}.{commits}.{revision}`` to the version number.
Both ``commits`` and ``revision`` come from
the output of ``git describe --tags HEAD``,
which `looks like`_ ``{tag}-{commits}-g{revision}``;
``major`` is currently hardcoded to ``1``.
This suffix helps distinguish a forked wheel's version
from the upstream version number.

Since I wasn't forking, I used a simplified scheme,
``+stripe.{attempt}``.

Then I updated some fields_ in ``torch-2.0.1+stripe.2.dist-info/METADATA``:

* Updated ``Version`` to include ``+stripe.2``
* Removed the ``Requires-Dist`` line for ``triton``.
  This is the crucial step to fix the cyclic dependency problem.

Now I had to update ``torch-2.0.1+stripe.2.dist-info/RECORD``,
which contains signatures for all the files in the wheel,
in the form ``{filename},sha256={safe_hash},{filesize}``.
Of course, ``RECORD`` does not have an entry for itself.

The paths to all the ``dist-info`` files needed to be updated in ``RECORD``
to include the ``+stripe.2`` suffix.

In Vim terms:

.. code:: vim

    :%s/^\(torch-2.0.1\)\(\.dist-info\)/\1+stripe.2\2/

You can use this ``record_hash.py`` script to compute the entry for a file:

.. code:: python

    #!/usr/bin/env python3

    import base64
    import hashlib
    import os
    import sys

    filename = sys.argv[1]

    with open(filename, "rb") as f:
        digest = hashlib.sha256(f.read())
        safe_hash = base64.urlsafe_b64encode(digest.digest()).decode("us-ascii").rstrip("=")
    print(f"{filename},sha256={safe_hash},{os.path.getsize(filename)}")

The output will look like this:

.. code:: bash

    $ ../record_hash.py torch-2.0.1+stripe.2.dist-info/METADATA
    torch-2.0.1+stripe.2.dist-info/METADATA,sha256=StmZkVzCWlHIxaIGVJocXv7JsDnlrSaNXwtuIlE_PKc,24703

Replace the ``METADATA`` entry in ``RECORD`` with the output from ``record_hash.py``.

Finally, you can ``zip`` up everything into a new wheel.
Note the ``+stripe.2`` in the new wheel's filename::

    zip ../torch-2.0.1+stripe.2-cp38-cp38-manylinux1_x86_64.whl -r .

At this point, you can upload the wheel to a private repository.

To install the wheel::

    pip install torch==2.0.1+stripe.2

You will not see ``triton`` being installed, unlike before.
However, if you do install ``triton``,
it will be satisfied by this patched version of ``torch``.


Summary
-------

If you have to manually patch a Python wheel:

* Decide upon a suffix, such as ``+stripe.2``.
* Unzip the wheel.
* Rename the ``dist-info`` directory to include the suffix.
* Update ``Version`` in ``METADATA`` to include the suffix.
* **Make other modifications.**
* Append the suffix to the ``dist-info`` entries in ``RECORD``.
* Use ``record_hash.py`` to compute new entries for all modified files.
  Update ``RECORD`` accordingly.
* Zip up the new wheel. Include the suffix in the filename.
* ``pip install`` the new wheel.

.. _Python wheel:
    https://realpython.com/python-wheels/
.. _PyTorch:
    https://pytorch.org/
.. _cyclic dependency:
    https://github.com/pytorch/pytorch/issues/99622
.. _Pip:
    https://pip.pypa.io/en/latest/
.. _Bazel:
    https://bazel.build/
.. _does not handle:
    https://github.com/bazelbuild/rules_python/issues/1076
.. _patch:
    https://en.wikipedia.org/wiki/Patch_(computing)
.. _writeup on the issue:
    https://github.com/pytorch/pytorch/issues/99622#issuecomment-1604812054
.. _wheel:
    https://packaging.python.org/en/latest/specifications/binary-distribution-format/
.. _Zip archive:
    https://en.wikipedia.org/wiki/ZIP_(file_format)
.. _contents:
    https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-contents
.. _looks like:
    https://git-scm.com/docs/git-describe#_examples
.. _fields:
    https://packaging.python.org/en/latest/specifications/core-metadata/
