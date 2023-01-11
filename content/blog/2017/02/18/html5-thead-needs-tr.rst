---
title: "HTML5 tables require tr inside thead"
date: "2017-02-18"
permalink: "/blog/2017/02/18/HTML5TablesRequireTrInsideThead.html"
tags: [html, til]
---



When I learned HTML tables back in the 90s,
at some point I discovered the ``<thead>`` element
for grouping the ``<th>`` column headers.
What I missed was there should be a ``<tr>`` element between the two.
In other words, a well-formed HTML table with a header looks like this:

.. code-block:: html

    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Value</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>USERNAME</td>
                <td>John.Smith</td>
                <td>2017-02-18T23:47</td>
            </tr>
        </tbody>
    </table>

and not:

.. code-block:: html

    <table>
        <thead>
            <th>Name</th>
            <th>Value</th>
            …

The latter form—``<thead>`` directly enclosing ``<th>``\ s—\
had always worked for me.
Until yesterday when I ran afoul of an HTML5 validator on a remote API,
which simply would not let me proceed until I wrapped my ``<th>`` cells with a ``<tr>``.

Who knew?

.. _permalink:
    /blog/2017/02/18/HTML5TablesRequireTrInsideThead.html
