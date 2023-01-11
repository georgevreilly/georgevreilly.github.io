---
title: "NVelocity templates and absolute paths"
date: "2007-03-07"
permalink: "/blog/2007/03/07/NVelocityTemplatesAndAbsolutePaths.html"
tags: [.NET, c-sharp, til]
---



.. image:: https://www.codegeneration.net/logos/nvelocity.gif
    :alt: NVelocity
    :target: http://www.castleproject.org/others/nvelocity/index.html
    :class: right-float

We've started using the `NVelocity`_ template formatting engine.
We were absolutely stymied for an hour, trying to figure
out how to get it working with an absolute path to the template file,
instead of the relative path shown in the `documentation`_.

The trick is to set ``file.resource.loader.path``.
Here's how to load ``C:\foo\bar\somefile.vm``:

.. code:: csharp

    ExtendedProperties props = new ExtendedProperties();
    props.AddProperty("file.resource.loader.path", new ArrayList(new string[]{".", "C:\\"}));
    velocity.Init(props);

    template = velocity.GetTemplate("foo\\bar\\somefile.vm");

.. _NVelocity: http://www.castleproject.org/others/nvelocity/index.html
.. _documentation: http://www.castleproject.org/others/nvelocity/usingit.html

.. _permalink:
    /blog/2007/03/07/NVelocityTemplatesAndAbsolutePaths.html
