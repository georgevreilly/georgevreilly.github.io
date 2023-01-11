---
title: "NVelocity: loading templates from embedded resources"
date: "2007-03-14"
permalink: "/blog/2007/03/14/NVelocityLoadingTemplatesFromEmbeddedResources.html"
tags: [.NET, c-sharp, til]
---



.. image:: https://www.codegeneration.net/logos/nvelocity.gif
    :alt: NVelocity
    :target: http://www.castleproject.org/others/nvelocity/index.html
    :class: right-float

In last week's tip on
using the `NVelocity`_ template formatting engine,
I described what to set to load a template from
an `absolute path`_.

.. _NVelocity: http://www.castleproject.org/others/nvelocity/index.html
.. _absolute path:
    /blog/2007/03/07/NVelocityTemplatesAndAbsolutePaths.html

Here's the magic necessary to get NVelocity to load a template from an
embedded resource:

.. code:: csharp

    VelocityEngine engine = new VelocityEngine();
    ExtendedProperties properties = new ExtendedProperties();
    properties.AddProperty("resource.loader", "assembly");
    properties.AddProperty("assembly.resource.loader.class",
        "NVelocity.Runtime.Resource.Loader.AssemblyResourceLoader, NVelocity");
    properties.AddProperty("assembly.resource.loader.assembly", "StencilFormatter");
    engine.Init(properties);

.. _permalink:
    /blog/2007/03/14/NVelocityLoadingTemplatesFromEmbeddedResources.html
