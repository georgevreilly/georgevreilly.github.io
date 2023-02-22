---
title: "Compressing Tar Files in Parallel"
date: "2023-02-21"
permalink: "/blog/2023/02/21/CompressingTarFilesInParallel.html"
tags: [linux]
---

TL;DR: use ``tar -I pigz`` or ``tar -I lbzip2``
to compress large tar files much more quickly.

I investigated various ways of compressing a 7GiB tar file.

The built-in ``--gzip`` and ``--bzip2`` compression methods in GNU ``tar``
are single-threaded.
If you invoke an external compressor with ``--use-compress-program``,
you can get some huge reductions in compression time,
with slightly worse compression ratios.

You can use pigz__ as a parallel replacement for ``gzip``
and lbzip2__ as a parallel version of ``bzip2``.
Both of them will make heavy use of all the cores in your system,
greatly reducing the *real* time relative to the *user* time.

__ https://zlib.net/pigz/
__ https://linux.die.net/man/1/lbzip2

Single-threaded compression timing:
``gzip`` is a lot faster than ``bzip2``::

    $ time tar --bzip2 -cf huge-bzip2.tar.bz2 hugedir

    real    13m15.352s
    user    12m53.972s
    sys     0m16.029s

    $ time tar --gzip -cf huge-gzip.tar.gz hugedir

    real    5m56.489s
    user    5m30.271s
    sys     0m14.633s

``fast`` parallel compression timing:
``pigz`` is the clear winner::

    $ time tar --use-compress-program='lbzip2 --fast' \
        -cf huge-lbzip2-fast.tar.bz2 hugedir

    real    2m35.967s
    user    11m38.865s
    sys     0m26.981s

    $ time tar --use-compress-program='pigz --fast' \
        -cf huge-pigz-fast.tar.gz hugedir

    real    0m58.222s
    user    3m22.134s
    sys     0m17.357s

``best`` parallel compression timing:
``lbzip2`` is much quicker than ``pigz``::

    $ time tar --use-compress-program='lbzip2 --best' \
        -cf huge-lbzip2-best.tar.bz2 hugedir

    real    1m44.365s
    user    11m38.277s
    sys     0m13.551s

    $ time tar --use-compress-program='pigz --best' \
        -cf huge-pigz-best.tar.gz hugedir

    real    2m27.694s
    user    16m20.441s
    sys     0m16.092s

Compressed file sizes:
``bzip2`` family compresses better than ``gzip`` family;
``best`` is smaller than default compression level which is smaller than ``fast``::

    $ ls -lSr
    -rw-r--r-- 1 user group 2460438578 Feb 22 03:03 huge-lbzip2-best.tar.bz2
    -rw-r--r-- 1 user group 2461172874 Feb 22 03:19 huge-bzip2.tar.bz2
    -rw-r--r-- 1 user group 2689784220 Feb 22 03:00 huge-lbzip2-fast.tar.bz2
    -rw-r--r-- 1 user group 2691286852 Feb 22 03:06 huge-pigz-best.tar.gz
    -rw-r--r-- 1 user group 2704591997 Feb 22 03:25 huge-gzip.tar.gz
    -rw-r--r-- 1 user group 2950547862 Feb 22 03:01 huge-pigz-fast.tar.gz
    -rw-r--r-- 1 user group 7365222400 Feb 22 03:00 huge.tar

