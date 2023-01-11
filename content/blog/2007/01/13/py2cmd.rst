---
title: "Python Batchfile Wrapper, Redux"
date: "2007-01-13"
permalink: "/blog/2007/01/13/PythonBatchfileWrapperRedux.html"
tags: [python, cmd]
---



.. image:: /content/binary/PythonBatch.jpg
    :alt: Python Batchfile Wrapper

Batchfile Wrapper
=================

I've made some significant changes to my `Python Batchfile Wrapper`_.
The main virtue of this wrapper is that it finds python.exe and
invokes it on the associated Python script,
ensuring that `input redirection`_ works.

.. _Python Batchfile Wrapper:
    /blog/2006/12/29/PythonBatchfileWrapper.html
.. _input redirection:
    http://mail.python.org/pipermail/python-bugs-list/2004-August/024920.html

I've also adapted `py2bat`_ to work with my wrapper.
I'm calling my version `py2cmd`_.

Here's my latest batch file, which is shorter than its predecessor.

To use it, place it in the same directory as the Python script
you want to run and give it the same basename;
i.e., ``d:\some\path or other\example.cmd``
will run ``d:\some\path or other\example.py``.

.. code:: batch

    @echo off
    setlocal
    set PythonExe=
    set PythonExeFlags=-u

    for %%i in (cmd bat exe) do (
        for %%j in (python.%%i) do (
            call :SetPythonExe "%%~$PATH:j"
        )
    )
    for /f "tokens=2 delims==" %%i in ('assoc .py') do (
        for /f "tokens=2 delims==" %%j in ('ftype %%i') do (
            for /f "tokens=1" %%k in ("%%j") do (
                call :SetPythonExe %%k
            )
        )
    )
    "%PythonExe%" %PythonExeFlags% "%~dpn0.py" %*
    goto :EOF

    :SetPythonExe
    if not [%1]==[""] (
        if ["%PythonExe%"]==[""] (
            set PythonExe=%~1
        )
    )
    goto :EOF

This is sufficiently cryptic that it merits some explanation.

The first set of nested loops attempts to find
``python.cmd``, ``python.bat``, and ``python.exe``, respectively,
along your PATH:

.. code:: batch

    for %%i in (cmd bat exe) do (
        for %%j in (python.%%i) do (
            call :SetPythonExe "%%~$PATH:j"
        )
    )

The ``%%~$PATH:j`` expression searches the PATH for ``%%j``
(i.e., ``python.cmd``, etc).
If it's found, the expression evaluates to the full path to ``%%j``.
Otherwise, it evaluates to the empty string.
I've bracketed the expression with `double quotes`_ in order to handle
spaces in directory names.

.. _double quotes: http://ss64.com/ntsyntax/esc.html
.. _parameter syntax: http://ss64.com/ntsyntax/parameters.html
.. _for loops: http://ss64.com/nt/for.html
.. _variable expansion:
    http://www.robvanderwoude.com/variableexpansion.html

The ``SetPythonExe`` subroutine simply sets ``%PythonExe%`` to ``%1``
if and only if ``%PythonExe%`` doesn't already have a value *and*
``%1`` is not empty.

We can't set ``%PythonExe%`` directly in the loop.
As explained at `for loops`_ and `variable expansion`_,
environment variables in the body of the loop are
evaluated once *before* the loop starts and
won't change until after the loop terminates:

.. code:: batch

    :SetPythonExe
    if not [%1]==[""] (
        if ["%PythonExe%"]==[""] (
            set PythonExe=%~1
        )
    )
    goto :EOF

Note: the ``%~1`` notation strips off any surrounding double quotes.
(ss64.com has details on `parameter syntax`_.)

The square brackets and double quotes are necessary to make it all work
if either ``%PythonExe%`` or ``%1`` contains spaces.
Getting this right was one of the hardest parts of the whole exercise.

The second set of nested loops are scarier:

