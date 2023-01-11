---
title: "Flame Graphs and Flame Charts"
date: "2016-08-23"
permalink: "/blog/2016/08/23/FlameGraphsAndFlameCharts.html"
tags: [tech, performance, til]
---



.. image:: https://deliveryimages.acm.org/10.1145/2930000/2927301/gregg4.png
    :alt: Flame Graph
    :target: http://queue.acm.org/detail.cfm?id=2927301
    :class: right-float
    :width: 700

I was investigating the performance of a web app today,
and I spent some time looking at the `Flame Chart`__ visualization
in Chrome's profiling tools, which helped identify some problems.

Flame Charts are like Brendan Gregg's `Flame Graphs`__,
except that the charts are sorted by time,
while the graphs are sorted alphabetically.

Quoting from Gregg's recent `ACM Queue article`__:

    A flame graph has the following characteristics:

    * A stack trace is represented as a column of boxes,
      where each box represents a function (a stack frame).
    * The y-axis shows the stack depth,
      ordered from root at the bottom to leaf at the top.
      The top box shows the function
      that was on-CPU when the stack trace was collected,
      and everything beneath that is its ancestry.
      The function beneath a function is its parent.
    * The x-axis spans the stack trace collection.
      It does not show the passage of time,
      so the left-to-right ordering has no special meaning.
      The left-to-right ordering of stack traces
      is performed alphabetically on the function names,
      from the root to the leaf of each stack.
      This maximizes box merging:
      when identical function boxes are horizontally adjacent,
      they are merged.
    * The width of each function box shows the frequency
      at which that function was present in the stack traces,
      or part of a stack trace ancestry.
      Functions with wide boxes were more present in the stack traces
      than those with narrow boxes,
      in proportion to their widths.

Flame graphs are a clever, information-dense way to present computer performance.
I suspect Edward Tufte would approve.

__ https://addyosmani.com/blog/devtools-flame-charts/
__ http://www.brendangregg.com/flamegraphs.html
__ http://queue.acm.org/detail.cfm?id=2927301

.. _permalink:
    /blog/2016/08/23/FlameGraphsAndFlameCharts.html
