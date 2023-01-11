---
title: "ssh IdentitiesOnly"
date: "2016-04-30"
permalink: "/blog/2016/04/30/SSHIdentitiesOnly.html"
tags: [ssh]
---



If you get "Too many authentication failures for username" when using SSH,
try using ``ssh -o 'IdentitiesOnly yes'`` instead.
By default, ssh-agent will promiscuously offer many identities.
Some hosts don't like that.

.. _permalink:
    /blog/2016/04/30/SSHIdentitiesOnly.html
