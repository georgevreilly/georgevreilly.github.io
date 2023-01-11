---
title: "SQLAlchemy got me Killed"
date: "2016-07-14"
permalink: "/blog/2016/07/14/SQLAlchemyGotMeKilled.html"
tags: [python, til]
---



I ran a script this afternoon that died mysteriously without any output.
It was using SQLAlchemy__ to query all the rows from a large table
so that they could be transformed into `JSON Lines`__ to be loaded into Elasticsearch.
When I reran my script,
I noticed this time that something had printed ``Killed`` at the very end.

A little research convinced me that the `OOM Killer`__ was the likely assassin.
I looked in ``/var/log/kern.log``
and I found that my process had used up almost all of the 8GB on this system
before being killed.

The query had to be the problem.
A little more research led me to augment my query with `yield_per`__,
which batched the results,
instead of fetching everything into memory at once.
There are various caveats to using ``yield_per``;
none applied here.

__  http://www.sqlalchemy.org/
__  http://jsonlines.org/
__  http://stackoverflow.com/questions/726690/who-killed-my-process-and-why
__  http://stackoverflow.com/questions/1145905/sqlalchemy-scan-huge-tables-using-orm

.. _permalink:
    /blog/2016/07/14/SQLAlchemyGotMeKilled.html
