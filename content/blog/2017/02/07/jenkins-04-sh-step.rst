---
title: "Jenkins #4: The sh Step"
date: "2017-02-07"
permalink: "/blog/2017/02/07/Jenkins04-shStep.html"
tags: [jenkins, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/

If there isn't a built-in Pipeline step to accomplish something,
you'll almost certainly use the `sh step`__.

`#4 in a series on Jenkins Pipelines 
</blog/2017/02/04/Jenkins01-MigratingToPipelines.html>`_

The ``sh`` step runs the Bourne shell—\
``/bin/sh``, *not* Bash aka the Bourne-again shell\ —\
with the ``-x`` (``xtrace``) and ``-e`` (``errexit``) options.

The ``xtrace`` option means that every step in the ``sh`` block is echoed to the Jenkins log,
after commands have been expanded by the shell.
This is useful but you could echo the contents of passwords or secret keys inadvertently.
Use ``set +x`` in your ``sh`` block to control this.

The ``errexit`` option means that the script will abort on the first error.
You can control__ this by testing ``if ! command; then …``
or using ``command || true``.

__ https://jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#code-sh-code-shell-script
__ https://www.davidpashley.com/articles/writing-robust-shell-scripts/

You can override the choice of shell by providing a shebang on the first line:

.. code-block:: groovy

    sh """#!/usr/bin/env python

        print([x**2 for x in range(5)])
    """

Be sure to put the shebang on the *first* line, immediately after the opening quote.

Groovy supports `multiple syntaxes for strings`__:
single-quote (one line, no interpolation),
double-quote (one line, interpolation__ aka GStrings),
triple single-quote (multiline, no interpolation), and
triple double-quote (multiline, interpolation).

GString interpolation is very, very useful
but you must be careful to *escape* dollar signs and backslashes meant for the shell.

.. code-block:: groovy

    sh """
        sudo docker run --rm --env-file \$TMPDIR/envfile \\
            --volume "\$(pwd)/${results_dir}:/webapp/build_output/test" \\
            "$image_name" ${command}
    """

For example, ``results_dir``, ``image_name``, and ``command``
are all Groovy string variables,
while ``\$TMPDIR`` is an (escaped) shell environment variable,
``\$(pwd)`` is an (escaped) example of shell `command substitution`__,
and the trailing :literal:`\\\\`\ s
turn into single :literal:`\\`\ s (line continuation markers)
when they are seen by the shell.

I've occasionally found it helpful to put ``cat -n \$0`` into some ``sh`` blocks.
Pipeline creates a temporary file holding the contents of the ``sh`` block
after GString interpolation.
When executed, ``$0`` is the name of the temporary script file.
The ``-n`` argument to ``cat`` precedes each line with its line number.
In other words, this shows the *actual* script with line numbers.
This technique helped me debug a problem
where an interpolated string contained an unexpected trailing newline,
which split the Groovy string across two shell lines.
I fixed that problem with ``trim()``.

If you need to capture the *output* of a ``sh`` block's execution, use ``returnStdout``:

.. code-block:: groovy

    String commit = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()

Typically, you will want to ``trim()`` (single line)
or ``split()`` (multiline) the result.

Finally, if you have more than a few lines in a ``sh`` block,
consider putting them into a separate script,
which can be independently tested and kept in source code.

__ https://groovy-lang.org/syntax.html#all-strings
__ https://groovy-lang.org/syntax.html#_string_interpolation
__ https://tldp.org/LDP/abs/html/commandsub.html

.. _permalink:
    /blog/2017/02/07/Jenkins04-shStep.html
