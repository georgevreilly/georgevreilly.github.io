---
title: "Posting to dasBlog with Windows Live Writer"
date: "2006-08-18"
permalink: "/blog/2006/08/18/PostingToDasBlogWithWindowsLiveWriter.html"
tags: [dasblog]
---



From Scott Hanselman,
I learned about Microsoft's new blog posting client, `Windows Live Writer`__.
I've played around with it and it's definitely the nicest free blogging client that I've used.

__ http://www.hanselman.com/blog/WindowsLiveWriterAndDasBlog19.aspx
__ http://www.emmabart.com/Meanderings/
__ http://filezilla.sourceforge.net/

Here are instructions on configuring it to post to dasBlog.
I'm showing how to set it up for `Emma's blog`__, since she's running dasBlog 1.8.
I'm running a recent build of the as-yet unreleased dasBlog 1.9, 
which supports Really Simple Discovery, 
which makes the first part of this exercise simpler, 
as WLW can infer that it's dealing with Metaweblog API, 
just by pointing it at the root of the blog.

Launch WLW and Add a Weblog Account. 
Choose Another weblog service.

.. image:: /content/binary/chooseblogtype_thumb.png

Next, enter the URL of your blog 
and the username and password that you use to log in.

.. image:: /content/binary/login_thumb.png

Select your provider, Metaweblog API. 
The remote posting URL is the blog homepage URL + /blogger.aspx:

.. image:: /content/binary/selectprovider_thumb.png

You are now ready to post text to your blog:

.. image:: /content/binary/configcomplete_thumb.png

Create a test post. 
Be sure to include an image. 
When you try to Publish it, you'll get a dialog like this:

.. image:: /content/binary/imageuploadunsupported_thumb.png

Use an FTP program to discover the FTP path to your blog's content/binary directory. 
Here's the relevant area in `FileZilla`__:

.. image:: /content/binary/filezillaaddressbar_thumb.png

Note that the leading parts of the path 
are quite different to the corresponding HTTP URL (and peculiar to Emma's site). 
Fill out the FTP Settings dialog with the appropriate settings:

.. image:: /content/binary/ftpsettings_thumb.png

You're now ready to upload images via FTP:

.. image:: /content/binary/ftpconfigcomplete_thumb.png

Go for it.

This post was of course created with Windows Live Writer. 
I did have to set the Image Size to original for each image, 
or they would have been squished down to an unreadable size.

Update: I had a hell of a time when I first posted this. 
None of the images showed up. 
Instead I was seeing fragments of raw HTML. 
I tracked it down to the dasBlog configuration filters, 
which (by default) rewrite the word dasBlog as a link to the dasBlog website. 
That's more-or-less fine in plain text, 
but it plays havoc if the word dasBlog appears in the middle of one of your image URLs.

.. _permalink:
    /blog/2006/08/18/PostingToDasBlogWithWindowsLiveWriter.html
