---
title: "Running PyCharm on Yosemite"
date: "2015-01-25"
permalink: "/blog/2015/01/25/PyCharmYosemite.html"
tags: [python, mac, vim, til]
---



.. image:: /content/binary/pycharm4-splash.png
    :alt: PyCharm
    :target: https://www.jetbrains.com/pycharm/
    :class: right-float

I did a `clean install of OS X 10.10`_ on my home laptop a week ago.
I tried to launch PyCharm_ 4.0.4 on it today.
It immediately failed. Every time.

When I looked in the System Console, I saw::

    1/25/15 7:46:00.557 PM pycharm[1160]: No matching VM found.
    1/25/15 7:46:00.711 PM com.apple.xpc.launchd[1]: (com.jetbrains.pycharm.58252[1160]) Service exited with abnormal code: 1

The JetBrains website wasn't very helpful when I looked there.
In time, I found a `StackOverflow answer`_ that put me on the right track
(and reminded me that I had previously solved this problem about a year ago, at work).
PyCharm and some of the other JetBrains IDEs require JDK 1.6,
as there are a number of `problems with JDK 1.7 and 1.8`_.
After I downloaded and installed `Apple's Java 6`_, PyCharm ran without further problems.

At work, we all use the PyCharm IDE for Python development,
even those of us who are diehard Vim or Emacs users.
It does a great job of helping you write and debug Python projects.
The IdeaVim_ plugin does an acceptable job of emulating Vim keybindings.


.. _clean install of OS X 10.10:
    /blog/2015/01/17/YosemiteCleanInstall.html
.. _PyCharm:
    https://www.jetbrains.com/pycharm/
.. _StackOverflow answer:
    http://stackoverflow.com/questions/26438628/crash-jetbrains-ide-with-yosemite-mac-osx-webstorm-intellij
.. _problems with JDK 1.7 and 1.8:
    https://intellij-support.jetbrains.com/entries/27854363-IDE-doesn-t-start-after-updating-to-Mac-OS-Yosemite-or-Mavericks
.. _Apple's Java 6:
    http://support.apple.com/kb/DL1572
.. _IdeaVim:
    https://github.com/JetBrains/ideavim

.. _permalink:
    /blog/2015/01/25/PyCharmYosemite.html
