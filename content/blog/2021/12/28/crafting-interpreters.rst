---
title: "Review: Crafting Interpreters"
date: "2021-12-28"
permalink: "/blog/2021/12/28/ReviewCraftingInterpreters.html"
tags: [books, reviews]
---



.. image:: https://images-na.ssl-images-amazon.com/images/I/41-7uSeOyCL._SX398_BO1,204,203,200_.jpg
    :alt: Crafting Interpreters
    :target: https://www.amazon.com/dp/0990582930/?tag=georgvreill-20
    :class: right-float

| Title: `Crafting Interpreters`_
| Author: Robert Nystrom
| Rating: ★ ★ ★ ★ ★
| Publisher: Genever Benning
| Copyright: 2021
| ISBN: `978-0990582939 <https://www.amazon.com/dp/0990582930/?tag=georgvreill-20>`_
| Pages: 640
| Keywords: programming, interpreters
| Reading period: 10–28 December, 2021

I've read hundreds of technical books over the last 40 years.
*Crafting Interpreters* is an instant classic,
and far more readable and fun than many of the classics.

Nystrom covers a lot of ground in this book,
building two very different interpreters for Lox,
a small dynamic language of his own design.
He takes us through *every line* of
jlox, a Java-based tree-walk interpreter,
and of clox, a bytecode virtual machine written in C.

For the first implementation, jlox,
he covers such topics as scanning,
parsing expressions with recursive descent,
evaluating expressions, control flow,
functions and closures, classes, and inheritance.

Starting with an empty slate,
Nystrom adds just enough code to implement the topic
of each chapter,
having a working albeit incomplete implementation of the interpreter
by the end of the chapter.
He adds new code as he goes,
inserting an extra ``case`` into a ``switch`` here
or writing a new function there,
or replacing a few lines of an earlier implementation
with something that's just been explained.
Knuth's `Literate Programming`_ explains a finished implementation,
broken into separate pieces for exposition.
Nystrom's continual, ever-evolving exposition is slower to get to the point,
but it's excellent pedagogy.
I would be remiss if I didn't mention the hundreds of hand-drawn illustrations,
which add a quirky flavor to the tone of the book.
He has a blog post on how he `pulled this organization off`__
and another on how he created a `physical book`__ from the text.

__ http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/
__ http://journal.stuffwithstuff.com/2021/07/29/640-pages-in-15-months/

clox is a very different second implementation of a Lox interpreter.
Instead of a slow interpreter walking an abstract syntax tree,
he develops a stack-based virtual machine,
compiles Lox into bytecode,
and interprets the bytecode.
He covers theory and practical considerations
for creating a bytecode virtual machine,
makes use of Pratt’s “top-down operator precedence parsing”,
and implements closures and classes in C.
In jlox, he used Java's ``HashMap`` to manage identifiers
and relied on Java's garbage collection for memory management.
For clox, he implements a hash table and a mark-and-sweep garbage collector.
Although he has to cover similar topics (parsing, local variables, closures) each time,
he finds a fresh perspective for the second implementation.

I read the entire book for free at https://craftinginterpreters.com/,
but I liked it so much that I've ordered a physical copy.
In fact, I actually read much of the book on the website in 2020,
but life intervened and I didn't finish it,
so this month, I read it again from the start.

This book is not a textbook and you don't get an exhaustive introduction
to building interpreters, much less compilers.
In the final year of my Computer Science degree at Trinity College Dublin in 1986–87,
I studied the `Dragon Book`_ when the first edition was brand new.
*Crafting Interpreters* is a lot more fun than the Dragon Book.

Highly recommended!

.. _Crafting Interpreters:
   https://craftinginterpreters.com/
.. _Literate Programming:
   https://en.wikipedia.org/wiki/Literate_programming
.. _Dragon Book:
   https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools

.. _permalink:
    /blog/2021/12/28/ReviewCraftingInterpreters.html
