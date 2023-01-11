---
title: "Review: RESTful Web Services"
date: "2007-09-09"
permalink: "/blog/2007/09/09/ReviewRESTfulWebServices.html"
tags: [books, reviews, programming, rest]
---



.. image:: https://images-na.ssl-images-amazon.com/images/P/0596529260.01.MZZZZZZZ.jpg
    :alt: RESTful Web Services
    :target: http://www.elliottbaybook.com/product/info.jsp?isbn=0596529260
    :class: right-float

| Title: RESTful Web Services
| Author: Leonard Richardson, Sam Ruby
| Rating: ★ ★ ★ ★ ½ 
| Publisher: O'Reilly
| Copyright: 2007
| ISBN: `0596529260 <http://www.elliottbaybook.com/product/info.jsp?isbn=0596529260>`_
| Pages: 419
| Keywords: programming, web services, REST
| Reading period: 22 August-8 September 2007

Anyone who has attempted to build a Web Service
has come away scarred by the complexity of all the WS-\* standards.
Heavyweight standards that in many ways reinvent
earlier distributed object technologies like CORBA and DCOM,
providing Remote Procedure Calls over HTTP.
The promised interoperability hasn't really happened:
a web service built with one stack of tools may or may not be
consumable by another stack.

A movement has arisen in the last few years,
arguing for `RESTful`_ Web Services:
lighterweight services built on top of the REST architectural style
with simpler tools.

Big Web Services expose algorithms and method calls.
ROA (REST-oriented architecture) web services expose data (resources)
through the simple, uniform interface of HTTP.

I'm not going to try to explain REST or ROA here.
Poke around the `book site`_ and the `RESTwiki`_ if you want more details.

I think this book is destined to be a minor classic.
It explains the REST-oriented architecture very clearly.
It works through several plausible examples,
building services and clients in a variety of languages
(most notably Ruby on Rails).
It's not intimately tied to one software stack,
which means that the book will still be useful five years from now.
In part, that's because the tools support is fairly weak.
As far as I can tell, you're reduced to rolling your own ROA web service
from scratch in .NET, for example.

I haven't had to dig very deeply into WS-\*, fortunately,
but I haven't cared for what I've seen.
The authors don't spend a lot of time critiquing what they see as
the shortcomings of SOAP and the WS-\* standards,
but I'm not equipped to find fault in what they say.
What they do say, sounds reasonable to me.

Recommended.

.. _RESTful: RESTwiki_
.. _RESTwiki:
    http://rest.blueoxen.net/cgi-bin/wiki.pl
.. _book site:
    http://www.crummy.com/writing/RESTful-Web-Services/

.. _permalink:
    /blog/2007/09/09/ReviewRESTfulWebServices.html
