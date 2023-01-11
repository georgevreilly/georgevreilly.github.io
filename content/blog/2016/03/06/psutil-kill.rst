---
title: "psutil kill"
date: "2016-03-06"
permalink: "/blog/2016/03/06/psutil-kill.html"
tags: [python, til]
---



From Python, I needed to find a process
that was performing SSH tunneling on port 8080
and kill it.

The following works in Bash:

.. code:: bash

    ps aux | grep [s]sh.*:8080 | awk '{print $2}' | xargs kill -9

The ``grep [s]sh`` trick ensures that the ``grep`` command itself
won't make it through to ``awk``.

Here's what I came up with in Python using psutil_:

.. code:: python

    def kill_port_forwarding(host_port):
        ssh_args = ["-f", "-N", "-L", "{0}:localhost:{0}".format(host_port)]
        for process in psutil.process_iter():
            try:
                if process.name().endswith('ssh'):
                    if process.cmdline()[-len(ssh_args):] == ssh_args:
                        process.kill()
            except psutil.NoSuchProcess:
                pass

Obviously, the process filtering is more rigorous in the Python version.

.. _psutil:
    http://pythonhosted.org/psutil/

.. _permalink:
    /blog/2016/03/06/psutil-kill.html
