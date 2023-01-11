---
title: "Review: Backbone.js Testing"
date: "2013-10-24"
permalink: "/blog/2013/10/24/ReviewBackbonejsTesting.html"
tags: [books, reviews, programming, javascript]
---



.. image:: https://images-na.ssl-images-amazon.com/images/P/178216524X.01.MZZZZZZZ.jpg
    :alt: Backbone.js Testing
    :target: http://www.packtpub.com/backbonejs-testing/book
    :class: right-float

| Title: Backbone.js Testing
| Author: Ryan Roemer
| Rating: ★ ★ ★ ★ ½
| Publisher: Packt
| Copyright: 2013
| ISBN: `178216524X <http://www.amazon.com/dp/178216524X/?tag=georgvreill-20>`_
| Pages: 168
| Keywords: programming, testing, javascript, backbone, mocha, chai, sinon
| Reading period: October 2013

`Backbone.js Testing`_ is a short, dense introduction
to testing JavaScript applications with three testing libraries,
`Mocha`_, `Chai`_, and `Sinon.JS`_.
Although the author uses a sample application
of a personal note manager written with `Backbone.js`_
throughout the book, much of the material
would apply to any JavaScript client or server framework.

`Mocha`_ is a test framework that can be executed in the browser or by `Node.js`_,
which runs your tests.
`Chai`_ is a framework-agnostic `TDD`_/\ `BDD`_ assertion library.
`Sinon.JS`_ provides standalone test spies, stubs and mocks for JavaScript.
They complement each other and the author does a good job of explaining
when and how to use each.

I've written a lot of tests in Python (unittest_ and mock_, primarily)
and C# (NUnit_), but my experience with JavaScript unit testing
was both limited and years out of date.
The JavaScript ecosystem continues to evolve rapidly,
with new browser frameworks and Node packages springing up everywhere.
JavaScript has some particular challenges in testing—\
notably, the DOM, asynchrony, and callbacks.
Mocha, Chai, and Sinon meet those challenges, though they can't take away all the pain.

The author describes how to test Backbone models, views, and collections;
dealing with asynchrony;
provides useful testing heuristics, including isolating components to reduce dependencies;
when to use stubs and mocks and fake servers;
and test automation with PhantomJS_.
He does not, however, teach you Backbone.js itself; for that, you'll need another book.

There are a few areas which I thought were dealt with too lightly.
There's no real discussion of `Test-driven_development`_ or
`Behavior-driven_development`_,
which provide the intellectual foundations of much of the book.
Nor does he have much to say about testability_ and how to make
`legacy code`_ more testable.
The sample Notes app has plenty of testing seams_
(much of this falls naturally out of the architecture of Backbone);
other people's apps are not so lucky.
The chapter on automation is extremely terse—it could be expanded into a very large book!—\
but it does provide useful indicators to many areas for exploration.

I learned a lot from this book and I have no hesitation in recommending it.

Disclosure: Thanks to `Ryan Roemer`_ and Packt for a review copy of this book.

.. _Backbone.js Testing: http://www.packtpub.com/backbonejs-testing/book
.. _Backbone.js: http://backbonejs.org/
.. _Mocha: http://visionmedia.github.io/mocha/
.. _Chai: http://chaijs.com/
.. _Sinon.JS: http://sinonjs.org/
.. _Node.js: http://nodejs.org/
.. _Test-driven_development:
.. _TDD: http://en.wikipedia.org/wiki/Test-driven_development
.. _Behavior-driven_development:
.. _BDD: http://en.wikipedia.org/wiki/Behavior-driven_development
.. _unittest: http://docs.python.org/2/library/unittest.html
.. _mock: http://www.voidspace.org.uk/python/mock/
.. _NUnit: http://www.nunit.org/
.. _PhantomJS: http://phantomjs.org/
.. _testability: http://en.wikipedia.org/wiki/Software_testability
.. _legacy code: http://en.wikipedia.org/wiki/Legacy_code
.. _seams: http://googletesting.blogspot.com/2008/08/by-miko-hevery-so-you-decided-to.html
.. _Ryan Roemer: http://backbone-testing.com/
.. _permalink:
    /blog/2013/10/24/ReviewBackbonejsTesting.html
