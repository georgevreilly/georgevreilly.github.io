---
title: "Jenkins #6: Miscellenea"
date: "2017-02-09"
permalink: "/blog/2017/02/09/Jenkins06-Miscellenea.html"
tags: [jenkins, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/

A collection of miscellaneous tips on using Pipelines in Jenkins 2.0.

`#6 in a series on Jenkins Pipelines 
</blog/2017/02/04/Jenkins01-MigratingToPipelines.html>`_


Environment Variables
^^^^^^^^^^^^^^^^^^^^^

Use the ``withEnv`` step to set environment variables.
Don't manipulate the ``env`` global variable.

The confusing example that you see in the documents,
``PATH+WHATEVER=/something``,
simply means to *prepend* ``/something`` to ``$PATH``.
The ``+WHATEVER`` has no other effect.


Credentials
^^^^^^^^^^^

The ``withEnv`` step should not be used to introduce secrets into the build environment.
Use the withCredentials__ plugin instead.

.. code-block:: groovy

    withCredentials([
        [$class: 'StringBinding', credentialsId: 'GPG_SECRET', variable: 'GPG_SECRET'],
        [$class: 'AmazonWebServicesCredentialsBinding',
         credentialsId: '0defaced-cafe-f00d-badd-0000000ff1ce',
         accessKeyVariable: 'AWS_ACCESS_KEY_ID',
         secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']
    ]) { 

__ https://wiki.jenkins-ci.org/display/JENKINS/Credentials+Binding+Plugin

Tip: Use the Pipeline Syntax Snippet Generator from *your* Jenkins project
to figure out the exact invocation for your credentials.

If you need to display environment variables for debugging purposes,
you can use something like this Python script instead of ``sh 'env | sort'``,
which can leave secrets in cleartext in your logs.
Note that ``withCredentials`` will mask values that it knows about.

.. code-block:: python

    #!/usr/bin/env python

    import os, re

    BLOCKLIST_RE = re.compile(r'^(.*_)?(PASSWORD|AUTH|TOKEN|SECRET|KEY)(_.*)?$')

    for k in sorted(os.environ.keys()):
        v = os.environ[k]
        if BLOCKLIST_RE.match(k) and len(v) > 2:
            v = '*{}{}{}*'.format(v[0], len(v)-2, v[-1])
        print('{}={}'.format(k, v))


Cleaning Up Workspaces
^^^^^^^^^^^^^^^^^^^^^^

You may need to clean up your workspace.
`Don't remove the .git directory`__.

.. code-block:: groovy

    sh "ls -A1 | grep -v "^\\.git\$" | xargs rm -rf"

* ``ls -A1`` lists all the files and directories in the current directory,
  except ``.`` and ``..``, one per line.
* The ``grep -v`` excludes ``^\.git$``.
  Note that the :literal:`\\` and the ``$`` are escaped in the ``sh`` step
  to prevent `GString interpolation`__.
* The ``xargs rm -rf`` deletes the remaining files and directories.

__ ../jenkins-03-github-integration/
__ ../jenkins-04-sh-step/


Editing Jenkinsfile
^^^^^^^^^^^^^^^^^^^

Be sure to put ``#!groovy`` as the first line in your ``Jenkinsfile``,
as a hint to your editor to use Groovy syntax highlighting.

We use PyCharm__ a lot, since we're a Python shop.
However, despite being written in Java, PyCharm's support for Groovy is mediocre.
You're expected to buy JetBrains' IntelliJ IDE.

Vim__ has built-in support for Groovy.
Atom__ with the `language-groovy`__ package works great.
Many other editors also support Groovy.

__ https://www.jetbrains.com/pycharm/
__ https://www.vim.org/
__ https://atom.io/
__ https://atom.io/packages/language-groovy


Stashes and Artifacts
^^^^^^^^^^^^^^^^^^^^^

Use ``stash`` and ``unstash`` to get artifacts across nodes within a pipeline.
If you're using the ``parallel`` step,
some of your branches will start out with an empty workspace,
and ``unstash`` is the easiest way to prime the workspace.

If you need to transfer artifacts between different builds,
you'll need to use ``archiveArtifacts`` and ``CopyArtifact``.

In project ``build-1``:

.. code-block:: groovy

    archiveArtifacts artifacts: 'my_artifact.zip', fingerprint: true

In project ``build-2``:

.. code-block:: groovy

    step ([$class: 'CopyArtifact',
           projectName: 'build-1',
           filter: 'my_artifact.zip',
           selector: [$class: 'StatusBuildSelector']
          ]);

Note that the ``StatusBuildSelector`` selector is picking the artifact
from the last successful build of ``build-1``.

You can find the various selectors in the `CopyArtifact source`__.
If you dig into the tests, you can probably figure out how to use the other selectors.

In ``build-1``, you can use ``build job: 'build-2', wait: false`` to kick off ``build-2``.

__ https://github.com/jenkinsci/copyartifact-plugin/tree/master/src/main/java/hudson/plugins/copyartifact


Debugging
^^^^^^^^^

Here are some tricks for debugging.

Local Groovy
~~~~~~~~~~~~

Run `Groovy locally`__ to debug syntax issues and Groovy functions.

__ /blog/2017/02/08/Jenkins05-Groovy.html

timestamps and ansiColor
~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``timestamps`` plugin to get timestamps to appear in the Jenkins log.
This is so useful that it should be the default.

The ``ansiColor`` plugin will generate transform colored console output
into colored log output.

.. code-block:: groovy

    node('ubuntu') {
        timestamps {
            ansiColor('xterm') {
                stage("Source Checkout") {
                    checkout scm

Job Debugging
~~~~~~~~~~~~~

Instead of troubleshooting build problems in a slow heavyweight job,
create a new lightweight job that isolates the problem.
You may get your iteration time down to a minute or so,
instead of many minutes.

Temporarily use "Pipeline script" instead of "Pipeline script from SCM",
so that you can try out changes more quickly.
Note that ``checkout scm`` won't work unless the Pipeline script comes from SCM.

The ``Replay`` command in the left menu lets you edit the Pipeline script
and rerun it.

sh Errors
~~~~~~~~~

You can use `cat -n $0`__ to echo the interpolated ``sh`` script to the log.

__ /blog/2017/02/07/Jenkins04-shStep.html

.. _permalink:
    /blog/2017/02/09/Jenkins06-Miscellenea.html
