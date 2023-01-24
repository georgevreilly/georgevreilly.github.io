---
title: "Implementing the Tree command in Rust, part 2: Printing Trees"
date: "2023-01-24"
permalink: "/blog/2023/01/24/TreeInRust2PrintingTrees.html"
tags: [rust]
draft: true
---

In `Part 1`_, we saw how to walk directory trees,
recursively using ``fs::read_dir``
to construct an in-memory tree of ``FileNode``\ s.
In Part 2, we'll implement the rest of the core of the `tree command`_:
printing the tree with `Box Drawing`_ characters.

.. _Part 1:
    /blog/...
.. _tree command:
    https://en.wikipedia.org/wiki/Tree_(command)
.. _Box Drawing:
    https://www.compart.com/en/unicode/block/U+2500

Let's take a look at some output from ``tree``::

    .
    ├── alloc.rs
    ├── ascii.rs
    ├── os
    │   ├── wasi
    │   │   ├── ffi.rs
    │   │   ├── mod.rs          ➊
    │   │   └── net             ➋
    │   │       └── mod.rs
    │   └── windows
    │       ├── ffi.rs          ➌
    │       ├── fs.rs
    │       ├── io
    │       │   └── tests.rs
    │       ├── mod.rs
    │       └── thread.rs
    ├── personality
    │   ├── dwarf
    │   │   ├── eh.rs
    │   │   ├── mod.rs
    │   │   └── tests.rs
    │   ├── emcc.rs
    │   └── gcc.rs
    └── personality.rs

The first thing that we notice is that
most entries at any level, such as ➊,
are preceded by ``├──``,
while the last entry, ➋, is preceded by ``└──``.
This article__ about building a directory tree generator
in Python calls them the *tee* and *elbow* connectors,
and I'm going to use that terminology.

The second thing we notice is that there are
multiple *prefixes* before the connectors,
either :literal:`│  \ ` (*pipe*) or 
:literal:`\    \ ` (*space*),
one prefix for each level.
The rule is that children of a last entry,
such as ``os/windows`` ➌, get the space prefix,
while children of other entries,
such as ``os/wasi`` or ``personality``,
get the pipe prefix.

For both connectors and prefixes,
the last entry at a particular level gets special treatment.

__ https://realpython.com/directory-tree-generator-python/


The ``print_tree`` function
===========================

A classic pattern with recursion is to create a pair of functions:
an outer public function that calls a private helper function
with the initial set of parameters to visit recursively.

Our ``print_tree`` function uses an inner ``visit`` function
to recursively do almost all of the work.

.. code-block:: rust

    pub fn print_tree(root: &str, dir: &Directory) {
        const OTHER_CHILD: &str = "│   ";   // prefix: pipe
        const OTHER_ENTRY: &str = "├── ";   // connector: tee
        const FINAL_CHILD: &str = "    ";   // prefix: no more siblings
        const FINAL_ENTRY: &str = "└── ";   // connector: elbow

        println!("{}", root);                                           ➊
        let (d, f) = visit(dir, "");
        println!("\n{} directories, {} files", d, f);

        fn visit(node: &Directory, prefix: &str) -> (usize, usize) {    ➋
            let mut dirs: usize = 1; // counting this directory         ➌
            let mut files: usize = 0;
            let mut count = node.entries.len();                         ➍
            for entry in &node.entries {
                count -= 1;
                let connector =
                    if count == 0 { FINAL_ENTRY } else { OTHER_ENTRY }; ➎
                match entry {
                    FileTree::DirNode(sub_dir) => {                     ➏
                        println!("{}{}{}", prefix, connector, sub_dir.name);
                        let new_prefix = format!(                       ➐
                            "{}{}",
                            prefix,
                            if count == 0 { FINAL_CHILD } else { OTHER_CHILD }
                        );
                        let (d, f) = visit(&sub_dir, &new_prefix);      ➑
                        dirs += d;
                        files += f;
                    }
                    FileTree::LinkNode(symlink) => {
                        println!(
                            "{}{}{} -> {}", prefix, connector,
                            symlink.name, symlink.target);
                        files += 1;
                    }
                    FileTree::FileNode(file) => {
                        println!("{}{}{}", prefix, connector, file.name);
                        files += 1;
                    }
                }
            }
            (dirs, files)                                               ➒
        }
    }

