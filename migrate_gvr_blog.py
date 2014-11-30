#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import fnmatch
import os
import re


def parse_args():
    parser = argparse.ArgumentParser(
        description="Migrate George's blog from DasBlog reStructuredText to Acrylamid")
    parser.set_defaults(
        blog_dir="~/stuff/Writing/blog/gvr",
        dry_run=False,
        limit=None,
        )

    parser.add_argument(
        'blog-dir', nargs="?",
        help="an INI file specifying the database\n(Default: '%(default)s'")
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be generated.")
    parser.add_argument(
        '--limit', '-l',
        type=int,
        help="Process this many receipts (default: all).")

    args = parser.parse_args()
    args.blog_dir = os.path.abspath(os.path.expanduser(args.blog_dir))
    return args


def walk_tree(dir, includes=None, excludes=None):
    # Adapted from http://stackoverflow.com/a/5141829/6364
    # Transform glob patterns to regular expressions
    includes = r'|'.join([fnmatch.translate(x) for x in includes])
    excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

    for root, dirs, files in os.walk(dir):
        # exclude dirs
        dirs[:] = [os.path.join(root, d) for d in dirs]
        dirs[:] = [d for d in dirs if not re.match(excludes, d)]

        # exclude/include files
        files = [os.path.join(root, f) for f in files]
        files = [f for f in files if not re.match(excludes, f)]
        files = [f for f in files if re.match(includes, f)]

        for fname in files:
            yield fname


def tail(fp, window=20):
    """Returns the last `window` lines of file `fp` as a list."""
    # Adapted from http://stackoverflow.com/a/7047765/6364
    if window == 0:
        return []
    BUFSIZ = 1024
    fp.seek(0, os.SEEK_END)
    bytes = fp.tell()
    size = window + 1
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if bytes - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            fp.seek(block * BUFSIZ, os.SEEK_END)
            # read BUFFER
            data.insert(0, fp.read(BUFSIZ))
        else:
            # file too small, start from beginning
            fp.seek(0, os.SEEK_SET)
            # only read what was not read
            data.insert(0, fp.read(bytes))
        lines_found = data[0].count('\n')
        size -= lines_found
        bytes -= BUFSIZ
        block -= 1
    return ''.join(data).splitlines()[-window:]


def read_permalink(filename):
    PERMALINK = '.. _permalink:'
    with open(filename) as fp:
        last_lines = tail(fp, 10)
        data = ''.join(last_lines)
        i = data.find(PERMALINK)
        if i >= 0:
            link = data[i + len(PERMALINK):].strip().split()[0]
            return link
    return None


if __name__ == '__main__':
    args = parse_args()
    blog_files = walk_tree(args.blog_dir, includes=('*.txt', '*.rst'), excludes=('*.gif',))
    for fname in list(blog_files)[:args.limit]:
        print fname, read_permalink(fname)