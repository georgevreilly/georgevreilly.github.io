---
title: "Implementing the Tree command in Rust, part 1: Walking Directories"
date: "2023-01-23"
permalink: "/blog/2023/01/23/TreeInRust1WalkDirectories.html"
tags: [rust]
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

I've split the code into two phases,
which will be covered in two blog posts.

1. Walking the directory tree on disk to build an in-memory tree.
2. Pretty-printing the in-memory tree.

While it's certainly possible to print a subtree as it's being read,
separating the two phases
yields code that is cleaner, simpler, and more testable.

In future, I will insert a third phase, *processing*,
between the reading and writing phases,
by a weak analogy with Extract-Transform-Load (`ETL`_).

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
==========================

There are three kinds of file tree node that I care about:
``File``, ``Directory``, and ``Symlink``.
These are the variants exposed by Rust's FileType__.

__ https://doc.rust-lang.org/std/fs/struct.FileType.html

* ``File`` has a name and file system metadata;
* ``Symlink`` has a name, a target, and metadata;
* ``Directory`` has a name and a list of child file tree nodes.

Here, *name* refers to the last component of a path;
e.g., the ``gamma`` in ``alpha/beta/gamma``.
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
        pub entries: Vec<FileTree>,
    }

File and directory paths are not guaranteed to be UTF-8.
Indeed, Unix file paths are an arbitrary sequence of bytes,
while Windows file paths are an opaque sequence of 16-bit integers.
You might think that I should be using ``OsString`` here,
since it holds a `platform-native string`__.
``String`` has to be valid UTF-8; ``OsString`` doesn't.
Unfortunately, it's not easy to look at the actual data in an ``OsString``,
unless you convert it (possibly lossily) to a ``String``.
See `File paths and OS strings`__ for more.

__ https://doc.rust-lang.org/std/ffi/struct.OsString.html
__ https://docs.rs/bstr/0.2.8/bstr/#file-paths-and-os-strings

The obvious way to represent a file tree node in Rust
is as an `enum`__ with three tuple-like variants.

__ https://hashrust.com/blog/why-rust-enums-are-so-cool/

.. code-block:: rust

    #[derive(Debug)]
    pub enum FileTree {
        DirNode(Directory),
        FileNode(File),
        LinkNode(Symlink),
    }

Here, each variant in the enum holds a struct of similar name.
We will be able to take advantage of Rust's `pattern matching`__
to handle each variant.

__ https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#destructuring-enums

We'll use ``fs::read_dir`` to read each directory in the hierarchy.
The read_dir__ function returns an iterator
that yields instances of ``io::Result<DirEntry>``.
If a ``DirEntry`` is a directory,
we can recursively invoke our ``dir_walk`` function
to read the child directory
and add its contents to our in-memory tree.

The walkdir__ crate also walks through a directory tree,
but it hides the recursion from you.
It's an excellent choice otherwise.

__ https://doc.rust-lang.org/std/fs/struct.ReadDir.html
__ https://docs.rs/walkdir/latest/walkdir/


Skipping and Sorting
--------------------

In each directory that we read,
we need to consider two factors.

1. Which entries to skip, such as hidden files.
2. How to sort the entries.

We almost always want to skip `hidden files and directories`__\
—on Unix, those entries whose names start with the ``.`` character.
Every directory includes entries
for ``.`` (itself) and ``..`` (parent directory),
and may include other hidden files or directories,
such as ``.vimrc`` or ``.git``.

__ https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory

On Windows, hidden files are controlled by an attribute__, not by their name.

__ https://www.raymond.cc/blog/reset-system-and-hidden-attributes-for-files-or-folders-caused-by-virus/

For more complicated usage,
we might want to skip `ignored files`__,
as specified in ``.gitignore``.

__ https://git-scm.com/docs/gitignore

The simplest useful filter for entry names
is one that rejects hidden files and directories.

.. code-block:: rust

    pub fn is_not_hidden(name: &str) -> bool {
        return !name.starts_with('.');
    }

Disk I/O is `costly and slow`__, compared to memory access.
It's far more efficient to not read a directory at all
than it is to eliminate a subtree at a later stage.
Even if the OS has cached the relevant directory contents,
there's still a `cost to the syscall`__ to retrieve that data from the kernel.

