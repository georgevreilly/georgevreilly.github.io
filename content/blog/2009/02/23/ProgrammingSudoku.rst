---
title: "Review: Programming Sudoku"
date: "2009-02-23"
permalink: "/blog/2009/02/23/ReviewProgrammingSudoku.html"
tags: [books, reviews, programming]
---



.. image:: https://images-na.ssl-images-amazon.com/images/P/1590596625.01.MZZZZZZZ.jpg
    :alt: Programming Sudoku
    :target: http://www.elliottbaybook.com/product/info.jsp?isbn=1590596625
    :class: right-float

| Title: Programming Sudoku
| Author: Wei-Ming Lee
| Rating: ★ ★ ½
| Publisher: Apress
| Copyright: 2006
| ISBN: `1590596625 <http://www.elliottbaybook.com/product/info.jsp?isbn=1590596625>`_
| Pages: 214
| Keywords: programming, introductory
| Reading period: 22 February, 2009

I was Toastmaster of the Day at this evening's meeting of
`Freely Speaking Toastmasters`_.
My theme was software development and I wanted to give the non-developer audience
a taste for what it's like to write a program.
I talked about writing a simple Sudoku game.

Yesterday, I read *Programming Sudoku* for background.
I bought this book for Emma after reading about it on `Scott Hanselman's blog`_.
It's targeted at beginning programmers and
walks them through building a Sudoku game and solver.
I was hoping to get Emma more interested in programming—unsuccessfully.
She found it repetitious and a little confusing,
and she found some typos in the code.

Pedagogically, the book is good.
It starts by creating a simple WinForms application
in Visual Basic to play a Sudoku game.
Then it builds a solver for simple games
and refines the solver to handle harder games.
Next, it adds a puzzle generator.
It concludes with a brief chapter on a similar game, Kakuro.
The explanation of gameplay is clear;
the approach seems reasonable.

The code, however, is horrible.
It's ugly, it's verbose, and it's repetitive.
Consider that the code for doing some operation to a row is
almost identical to doing the same operation to a column,
but no attempt is made to abstract such operations into helper functions.

Or how about this unexplained fragment to see if a column is complete,
which is repeated often, with minor variations::

    pattern = "123456789"
    For r = 1 To 9
        pattern = pattern.Replace(actual(c,r).ToString(), String.Empty)
    Next
    If pattern.Length > 0 Then
        Return False
    End If

To me, it's obvious that this is a poor man's set difference operation.
To a novice programmer, I doubt it.

Examples should be exemplary and held to a higher standard
than code that is not intended for public view.
All too often, sample code ends up in production.
When I wrote `samples for classic ASP`_,
I took care to make them good code.

The book is short.
The author could have shown some ugly code as an initial solution,
then cleaned it up and explained why the new code was better.
That would have done his readers a greater service.

I cannot recommend this book to novices:
they won't learn good habits from it.

.. _Freely Speaking Toastmasters:
    http://www.FreelySpeaking.org/
.. _Scott Hanselman's blog:
    http://www.hanselman.com/blog/ProgrammingSudoku.aspx
.. _samples for classic ASP:
    https://github.com/georgevreilly/sample-ASP-components

.. _permalink:
    /blog/2009/02/23/ReviewProgrammingSudoku.html
