---
title: "Python Batchfile Wrapper"
date: "2006-12-29"
permalink: "/blog/2006/12/29/PythonBatchfileWrapper.html"
tags: [python, cmd, til]
---



.. image:: /content/binary/PythonBatch.jpg
    :alt: Python Batchfile Wrapper

I've been getting into Python lately. One problem that I've encountered
under Windows, is that input redirection doesn't work if you use
the ``.py`` file association to run the script; e.g.::

    C:\> foo.py < input.txt

There's a well-known `input redirection bug`_. The fix is to explicitly use
``python.exe`` to run the script.

A related problem for me was that ``stdin`` was opened as a *text* file,
not a *binary* file, so ``\r`` bytes were being discarded from binary input
files. The fix is to run ``python.exe -u`` (unbuffered binary input and
output).

I didn't want to hardcode the path to ``python.exe`` in a batch file,
so I came up with the following wrapper, which parses the output from
``assoc .py`` and ``ftype Python.File``.

Just place this batch file in the same directory as ``foo.py`` and call it
``foo.bat``.


.. code:: batch

    @setlocal
    @if (%_echo%)==()  set _echo=off
    @echo %_echo%

    :: You must explicitly invoke python.exe, rather than rely on the
    :: file association for .py, if you want stdin redirection to work.
    :: See http://mail.python.org/pipermail/python-bugs-list/2004-August/024920.html
    :: The -u flag to python.exe specifies unbuffered, binary stdin,
    :: so '\r\n' is not remapped to '\n'.
    call :FindPythonExe

    if "%PythonExe%"=="" (
        echo Can't find python.exe
        exit /B 1
    )

    :: Replace the extension of this batch file with .py: s/.bat$/.py/
    set PythonFile=%~dpn0.py

    "%PythonExe%" -u %PythonFile% %*
    goto :EOF


    ::
    :: Find python.exe in the path or via the .py association
    ::
    :FindPythonExe
    set PythonExe=
    :: Search for python.{cmd,bat,exe} in %PATH%
    for %%i in (cmd bat exe) do (
        if "%PythonExe%"=="" (
            for %%j in (python.%%i) do set PythonExe=%%~$PATH:j
        )
    )
    :: Extract path to python.exe from .py association
    if "%PythonExe%"=="" call :AssocPy2Exe
    goto :EOF


    ::
    :: Return the executable associated with .py in %PythonExe%
    ::
    :AssocPy2Exe
    call :AssocExtn2Exe .py
    set PythonExe=%_exe%
    goto :EOF

    ::
    :: Return the executable associated with file extension %1 in %_exe%
    ::
    :AssocExtn2Exe
    :: assoc .py -> .py=Python.File
    for /f "usebackq tokens=2 delims==" %%i in (`assoc %1`) do set _ftype=%%i

    :: ftype Python.File -> Python.File="C:\Python24\python.exe" "%1" %*
    :: Grab everything after the '='
    for /f "usebackq tokens=2 delims==" %%i in (`ftype %_ftype%`) do set _rhs=%%i

    :: Get the first token of the space-separated list
    for /f "tokens=1" %%i in ("%_rhs%") do set _exe=%%i
    goto :EOF

Now you can run ``foo.bat < bar.jpg`` with the expected results.

Enjoy!

**Update 2006/01/03**:
The batchfile now searches ``%PATH%`` before looking
up the ``.py`` association.

**Update 2007/01/12**:
See `here </blog/2007/01/13/PythonBatchfileWrapperRedux.html>`_
for a significantly improved batchfile and for py2cmd.

.. _input redirection bug:
    http://mail.python.org/pipermail/python-bugs-list/2004-August/024920.html

.. _permalink:
    /blog/2006/12/29/PythonBatchfileWrapper.html