.. code:: batch

    for /f "tokens=2 delims==" %%i in ('assoc .py') do (
        for /f "tokens=2 delims==" %%j in ('ftype %%i') do (
            for /f "tokens=1" %%k in ("%%j") do (
                call :SetPythonExe %%k
            )
        )
    )

The outer loop runs once:
``assoc .py`` yields ``.py=Python.File``
and ``%%i`` is set to ``Python.File``.
Running ``ftype Python.File`` yields
``Python.File="C:\Python24\python.exe" "%1" %*`` (on my machine).

The second loop also runs once:
``%%j`` is set to everything on the right-hand side of the ``=``.

The third loop also runs once:
``%%k`` is set to the first token in ``%%j``, ``"C:\Python24\python.exe"``,
which is passed in to ``SetPythonExe``.

At this point, ``%PythonExe%`` will have a value if
``python.cmd`` (or ``python.bat`` or ``python.exe``) existed on your path,
or the ``.py`` extension was registered.

If it doesn't have a value, then the invocation of ``"%PythonExe%"`` will
fail, setting ``%errorlevel%`` to 9009:

.. code:: batch

    "%PythonExe%" %PythonExeFlags% "%~dpn0.py" %*
    goto :EOF

``%PythonExeFlags%`` was set to ``-u`` at the beginning of the script.
As explained in my `Python Batchfile Wrapper`_ post,
this treats stdin, stdout, and stderr as raw streams,
instead of transliterating ``\r\n`` into ``\n``.
If you want cooked input, simply remove the ``-u``.

The ``"%~dpn0.py"`` notation yields the absolute path to the
Python script with the ``.py`` extension sitting beside this batch file:
another example of `parameter syntax`_.

Finally, ``goto :EOF`` ends execution of the batchfile,
skipping the ``:SetPythonExe`` subroutine.

Whew!


py2cmd
======

You can have a batchfile sitting alongside a Python script as above,
or you can have a self-contained batchfile cum Python script.

`py2bat`_ has been kicking around for years.
It takes a Python script and turns it into a batchfile,
by relying on a couple of tricks.

.. _py2bat:
    http://mail.python.org/pipermail/python-list/2000-January/019450.html
.. _py2cmd:
    /Python/py2cmd/

I've adapted py2bat into a new script, `py2cmd`_.
In essence, the generated batchfile looks like this:

.. code:: batch

    @echo off
    REM="""
    ... set PythonExe as above ...
    "%PythonExe%" -x %0
    goto :EOF
    """

    # python code starts here
    # ...

When this file is executed by cmd.exe, the control flow should be obvious.
Disable echoing to the screen,
a funny-looking REM,
set ``%PythonExe%`` as before (not shown),
invoke ``python.exe`` with the ``-x`` flag on the current batchfile,
and finally skip past the rest of the file.

When Python is invoked with the ``-x`` flag,
it skips the first line of the script (``@echo off``).
The second line sets the variable ``REM`` to the multiline string
which continues down to the closing ``"""`` below the ``goto :EOF``.
Everything after that is the original Python script.
All the batchfile nonsense is wrapped up inside the ``REM`` variable.

Download `py2cmd`_.


Other Wrappers
==============

Fredrik Lundh's `ExeMaker`_ generates a stub executable to launch
a Python script with the same basename.
It requires that Python already be installed on the target machine.
I couldn't get ExeMaker to work properly.
The stub executable leaves me at the Python interpreter's interactive prompt.

`py2exe`_ takes a Python script and bundles up all the Python support files
to make it run on a machine that doesn't have Python installed.
Works fine for me, but you get 4MB+ of associated runtime.
Massive overkill if the target machine is known to have Python installed.

.. _ExeMaker: http://effbot.org/zone/exemaker.htm
.. _py2exe: http://www.py2exe.org/

.. _permalink:
    /blog/2007/01/13/PythonBatchfileWrapperRedux.html
