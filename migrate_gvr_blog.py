#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

import six
import argparse
from datetime import datetime
import fnmatch
import hashlib
import io
import json
import os
import re
import shutil
from six.moves.urllib.parse import urlsplit
from collections import OrderedDict

#BASE_URL = "http://www.georgevreilly.com/blog"
BASE_URL = "/blog"


Verbose = False


def log(*args):
    if Verbose:
        print(*args)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Migrate George's blog from DasBlog reStructuredText to Acrylamid")
    parser.set_defaults(
        dasblog_dir="~/stuff/Writing/blog/gvr",
        dry_run=False,
        limit=None,
        base_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), "content")),
        blog_dir="blog",
        verbose=False,
    )

    parser.add_argument(
        'dasblog_dir', nargs="?",
        help="Where the old DasBlog content lives\n(Default: '%(default)s'")
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be generated.")
    parser.add_argument(
        '--limit', '-l',
        type=int,
        help="Process this many entries (default: all).")
    parser.add_argument(
        '--verbose', '-v',
        action="store_true",
        help="Be more verbose")

    args = parser.parse_args()

    args.dasblog_dir = os.path.abspath(os.path.expanduser(args.dasblog_dir))

    global Verbose
    Verbose = args.verbose

    return args


def read_permalink(filename):
    PERMALINK = ".. _permalink:"
    link = None
    with open(filename, "rb") as fp:
        last_lines = tail(fp, 10)
        data = ''.join(last_lines)
        i = data.find(PERMALINK)
        if i >= 0:
            try:
                link = data[i + len(PERMALINK):].strip().split()[0]
                date_parts = link.split('/')[2:5]
                if len(date_parts) < 3:
                    link = None
                else:
                    datetime.strptime("/".join(date_parts), "%Y/%m/%d")
            except Exception as e:
                print(filename, e)
                link = None
    return link


def walk_tree(dir, includes, excludes=None):
    """Walk a directory tree, including and excluding files and dirs by wildcards.

    Adapted (and fixed!) from http://stackoverflow.com/a/5141829/6364
    """
    # Transform glob patterns to regular expressions
    includes_re = re.compile('|'.join(
        [fnmatch.translate(x) for x in includes]))
    excludes_re = re.compile('|'.join(
        [fnmatch.translate(x) for x in excludes]) if excludes else '$.')

    for top, dirs, files in os.walk(dir, topdown=True):
        # exclude directories by mutating `dirs`
        dirs[:] = sorted([d for d in dirs if not excludes_re.search(os.path.join(top, d))],
                         key=six.text_type.lower)

        # exclude/include files
        files = [os.path.join(top, f) for f in files]
        files = [f for f in files if not excludes_re.search(f)]
        files = [f for f in files if includes_re.search(f)]
        files = sorted(files, key=six.text_type.lower)

        for fname in files:
            yield fname


def tail(fp, window=20):
    """Returns the last `window` lines of file `fp` as a list."""
    # Adapted from http://stackoverflow.com/a/7047765/6364
    if window == 0:
        return []
    BUFSIZ = 1024
    fp.seek(0, os.SEEK_END)
    byte_count = fp.tell()
    size = window + 1
    block = -1
    data = []
    while size > 0 and byte_count > 0:
        if byte_count - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            fp.seek(block * BUFSIZ, os.SEEK_END)
            # read BUFFER
            line_bytes = fp.read(BUFSIZ)
        else:
            # file too small, start from beginning
            fp.seek(0, os.SEEK_SET)
            # only read what was not read
            line_bytes = fp.read(byte_count)
        data.insert(0, line_bytes)
        lines_found = len([c for c in line_bytes if c == b'\n'])
        size -= lines_found
        byte_count -= BUFSIZ
        block -= 1
    data = b''.join(data).splitlines()
    return [l.decode("utf-8") for l in data[-window:]]


def link_path(url):
    return url[len(BASE_URL):]
    u = urlsplit(url)
    return u.path


def dump_links(permalink_titles, filename_links):
    permalinks = set(permalink_titles.keys())
    filelinks = set(filename_links.keys())

    orphaned_permalinks = permalinks - filelinks
    print("\n", len(orphaned_permalinks), "Orphaned Permalinks")
    return
    for f in orphaned_permalinks:
        print(f)

    orphaned_filelinks = filelinks - permalinks
    print("\n", len(orphaned_filelinks), "Orphaned File Links")
    for f in orphaned_filelinks:
        print(f)

    found_links = permalinks & filelinks
    print("\n", len(found_links), "Found links")
    for f in found_links:
        print(f, filename_links[f])