__ https://louwrentius.com/understanding-storage-performance-iops-and-latency.html 
__ https://gms.tf/on-the-costs-of-syscalls.html

There is `no specific order`__ to entries in a directory
or to the results returned by low-level APIs like ``fs::read_dir``.
By default, ``ls`` sorts entries alphabetically,
but it can also sort by creation time, modification time, or size,
in ascending or descending order.

__ https://stackoverflow.com/a/8977490/6364

Unix filesystems are case-sensitive,
but Mac filesystems (APFS and HFS+) are case-insensitive by default,
although they preserve the case of the original filename.
Windows' filesystems (NTFS, exFAT, and FAT32)
are `likewise`__ case-preserving and case-insensitive.

__ https://learn.microsoft.com/en-us/windows/win32/fileio/filesystem-functionality-comparison

Here is a case-sensitive comparator__ for use with ``sort_by``:

__ https://doc.rust-lang.org/std/vec/struct.Vec.html#method.sort_by

.. code-block:: rust

    pub fn sort_by_name(a: &fs::DirEntry, b: &fs::DirEntry) -> Ordering {
        let a_name: String =
            a.path().file_name().unwrap().to_str().unwrap().into();     ➊
        let b_name: String =
            b.path().file_name().unwrap().to_str().unwrap().into();
        a_name.cmp(&b_name)                                             ➋
    }

1. This messy expression is necessary to get the *name* as a ``String``.
2. ``cmp`` returns ``Less``, ``Equal``, or ``Greater`` from the ``Ordering`` enum.

More on ``Ordering`` here__.

__ https://www.philipdaniels.com/blog/2019/rust-equality-and-ordering/



The ``dir_walk`` function
=========================

Finally, the recursive ``dir_walk`` function that
creates the tree of ``FileTree`` nodes.

.. code-block:: rust

    pub fn dir_walk(
        root: &PathBuf,
        filter: fn(name: &str) -> bool,                 ➊
        compare: fn(a: &fs::DirEntry, b: &fs::DirEntry) -> Ordering,
    ) -> io::Result<Directory> {
        let mut entries: Vec<fs::DirEntry> = fs::read_dir(root)?
            .filter_map(|result| result.ok())
            .collect();                                 ➋
        entries.sort_by(compare);
        let mut directory: Vec<FileTree> =
            Vec::with_capacity(entries.len());          ➌
        for e in entries {
            let path = e.path();
            let name: String = path.file_name().unwrap().to_str().unwrap().into();
            if !filter(&name) {                         ➍
                continue;
            };
            let metadata = fs::metadata(&path).unwrap();
            let node = match path {                     ➎
                path if path.is_dir() => {
                    FileTree::DirNode(                  ➏
                        dir_walk(&root.join(name), filter, compare)?)
                }
                path if path.is_symlink() => FileTree::LinkNode(Symlink {
                    name: name.into(),
                    target: fs::read_link(path).unwrap().to_string_lossy().to_string(),
                    metadata: metadata,
                }),
                path if path.is_file() => FileTree::FileNode(File {
                    name: name.into(),
                    metadata: metadata,
                }),
                _ => unreachable!(),
            };
            directory.push(node);
        }
        let name = root
            .file_name()
            .unwrap_or(OsStr::new("."))                 ➐
            .to_str()
            .unwrap()
            .into();
        Ok(Directory {                                  ➑
            name: name,
            entries: directory,
        })
    }

1. Currently, the ``filter`` and ``compare`` parameters are ``fn``\ s.
   They could probably be ``FnMut`` traits.
2. Read directory.
   Discard any ``Error`` results.
   Collect into a ``Vec``.
3. We'll need at most this many entries.
4. Use ``filter`` to discard names that won't be visited.
5. Match the path as a ``DirNode``, ``LinkNode``, or ``FileNode``,
   by using `match guards`__.
6. Visit the subdirectory recursively.
7. If ``root`` was ``"."``, the ``file_name()`` will be ``None``.
8. Return a ``Directory`` for this directory, wrapped in an ``io::Result``.

In `Part 2`_, we'll print the directory tree.


__ https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#extra-conditionals-with-match-guards

.. _Part 2:
    /blog/...

.. _permalink:
    /blog/2023/01/10/TreeInRust1WalkDirectories.html
