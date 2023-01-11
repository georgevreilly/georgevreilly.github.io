---
title: "Sharing Dotfiles between Windows and \\*nix"
date: "2008-05-14"
permalink: "/blog/2008/05/14/SharingDotfilesBetweenWindowsAndNix.html"
tags: [programming, windows, linux, mac, til]
---



.. image:: /content/binary/shared-dotfiles.png
    :alt: Sharing Dotfiles between Windows and \*nix
    :class: right-float

Tomas Restrepo wrote a post about
`sharing dotfiles between Windows and Ubuntu`_,
specifically about sharing ``.vimrc`` (Linux) and ``_vimrc`` (Windows)
and the ``.vim`` (Linux) and ``vimfiles`` (Windows) directories.

I have a different solution.
On Windows, my ``C:\AutoExec.bat`` includes::

    set HOME=C:\gvr
    set VIM=C:\Vim
    set VIMDIR=%VIM%\vim71
    set EDITOR=%VIMDIR%\gvim.exe
    set PATH=%PATH%;C:\Win32app;C:\GnuWin32\bin;C:\UnxUtils;C:\SysInternals;C:\Python25\Scripts

``%HOME%`` (``C:\gvr``) contains ``_vimrc``, ``vimfiles``,
and other stuff accumulated over many years.
This directory is stored in a personal Subversion repository at `DevjaVu`_.
All my Vim files are stored with Unix LF endings, not Windows CR-LFs,
so that they'll work on my Mac OS X and Linux boxen.
I play some games with ``if has("win32")`` and
``if has('gui_macvim')`` to ensure that my ``_vimrc``
works cross-platform.

On my \*nix boxes, the ``gvr`` folder lives under my home directory at ``~/gvr``,
and ``~/.vimrc`` and ``~/.vim`` are symlinks::

    $ ln -s ~/gvr/_vimrc ~/.vimrc
    $ ln -s ~/gvr/vimfiles/ ~/.vim

In addition, the dotfiles that I keep in SVN are stored locally in
``~/gvr/dotfiles`` without a leading period in their names,
which makes them easy to see::

    $ ln -s ~/gvr/dotfiles/bashrc ~/.bashrc

This arrangement works well for me.

.. _sharing dotfiles between Windows and Ubuntu:
    http://www.winterdom.com/weblog/2008/05/09/SharingDotfilesBetweenWindowsAndUbuntu.aspx
.. _DevjaVu:
    http://www.devjavu.com/

.. _permalink:
    /blog/2008/05/14/SharingDotfilesBetweenWindowsAndNix.html
