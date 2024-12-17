---
title: "Patching and Splitting Python Wheels"
date: "2024-12-16"
permalink: "/blog/2024/12/16/PatchingAndSplittingPythonWheels.html"
tags: [python]
---

.. image:: /content/binary/patching-bike-tube.jpg
    :alt: Patching a bicycle tube
    :width: 700

I gave lightning talks at `Python Ireland`_ in May 2024 and
`Puget Sound Programming Python (PuPPy)`_ in August 2024
about patching and splitting wheels: slides_.

Patching Wheels
---------------

Last year, I wrote about manually `Patching a Python Wheel`_.
There was a cyclic dependency
between the Torch 2.0.1 wheel and the Triton 2.0.0 wheel.
While ``pip`` had no problem with this,
Bazel_ certainly did.
My workaround_ was to unzip the Torch wheel,
edit the metadata to remove the dependency on Triton,
and zip the wheel up again with a modified name.

At the beginning of this year,
I had to patch Torch 2.1 for `different reasons`_.
Again, I needed to patch the Torch wheel because of Bazel problems.
Due to the way that Bazel installs each package in a different location,
instead of one common ``site-packages``,
I had to ensure_ that Torch preloaded a series of ``lib*.so`` extensions
in *topologically sorted* order.
This time, I wrote a `patcher script`_ to apply patches to a wheel.

The `patcher script`_ uses the official wheel_ package
to do most of the work
of extracting the contents and packing the new wheel.
My `torch21 repo`_ gives two examples of how to use ``patcher``.

Splitting Wheels
----------------

There are multiple variants of the Torch wheel.
The Torch 2.1 wheel with CUDA 11.8, ``torch==2.1.2+cu118``, is 2.5GB,
and expands to 4GB!
Almost all of that is in shared object libraries (``lib/lib*.so``),
some 3.9GB.

::

    -rwxr-xr-x 1 georgevreilly stripe  125M Dec 12 18:05 libcudnn_adv_infer.so.8
    -rwxr-xr-x 1 georgevreilly stripe  241M Dec 12 18:05 libtorch_cuda_linalg.so
    -rwxr-xr-x 1 georgevreilly stripe  451M Dec 12 18:05 libtorch_cpu.so
    -rwxr-xr-x 1 georgevreilly stripe  548M Dec 12 18:04 libcublasLt.so.11
    -rwxr-xr-x 1 georgevreilly stripe  621M Dec 12 18:05 libcudnn_cnn_infer.so.8
    -rwxr-xr-x 1 georgevreilly stripe 1355M Dec 12 18:05 libtorch_cuda.so

.. image:: /content/binary/torch-topo-deps.png
    :alt: Library interdependencies
    :width: 700

An internal system that we use for remotely building Bazel actions
has a hard limit of 3GB.
This is an internal policy, not an inherent Bazel limitation,
but it led to difficulties with building apps
that wanted to use the wheel.

My solution was to split the wheel into two wheels,
a ``cudatorch`` wheel, which contained the two largest libraries,
``libtorch_cuda.so`` (1355MB) and ``libtorch_cuda_linalg.so`` (241MB),
and a modified version of the ``torch`` wheel, which contained everything else.

I had to use `patchelf`_ to modify the rpath_ of the two libs
in the ``cudatorch`` wheel to something like
``$ORIGIN:$ORIGIN/../../torch/lib``.

In the ``torch`` wheel, I had to patch ``torch/__init__.py``
to preload the ``cudatorch`` libs.

.. _Python Ireland:
    https://www.meetup.com/pythonireland/events/300802991/
.. _Puget Sound Programming Python (PuPPy):
    https://www.meetup.com/psppython/events/302211630/
.. _slides:
    https://docs.google.com/presentation/d/1YXfI7U1oVgHLSgX8uYieIGdooQK-jTqXWMhpkUrAo4U/edit?usp=sharing
.. _Patching a Python Wheel:
.. _workaround:
    /blog/2023/08/10/PatchingAPythonWheel.html
.. _Bazel:
    https://bazel.build/
.. _torch21 repo:
.. _different reasons:
.. _ensure:
    https://github.com/georgevreilly/torch21
.. _patcher script:
    https://github.com/georgevreilly/torch21/blob/main/scripts/patcher
.. _wheel:
    https://wheel.readthedocs.io/en/stable/
.. _patchelf:
    https://manpages.ubuntu.com/manpages/noble/en/man1/patchelf.1.html
.. _rpath:
    https://en.wikipedia.org/wiki/Rpath
