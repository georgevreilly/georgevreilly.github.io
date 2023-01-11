---
title: "Implementing the Tree command in Rust, part 1: Walking Directories"
date: "2023-01-10"
permalink: "/blog/2023/01/10/TreeInRust1WalkDirectories.html"
tags: [rust]
draft: true
---



.. image:: /content/binary/rust-core-src-num-tree.png
    :alt: tree tree core/src/num for Rust
    :width: 160
    :class: right-float

I've been learning Rust lately.
At first, I read several books,
including `Rust in Action`_,
`Code Like a Pro in Rust`_,
and most of `Programming Rust`_.
Now, I'm starting to actually write code.

I read the `Command-Line Rust`_ book last month,
which challenged readers to write
our own implementations of the `tree command`_.

I decided to accept the challenge.

At its simplest, ``tree`` simply prints a directory tree,
using some of the Unicode `Box Drawing`_ characters
to show the hierarchical relationship,
as in the image at right.

I've split the code into two phases:

1. Walking the directory tree on disk to build an in-memory tree.
2. Pretty-printing the in-memory tree.

While it's certainly possible to print a subtree as it's being read,
separating the two phases
yields code that is cleaner and simpler and more testable.

In future, I will insert a third phase, *processing*,
between the reading and writing phases,
by analogy with Extract-Transform-Load (`ETL`_).

.. _Rust in Action:
    https://www.manning.com/books/rust-in-action
.. _Code Like a Pro in Rust:
    https://www.manning.com/books/code-like-a-pro-in-rust
.. _Command-Line Rust:
    https://www.goodreads.com/review/show/5183138397
.. _Programming Rust:
    https://learning.oreilly.com/library/view/programming-rust-2nd/9781492052586/
.. _tree command:
    https://en.wikipedia.org/wiki/Tree_(command)
.. _Box Drawing:
    https://www.compart.com/en/unicode/block/U+2500
.. _ETL:
    https://en.wikipedia.org/wiki/Extract,_transform,_load

Walking the Directory Tree
--------------------------

There are three kinds of file tree node that I care about:
``File``, ``Directory``, and ``Symlink``.
These are the variants exposed by Rust's FileType__.

__ https://doc.rust-lang.org/std/fs/struct.FileType.html

* ``File`` has a name and file system metadata;
* ``Symlink`` has a name, a target, and metadata;
* ``Directory`` has a name and a list of child file tree nodes.

The file system metadata is not currently used,
but will be in future.

.. code-block:: rust

    #[derive(Debug)]
    pub struct File {
        pub name: String,
        pub metadata: fs::Metadata,
    }

    #[derive(Debug)]
    pub struct Symlink {
        pub name: String,
        pub target: String,
        pub metadata: fs::Metadata,
    }

    #[derive(Debug)]
    pub struct Directory {
        pub name: String,
        pub entries: Vec<FileTreeNode>,
    }

The obvious way to represent a file tree node in Rust
is as an `enum`__ with three variants.

__ https://hashrust.com/blog/why-rust-enums-are-so-cool/

.. code-block:: rust

    #[derive(Debug)]
    pub enum FileTreeNode {
        Directory(Directory),
        File(File),
        Symlink(Symlink),
    }

Here, each variant in the enum holds a struct of the same name.
We will be able to take advantage of Rust's pattern matching
to handle each variant.

We'll use ``fs::read_dir`` to read each directory in the hierarchy.
The read_dir__ function returns an iterator
that yields instances of ``io::Result<DirEntry>``.

The walkdir__ crate also walks through a directory tree,
but it hides the recursion from you.
It's an excellent choice otherwise.

__ https://doc.rust-lang.org/std/fs/struct.ReadDir.html
__ https://docs.rs/walkdir/latest/walkdir/

In each directory that we read,
we need to consider two factors.

1. Which entries to skip, such as hidden files.
2. How to sort the entries.

We almost always want to skip hidden files—\
on Unix, those whose filenames start with the ``.`` character.
Every directory includes entries
for ``.`` (itself) and ``..`` (parent directory),
and may include other hidden files or directories,
such as ``.python-version`` or ``.git``.
For more complicated usage, we might want to skip
*ignored* files, as specified in ``.gitignore``.

Disk I/O is expensive.
It's much more efficient to never read a directory
than it is to eliminate a subtree at a later stage.

There is no specific order to entries in a directory.
The ``ls`` command sorts entries alphabetically by default,
but it can also sort by creation time, modification time, or size,
in ascending or descending order.



.. _permalink:
    /blog/2023/01/10/TreeInRust1WalkDirectories.html