1. The outer function, ``print_tree``,
   simply prints the name of the root node on a line by itself;
   calls the inner ``visit`` function with the ``dir`` node and an empty prefix;
   and finally prints the number of directories and files visited.
   This is for compatibility with the output of ``tree``.
2. The inner ``visit`` takes two parameters:
   ``node``, a ``Directory``, and
   ``prefix``, a string which is initially empty.
3. Keep track of the number of ``dirs`` and ``files`` seen at this level
   and in sub-directories.
4. We count downwards from the number of entries in this directory to zero.
   When ``count`` is zero, we are on the last entry, which gets special treatment.
5. Compute the connector,
   ``└──`` (*elbow*) for the last entry;
   ``├──`` (*tee*) otherwise.
6. Match the ``FileTree::DirNode`` variant
   and destructure__ the value into ``sub_dir``, a ``&Directory``.
7. Before recursively visiting a sub-directory,
   we compute a new prefix,
   by appending the appropriate sub-prefix to the current prefix.
   If there are further entries (``count > 0``),
   the sub-prefix for the current level is :literal:`│  \ ` (*pipe*);
   otherwise, it's :literal:`\    \ ` (*spaces*).
8. Call ``visit`` recursively, then add to the
   running totals of ``dirs`` and ``files``.
9. ``visit`` returns a tuple of the counts of directories and files
   that were recursively visited.

One subtlety that is not obvious from the above is that
``OTHER_CHILD`` actually contains two `non-breaking spaces`__:

.. code-block:: rust

    const OTHER_CHILD: &str = "│\u{00A0}\u{00A0} "; // prefix: pipe

This is for compatibility with the output of ``tree``:

.. code-block:: bash

    $ diff <(cargo run -q -- ./tests) <(tree ./tests) && echo "no difference"
    no difference

Using `process substitution`__ to generate two different inputs for ``diff``.

__ https://doc.rust-lang.org/reference/patterns.html#destructuring
__ https://en.wikipedia.org/wiki/Non-breaking_space
__ /blog/2022/01/31/DiffFileFragment.html


The ``main`` function
=====================

Let's tie it all together.

.. code-block:: rust

    fn main() -> io::Result<()> {
        let root = env::args().nth(1).unwrap_or(".".to_string());   ➊
        let dir: Directory = dir_walk(                              ➋
            &PathBuf::from(root.clone()),                           ➌
            is_not_hidden,
            sort_by_name)?;                                         ➍
        print_tree(&root, &dir);                                    ➎
        Ok(())                                                      ➏
    }

1. The simplest possible way to get a single, optional command-line argument.
   If omitted, we default to ``.``, the current directory.
   For more sophisticated argument parsing, we could use Clap__.
2. Use ``dir_walk`` from `Part 1`_ to recursively build
   a directory of ``FileTree`` nodes.
3. Create a ``PathBuf`` from ``root``, a string;
   ``clone`` is needed because ``PathBuf::from`` takes ownership of the string buffer.
   Use the ``is_not_hidden`` filter and the ``sort_by_name`` comparator from `Part 1`_.
4. The `postfix question mark operator`__, ``?``, is used to propagate errors.
5. Let ``print_tree`` draw the diagram.
6. Return the ``Ok`` unit__ result to indicate success.

__ https://docs.rs/clap/latest/clap/
__ https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-question-mark-operator
__ https://doc.rust-lang.org/std/primitive.unit.html 


Baum
====

You can find the Baum_ source code on GitHub.

.. _Baum:
    https://github.com/georgevreilly/baum

In Part 3, we'll discuss testing.


Resources
=========

* `Official tree source`_:
  The actual source for ``tree``, written in old-school C.
* `Draw a Tree Structure With Only CSS`_:
  Use CSS to draw links in nested, unordered lists.
* `Build a Python Directory Tree Generator for the Command Line`_.
* Kevin Newton has implemented `Tree in Multiple Languages`_.
* Tre_ is a modern alternative to ``tree`` in Rust.



.. _Draw a Tree Structure With Only CSS:
    https://two-wrongs.com/draw-a-tree-structure-with-only-css.html
.. _Build a Python Directory Tree Generator for the Command Line:
    https://realpython.com/directory-tree-generator-python/
.. _Tree in Multiple Languages:
    https://github.com/kddnewton/tree
.. _Tre:
    https://github.com/dduan/tre
.. _Official tree source: 
    https://github.com/Old-Man-Programmer/tree/
