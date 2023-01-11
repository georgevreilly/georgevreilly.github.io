---
title: "psql: could not connect to server"
date: "2016-01-19"
permalink: "/blog/2016/01/19/PsqlCouldNotConnectToServer.html"
tags: [postgres, til]
---



I wanted to clean out my local PostgreSQL database today
so that I could restore a database dump taken on another system,
but every time I ran the psql_ utility, I got::

    psql: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

I tried various things, including restarting Postgres several times,
but nothing helped.
Eventually, I thought to look in ``/usr/local/var/postgres/server.log``,
where I saw several error messages indicating that Postgres 9.5
couldn't read data files created with 9.4.
At that point, I realized that during my most recent ``brew update; brew upgrade``,
Homebrew_ had upgraded my installation of
`Postgres from 9.4 to 9.5
<https://github.com/Homebrew/homebrew/blob/master/Library/Formula/postgresql.rb>`_.
A little investigation led me to this gist_.
Since I didn't care about the old database files,
I created a fresh ``/usr/local/var/postgres`` and ran ``initdb``.


.. _psql:
    http://postgresguide.com/utilities/psql.html
.. _Homebrew:
    http://brew.sh/
.. _gist:
    https://gist.github.com/joho/3735740

.. _permalink:
    /blog/2016/01/19/PsqlCouldNotConnectToServer.html
