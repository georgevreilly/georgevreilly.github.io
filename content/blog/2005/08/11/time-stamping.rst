---
title: "TIME stamping"
date: "2005-08-11"
permalink: "/blog/2005/08/11/TIMEStamping.html"
tags: [cmd]
---



I'm a command-line dinosaur.
`Vim`__ (Vi IMproved) is my favorite text editor.
And I write quite a few little batch files.

Here are a few useful tricks that work with cmd.exe on Windows XP.

Timestamped filename
--------------------

Sometimes I want to create a file whose name includes the current date and time.
By combining the magic ``%DATE%`` and ``%TIME%`` environment variables,
with ``for /f`` and a little bit of string substitution, 
I can create that filename.

.. code-block:: winbatch

    REM
    REM "Tue 06/14/2005" -> "06/14/2005"
    REM
    for /f "tokens=2"              %%i in ("%DATE%") do set MDY=%%i
    REM
    REM "06/14/2005" -> "2005-06-14"
    REM
    for /f "delims=/ tokens=1,2,3" %%i in ("%MDY%")  do set YMD=%%k-%%i-%%j

    REM "16:44:39.72" -> "1644"
    REM
    for /f "delims=: tokens=1,2"   %%i in ("%TIME%") do set HM=%%i%%j
    REM
    REM " 237" -> "0237"    (%TIME% < 10:00:00.00 contains a leading space)
    set HM=%HM: =0% 

    xcopy /yf %1 %YMD%_%HM%.bak

See ``for /?`` and ``set /?`` to explain everything that the comments don't.

Timing Operations
-----------------

Sometimes it's useful to time operations.

.. code-block:: winbatch

    @setlocal
    @if (%_echo%)==()  set _echo=off
    @echo %_echo%

    call :time T1
    set T2=%T1%
    set Iter=0
    @echo T1 = %T1%

    :repeat
    CostlyOperation.exe

    call :time T2
    set /A DeltaT=%T2% - %T1%
    set /A Iter=%Iter% + 1
    set /A Avg=%DeltaT% / %Iter%
    @echo DeltaT = %DeltaT%, Avg = %Avg%, Iter = %Iter%, T2 = %T2%
    goto :repeat


    :time
    set TT=%TIME%
    for /f "delims=: tokens=1" %%i in ("%TT%")  do set hrs=%%i
    for /f "delims=: tokens=2" %%i in ("%TT%")  do set min=1%%i
    for /f "delims=: tokens=3" %%i in ("%TT%")  do set sec=1%%i
    set /A %1=3600 * %hrs%  +  60 * (%min%-100)  +  (%sec%-100)
    goto :EOF

The ``:time`` subroutine calculates the number of seconds that have elapsed today.
The business with 100 is to handle the case that ``min`` or ``sec`` is ``08`` or ``09``,
which Cmd's expression evaluator considers to be malformed `octal`__.

``set /?`` explains ``set /A`` arithmetic.
``call /?`` explains subroutine syntax and ``goto :EOF``.

Extending this code so that it works past midnight
is left as the proverbial `exercise for the reader`__.

__ http://www.vim.org/
__ http://weblogs.asp.net/george_v_reilly/archive/2004/12/13.aspx
__ http://catb.org/%7Eesr/jargon/html/E/exercise--left-as-an.html

.. _permalink:
    /blog/2005/08/11/TIMEStamping.html
