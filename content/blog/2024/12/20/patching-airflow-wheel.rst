---
title: "Patching Airflow Wheels"
date: "2024-12-20"
permalink: "/blog/2024/12/20/PatchingAirflowWheels.html"
tags: [python]
---

In `Patching and Splitting Python Wheels`_,
I wrote about some occasions when I had to take a `Python wheel`_
and patch it.
Now I want to tell you about a very different approach
that I used recently to patch Airflow wheels.

With the other wheels, we just needed to apply some tactical patches.
With Airflow, we are making substantive changes.

.. image:: /content/binary/ApacheAirflowLogo.png
    :alt: Apache Airflow
    :target: https://airflow.apache.org/

We've been using Airflow_ for years at work.
We built up a lot of infrastructure around Airflow 1
and we are gradually migrating to `Airflow 2`_.

Several years ago, we forked the `airflow package`_
and made a large number of changes to it for internal consumption.
Unfortunately, this made it increasingly hard for us to merge changes
from the `upstream repo`_ into our internal Git repository,
as the repos continued to diverge.

Airflow's `current release workflow`_:

* Create a release branch from ``main``.
* Create release candidates.
* Fix any problems, including cherry-picking from ``main``.
* Publish the final release, which is tagged_.
  The package is uploaded to PyPI.

Note that this tagged branch is never merged back to ``main``,
so you cannot checkout an official release from the ``main`` branch.
You must checkout the tag instead.
(I don't know if this was also the release workflow for Airflow 1.)

Our internal workflow is different.
Engineers work on feature branches and create pull requests.
These pull requests get merged into ``master``.
Production deployments are built from ``master`` only.
We don't use tagged releases.
This ``master``-centric assumption is baked deeply
into our build and continuous integration systems.
Since the upstream ``main`` doesn't have release code,
it's not suitable for merging into our ``master``.

Git Clone Workflow
------------------

To avoid the difficulties that we caused ourselves with Airflow 1,
we created a fresh repository for Airflow 2,
which does *not* have a copy of the upstream repo's code.
We now maintain a set of patches for each upstream release that we care about.
This new repo has build scripts and patches only.

When I first set this up,
I had the CI build script create a shallow clone of the upstream repo,
then check out each tag,
and apply our patches.

.. code:: bash

    # NOT SHOWN: create a virtualenv with Hatch and other build dependencies
    # from Airflow's pyproject.toml

    git clone --depth=1 https://github.com/apache/airflow.git worktree
    cd worktree

    for tag in ("2.10.2" "2.10.4"); do
        git reset --hard HEAD
        rm -rf dist
        git fetch --depth 1 origin "$tag"
        git checkout --quiet FETCH_HEAD

        for p in ../patches/"$tag"/*.patch; do
            git am < "$p"
        done

        python3 -m build --wheel
        cp dist/* ../build
    done

The first patch for each tag changes the version information
so that our wheel won't conflict with the official wheel from upstream.
It updates ``tool.hatch.version`` in ``pyproject.toml`` to read:

.. code:: toml

    [tool.hatch.version]
    source = "code"
    expression = "stripe_airflow_version()"
    path = "stripe_version.py"

instead of extracting the version information from ``airflow/__init__.py``.

The ``stripe_version.py`` script uses `git describe`_
to get the number of additional commits in our branch
and the abbreviated SHA of the most recent commit,
then prefixes these items with ``+stripe.${MAJOR}.``
All of this is suffixed to the actual version number from upstream,
so we build a wheel that is named something like
``apache_airflow-${TAG}+stripe.1.${COUNT}.g${SHA}-py3-none-any.whl``.

While this system produced a working wheel,
there was one critical omission.
The official upstream wheel contained an extra 37MB of UI code in ``www/static``,
which is used by the various Airflow website UIs.

I spent quite a bit of effort to make our build generate this extra payload,
but it turned out to be very difficult.
``python3 -m hatch build -t custom``
requires Node.js and does a lot of extra steps
that didn't interact well with the locked down egress rules of our CI.

Source Distribution Workflow
----------------------------

I realized that all of the ``www/static`` tree could be
extracted from the official release,
and that we didn't have to generate it in CI.

Instead of checking out a tag,
our CI downloads the official `source distribution`_ tarball,
``apache_airflow-${RELEASE}.tar.gz``,
untars the contents,
applies our patches using ``patch --strip=1`` instead of ``git am``,
and builds a new wheel.

It took me a while to figure out why our custom versioning wasn't working.
Because the sdist contains a file called ``PKG-INFO`` at the root,
Hatch takes the version from that.
I had to update the ``stripe_version.py`` script to modify
the ``Version:`` line in ``PKG-INFO``.

Format-Patch Workflow
---------------------

So far, I've covered how the patched wheel is built in CI,
but not how you would create new patches.

For local development, you can check out the upstream tag
(see ``FETCH_HEAD`` above),
then apply any existing patches that are relevant.
Make other changes, commit them locally, and build the wheel by hand.
When you have tested and have something that you're happy with,
you can use `git format-patch`_ to create a series of patches.
These patches can then be committed to the repo that we use to build the wheels.

This workflow is less convenient
than making changes directly in the forked code,
as we did with Airflow 1.
But now we only have a moderate amount of friction
to upgrade to a newer release from upstream,
instead of ever-increasing difficulty.

.. _Patching and Splitting Python Wheels:
   /blog/2024/12/16/PatchingAndSplittingPythonWheels.html
.. _Python wheel:
    https://realpython.com/python-wheels/
.. _Airflow:
    https://airflow.apache.org/
.. _Airflow 2:
    https://www.astronomer.io/blog/introducing-airflow-2-0/
.. _airflow package:
    https://pypi.org/project/apache-airflow/
.. _upstream repo:
    https://github.com/apache/airflow
.. _current release workflow:
    https://github.com/apache/airflow/blob/2.10.2/dev/README_RELEASE_AIRFLOW.md
.. _tagged:
    https://git-scm.com/book/en/v2/Git-Basics-Tagging
.. _git describe:
    https://git-scm.com/docs/git-describe
.. _source distribution:
    https://packaging.python.org/en/latest/specifications/source-distribution-format/
.. _git format-patch:
    https://git-scm.com/book/en/v2/Distributed-Git-Maintaining-a-Project