class ReMatcher(object):
    def __init__(self, value=None):
        self.value = value

    def match(self, re, line):
        self.value = re.match(line)
        return self.value

    def group(self, key):
        return self.value.group(key)


title_re = re.compile(r"^.. title:: (?P<title>.*)$")
tags_re = re.compile(r"^.. tags: (?P<tags>.*)$")
vim_re = re.compile(r"^.. vim:set.*")
emacs_re = re.compile(r"^.. -\*- .* -\*-")
image_content_binary_re = re.compile(r"(?P<directive>.. image::) +(?P<path>content/binary/.*)$")


def migrate_file(source_dir, base_dir, target_dir, fname, permalink):
    source_file = os.path.join(source_dir, fname)
    date_parts = permalink.split('/')[1:4]
    if len(date_parts) < 3:
        print("Need to fix", fname, date_parts)
        return
    subdirs = os.path.join(target_dir, *date_parts)
    target_file = os.path.join(subdirs, os.path.splitext(os.path.split(fname)[1])[0])

    data, title, tags, matcher = [], None, None, ReMatcher()
    with io.open(source_file, "r", encoding="utf8") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            if matcher.match(title_re, line):
                title = matcher.group('title').strip()
                continue
            elif vim_re.match(line) or emacs_re.match(line):
                continue
            elif matcher.match(image_content_binary_re, line):
                line = "{0} /{1}\n".format(matcher.group('directive'), matcher.group('path'))
            elif matcher.match(tags_re, line):
                tags = matcher.group('tags').strip()
                continue

            data.append(line)

    prolog = [
        title,
        "#" * len(title),
        "",
        ":date: {0}-{1}-{2}".format(*date_parts),
        ":permalink: /blog{0}".format(permalink.replace(".aspx", ".html")),
    ] + ([":tags: {0}".format(tags)] if tags else [])
    prolog = "\n".join(prolog) + "\n"
    epilog = ""

    write = False
    subdir_path = os.path.join(base_dir, subdirs)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)
        write = True
    target_file = os.path.join(base_dir, target_file + ".rst")
    target_data = (prolog + ''.join(data) + epilog).encode('utf-8')
    if not os.path.exists(target_file):
        write = True
    else:
        new_md5 = hashlib.md5(target_data).hexdigest()
        with open(target_file, "rb") as fp:
            old_data = fp.read()
        old_md5 = hashlib.md5(old_data).hexdigest()
        write = (old_md5 != new_md5)
#       if not write:
#           log("Not writing '{0}': old={1}, new={2}".format(source_file, old_md5, new_md5))

    if write:
        print("'{0}' -> '{1}' ({2})".format(source_file, target_file, permalink))

        with io.open(target_file, "w", encoding="utf8") as fp:
            fp.write(prolog)
            for line in data:
                fp.write(line)
            fp.write(epilog)
        shutil.copystat(source_file, target_file)


def migrate_files(args, filename_links):
    for permalink, fname in filename_links.items():
        migrate_file(args.dasblog_dir, args.base_dir, args.blog_dir, fname, permalink)

    # Copy content/binary
    cb_src = os.path.join(args.dasblog_dir, "content")
    cb_dst = os.path.abspath(os.path.join(args.base_dir, "..", "media", "content"))
    if os.path.exists(cb_dst):
        shutil.rmtree(cb_dst)
    shutil.copytree(cb_src, cb_dst, ignore=lambda src, names: set([".DS_Store"]))


if __name__ == '__main__':
    args = parse_args()
    with io.open(os.path.join(os.path.dirname(__file__), "permalinks.json"), "r", encoding="utf8") as fp:
        permalink_titles = json.load(fp)

    filename_links = {}
    blog_files = walk_tree(args.dasblog_dir, includes=('*.txt', '*.rst'), excludes=('*.gif',))
    filenames = list(blog_files)[:args.limit]

    for fname in filenames:
        link = read_permalink(fname)
        if link:
            link = link_path(link)
            filename_links[link] = fname
        elif args.verbose:
            print("No link for {}".format(fname))

#   dump_links(permalink_titles, filename_links)
    migrate_files(args, filename_links)
