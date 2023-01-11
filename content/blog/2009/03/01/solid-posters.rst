---
title: "SOLID Development Priniciples – in Motivational Posters"
date: "2009-03-01"
permalink: "/blog/2009/03/01/SOLIDDevPriniciples-MotivationalPosters.html"
tags: [programming]
---



.. image:: https://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/SOLID_5F00_6EC97F9C.jpg
    :alt: SOLID Development Priniciples – in Motivational Posters
    :target: http://www.lostechies.com/blogs/derickbailey/archive/2009/02/11/solid-development-principles-in-motivational-pictures.aspx
    :width: 300
    :class: right-float

Derick Bailey put together a set of `Motivational Posters`_
to illustrate the `SOLID principles`_.
SOLID is a set of principles that help guide OO code
towards greater testability_.
They increase cohesion_ and reduce dependencies, hence, coupling.


.. raw:: html

    <br style="clear: both" />

.. image:: https://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/SingleResponsibilityPrinciple2_5F00_71060858.jpg
    :alt: Single Responsibility Principle — A class should have one, and only one, reason to change
    :target: http://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/SingleResponsibilityPrinciple2_5F00_71060858.jpg
    :width: 300
    :class: left-float

**Single Responsibility Principle** — A class should have one, and only one, reason to change

Ideally, a class or a function will do only one thing and do it well,
in only a few lines.

Recently, I refactored two large functions.
One function proxied an HTTP request: it had to
selectively copy request headers, construct other headers,
copy the request body, make the request, handle exceptions,
selectively copy response headers, construct other headers,
and copy the request body.
The preceding sentence tells you what the resulting functions looked like.

The other function made a series of related database queries,
constructed some intermediate data structures,
then performed some joins,
to build an object graph.
Each query got its own function
as did each builder of an intermediate data structure.
The top-level function became eight simple lines
and is now comprehensible.


.. raw:: html

    <br style="clear: both" />

.. image:: https://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/OpenClosedPrinciple2_5F00_2C596E17.jpg
    :alt: Open-Closed Principle — You should be able to extend a class's behavior, without modifying it
    :target: http://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/OpenClosedPrinciple2_5F00_2C596E17.jpg
    :width: 300
    :class: right-float

**Open-Closed Principle** — You should be able to extend a class's behavior, without modifying it

The classic formulation of the Open-Closed Principle is:

    Software Entities (classes, modules, functions, etc.)
    should be Open for Extension, but Closed for Modification.

That's pithy—and confusing.
Let me try restating it:
don't change existing code when you want to add new code.

If you've designed your system with abstract base classes and interfaces,
then it's generally possible to achieve this.
If you have to add new if-clauses or adjust ``switch`` statements
in existing code,
your code is not closed for modification.

Think “pluggable” or the `Template Method`_ and `Strategy`_ patterns.


.. raw:: html

    <br style="clear: both" />

.. image:: https://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/LiskovSubtitutionPrinciple_5F00_52BB5162.jpg
    :alt: Liskov Substitution Principle — Derived classes must be substitutable for their base classes
    :target: http://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/LiskovSubtitutionPrinciple_5F00_52BB5162.jpg
    :width: 300
    :class: left-float

**Liskov Substitution Principle** — Derived classes must be substitutable for their base classes



.. raw:: html

    <br style="clear: both" />

.. image:: https://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/InterfaceSegregationPrinciple_5F00_60216468.jpg
    :alt: Interface Segregation Principle — Make fine grained interfaces that are client specific
    :target: http://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/InterfaceSegregationPrinciple_5F00_60216468.jpg
    :width: 300
    :class: clear-both right-float

**Interface Segregation Principle** — Make fine grained interfaces that are client specific

*italic*



.. raw:: html

    <br style="clear: both" />

.. image:: https://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/DependencyInversionPrinciple_5F00_0278F9E2.jpg
    :alt: Dependency Inversion Principle — Depend on abstractions, not on concretions
    :target: http://www.lostechies.com/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/derickbailey/DependencyInversionPrinciple_5F00_0278F9E2.jpg
    :width: 300
    :class: left-float

**Dependency Inversion Principle** — Depend on abstractions, not on concretions

.. _Motivational Posters:
    http://www.lostechies.com/blogs/derickbailey/archive/2009/02/11/solid-development-principles-in-motivational-pictures.aspx
.. _SOLID principles:
    http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod
.. _davesquared's explanation of SOLID:
    http://davesquared.blogspot.com/2009/01/introduction-to-solid-principles-of-oo.html
.. _testability:
    http://blog.scottbellware.com/2009/01/good-design-is-easily-learned.html
.. _cohesion:
    http://en.wikipedia.org/wiki/Cohesion_(computer_science)
    http://www.appistry.com/blogs/michael/openclose-principle-and-dependency-inversion-principle-ndash-two-sides-same-coin
.. _Template Method:
    http://en.wikipedia.org/wiki/Template_method_pattern
.. _Strategy:
    http://en.wikipedia.org/wiki/Strategy_pattern
.. _Software Development is not a Jenga game:
    http://blog.fohjin.com/blog/2009/2/26/Software_Development_is_not_a_Jenga_game

.. _permalink:
    /blog/2009/03/01/SOLIDDevPriniciples-MotivationalPosters.html
