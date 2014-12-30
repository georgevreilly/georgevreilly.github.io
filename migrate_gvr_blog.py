#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import codecs
import fnmatch
import json
import os
import re
import urlparse
import shutil

BASE_URL = "http://www.georgevreilly.com/blog"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Migrate George's blog from DasBlog reStructuredText to Acrylamid")
    parser.set_defaults(
        blog_dir="~/stuff/Writing/blog/gvr",
        dry_run=False,
        limit=None,
        content_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), "content")),
        )

    parser.add_argument(
        'blog_dir', nargs="?",
        help="Where the old DasBlog content lives\n(Default: '%(default)s'")
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be generated.")
    parser.add_argument(
        '--limit', '-l',
        type=int,
        help="Process this many entries (default: all).")

    args = parser.parse_args()
    args.blog_dir = os.path.abspath(os.path.expanduser(args.blog_dir))
    return args


def read_permalink(filename):
    PERMALINK = ".. _permalink:"
    link = None
    with open(filename) as fp:
        last_lines = tail(fp, 10)
        data = ''.join(last_lines)
        i = data.find(PERMALINK)
        if i >= 0:
            try:
                link = data[i + len(PERMALINK):].strip().split()[0]
            except:
                print filename
    return link


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


def link_path(url):
    return url[len(BASE_URL):]
    u = urlparse.urlsplit(url)
    return u.path


def dump_links(permalink_titles, filename_links):
    permalinks = set(permalink_titles.keys())
    filelinks = set(filename_links.keys())

    orphaned_permalinks = permalinks - filelinks
    print "\n", len(orphaned_permalinks), "Orphaned Permalinks"
    return
    for f in orphaned_permalinks:
        print f

    orphaned_filelinks = filelinks - permalinks
    print "\n", len(orphaned_filelinks), "Orphaned File Links"
    for f in orphaned_filelinks:
        print f

    found_links = permalinks & filelinks
    print "\n", len(found_links), "Found links"
    for f in found_links:
        print f, filename_links[f]


title_re = re.compile(r"^.. title:: (?P<title>.*)$")
vim_re = re.compile(r"^.. vim:set.*")


def migrate_file(source_dir, target_dir, fname, permalink):
    source_file = os.path.join(source_dir, fname)
    date_parts = permalink.split('/')[1:4]
    if len(date_parts) < 3: return
    subdirs = os.path.join(target_dir, *date_parts)
    target_file = os.path.join(subdirs, os.path.splitext(os.path.split(fname)[1])[0])
    print source_file, "->", target_file + '.rst'

    data, title, i = [], None, 0
    with codecs.open(source_file, "r", encoding="utf8") as fp:
        while True:
            line = fp.readline(); i += 1
            if not line: break
            m = title_re.match(line)
            if m:
                title = m.group('title').strip()
            elif vim_re.match(line):
                continue
            else:
                data.append(line)

    prolog = '\n'.join([
        title,
        '#' * len(title),
        '',
        ":date: {0}-{1}-{2}".format(*date_parts),
        ":permalink: /blog/{0}.html".format(target_file),
        ''
    ])
    epilog = ''

    if not os.path.exists(subdirs):
        os.makedirs(subdirs)
    target_file = os.path.join(target_dir, target_file + '.rst')
    with codecs.open(target_file, "w", encoding="utf8") as fp:
        fp.write(prolog)
        for line in data:
            fp.write(line)
        fp.write(epilog)
    shutil.copystat(source_file, target_file)


def migrate_files(args, filename_links):
    for permalink, fname in filename_links.iteritems():
        migrate_file(args.blog_dir, args.content_dir, fname, permalink)


if __name__ == '__main__':
    args = parse_args()
    with codecs.open(os.path.join(os.path.dirname(__file__), "permalinks.json"), "r", encoding="utf8") as fp:
        permalink_titles = json.load(fp)

    filename_links = {}
    blog_files = walk_tree(args.blog_dir, includes=('*.txt', '*.rst'), excludes=('*.gif',))
    filenames = list(blog_files)[:args.limit]

    for fname in filenames:
        link = read_permalink(fname)
        if link:
            link = link_path(link)
            filename_links[link] = fname

#   dump_links(permalink_titles, filename_links)
    migrate_files(args, filename_links)

