#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import codecs
import fnmatch
import hashlib
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
        dasblog_dir="~/stuff/Writing/blog/gvr",
        dry_run=False,
        limit=None,
        base_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), "content")),
        blog_dir="blog",
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

    args = parser.parse_args()
    args.dasblog_dir = os.path.abspath(os.path.expanduser(args.dasblog_dir))
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
                link = link.decode('utf8')
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


class ReMatcher(object):
    def __init__(self, value=None):
        self.value = value

    def match(self, re, line):
        self.value = re.match(line)
        return self.value

    def group(self, key):
        return self.value.group(key)


title_re = re.compile(ur"^.. title:: (?P<title>.*)$")
vim_re = re.compile(ur"^.. vim:set.*")
emacs_re = re.compile(ur"^.. -\*- .* -\*-")
image_content_binary_re = re.compile(ur"(?P<directive>.. image::) +(?P<path>content/binary/.*)$")


def migrate_file(source_dir, base_dir, target_dir, fname, permalink):
    source_file = os.path.join(source_dir, fname)
    date_parts = permalink.split('/')[1:4]
    if len(date_parts) < 3:
        print "Need to fix", fname, date_parts
        return
    subdirs = os.path.join(target_dir, *date_parts)
    target_file = os.path.join(subdirs, os.path.splitext(os.path.split(fname)[1])[0])
    write = False

    data, title, matcher = [], None, ReMatcher()
    with codecs.open(source_file, "r", encoding="utf8") as fp:
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
            data.append(line)

    prolog = u"\n".join([
        title,
        u"#" * len(title),
        u"",
        u":date: {0}-{1}-{2}".format(*date_parts),
        u":permalink: /blog{0}".format(permalink.replace(u".aspx", u".html")),
        u""
    ])
    epilog = u""

    subdir_path = os.path.join(base_dir, subdirs)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)
        write = True
    target_file = os.path.join(base_dir, target_file + u".rst")
    target_data = (prolog + ''.join(data) + epilog).encode('utf-8')
    if not os.path.exists(target_file):
        write = True
    else:
        new_md5 = hashlib.md5(target_data)
        with open(target_file) as fp:
            old_data = fp.read()
            old_md5 = hashlib.md5(old_data)
            write = (old_md5.hexdigest() != new_md5.hexdigest())

    if write:
        print u"'{0}' -> '{1}' ({2})".format(source_file, target_file, permalink)

        with codecs.open(target_file, "w", encoding="utf8") as fp:
            fp.write(prolog)
            for line in data:
                fp.write(line)
            fp.write(epilog)
        shutil.copystat(source_file, target_file)


def migrate_files(args, filename_links):
    for permalink, fname in filename_links.iteritems():
        migrate_file(args.dasblog_dir, args.base_dir, args.blog_dir, fname, permalink)
    # Copy content/binary
    cb_src = os.path.join(args.dasblog_dir, "content")
    cb_dst = os.path.abspath(os.path.join(args.base_dir, "..", "media", "content"))
    if os.path.exists(cb_dst):
        shutil.rmtree(cb_dst)
    shutil.copytree(cb_src, cb_dst, ignore=lambda src, names: set([".DS_Store"]))


if __name__ == '__main__':
    args = parse_args()
    with codecs.open(os.path.join(os.path.dirname(__file__), "permalinks.json"), "r", encoding="utf8") as fp:
        permalink_titles = json.load(fp)

    filename_links = {}
    blog_files = walk_tree(args.dasblog_dir, includes=('*.txt', '*.rst'), excludes=('*.gif',))
    filenames = list(blog_files)[:args.limit]

    for fname in filenames:
        link = read_permalink(fname)
        if link:
            link = link_path(link)
            filename_links[link] = fname

#   dump_links(permalink_titles, filename_links)
    migrate_files(args, filename_links)

