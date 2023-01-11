---
title: "Creating a New PostgreSQL Database at RDS"
date: "2016-06-28"
permalink: "/blog/2016/06/28/CreatingANewPostgreSQLDatabaseAtRDS.html"
tags: [postgres, aws, til]
---



Many of us are guilty of saying “database” when we mean a database server or a DBMS.
A database is a collection of tables storing related data,
schemas, stored procs, and permissions.
Most database servers are capable of managing many databases simultaneously.

I needed to create a new PostgreSQL database at Amazon's RDS last week.
I already had an RDS instance; I needed a new database on that instance.
My Google searches turned up various recipes for creating a new RDS instance.

The following worked for me:

* SSH to an EC2 instance inside our VPC,
  so that I could connect to the RDS instance using `psql`_.
* Then run:

.. code:: bash

    psql --host=SOME-DBMS-HOST --dbname EXISTING_DB \
         --username=YOUR-USERNAME --password \
         --command="CREATE DATABASE new_database WITH OWNER some_owner"

* Using ``--password`` will prompt you for a password.
  If you've set up |~/.pgpass|_, you can specify ``--no-password`` instead.
* The critical part that was hard to figure out is that I had to specify 
  ``--dbname EXISTING_DB``.
  Otherwise, psql kept trying to connect to a database called YOUR-USERNAME.
* This should work for any PostgreSQL server, not just one hosted at RDS.

.. _psql:
    http://postgresguide.com/utilities/psql.html
.. |~/.pgpass| replace:: ``~/.pgpass``
.. _~/.pgpass:
    https://blog.sleeplessbeastie.eu/2014/03/23/how-to-non-interactively-provide-password-for-the-postgresql-interactive-terminal/

.. _Format text in a link in reStructuredText:
    http://stackoverflow.com/a/4836544/6364

.. _permalink:
    /blog/2016/06/28/CreatingANewPostgreSQLDatabaseAtRDS.html
