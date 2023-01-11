---
title: "Usability testing dasBlog installation"
date: "2006-02-10"
permalink: "/blog/2006/02/10/UsabilityTestingDasBlogInstallation.html"
tags: [usability, dasblog]
---



I've been hanging out on the dasBlog developers' mailing list for the last
couple of months, and I've made some minor contributions to the code.

I sent the following email to the developers' list last night.


----


My wife has decided to start a blog for
`Team Ireland <http://thewheel.biz/TeamIreland>`_ in the
`2006 Knitting Olympics <http://www.yarnharlot.ca/blog/olympics2006.html>`_,
and she asked me to install `dasBlog <http://dasblog.info>`_ on her site.
I decided that this was an excellent opportunity to do some usability testing
on the installation instructions for dasBlog. I asked her to try installing
dasBlog, while I watched. I promised that I would bail her out if she got
mired too deeply.

Emma has worked as a black-box software tester for several years. She
writes SQL scripts by hand, but is not otherwise a programmer. I figured
that she could probably install a project like dasBlog, with an intended
audience of Advanced End Users.

First, we obtained a graphical FTP client
(`FileZilla <http://filezilla.sourceforge.net/>`_) and checked that she
could successfully upload a one-line ASP.NET program to her website::

    The time is <% = DateTime.Now %>

Then it was time to start installing dasBlog. I told her to start at
http://dasblog.info and figure out how to get dasBlog and how to install it.

She totally ignored the alphabetical table of contents on the left-hand
side, which is formatted as a rather large set of RSS feeds. Instead, she
read through the long blogpost on the right-hand side, which didn't
enlighten her. After a while, I pointed to the left column. Her reaction:
why do I want to subscribe to feeds? I pointed out to the `Install/Setup
<http://dasblog.info/CategoryView,category,Install/Setup.aspx>`_
feed. (Reviewing the frontpage post now, I see that the Install/Setup link
also appears there.)

    There needs to be a prominent link on the front page to a Getting
    Started guide.  http://dasblog.info and http://dasblog.us are
    a huge improvement on the state of the documentation a couple of
    months ago, but they still need work.

She found the Install/Setup instructions confusing. They don't cover well
the case of doing a remote install to a commercial host provider.
Obviously, it's not possible to write a comprehensive guide on this, as
providers have many different configuration utilities. Our provider is
using Ensim's WEBppliance, which I find painful to use.

There needs to be a Point #0 on the Install/Setup instructions: download
the files. After some more headscratching, she found her way to the
`download page <http://sourceforge.net/project/showfiles.php?group_id=127624>`_.
She was pretty sure that she didn't want to download
``DasBlog-1.8.5223.2-Source.zip``, but she wasn't too sure if she should
download ``DasBlog-1.8.5223.2-Web-Files.zip``.

She created a local directory, ``C:\dasblogce`` and unzipped the files there.
That of course meant that the files she needed to upload were in
``C:\dasblogce\dasblogce``.

Point #1 of `Setup/Install
<http://dasblog.info/CategoryView,category,Install/Setup.aspx>`_
is unhelpful to the uninitiated.
Point #2 isn't all that clear either.

Using FileZilla, she uploaded the files from ``C:\dasblogce\dasblogce`` to
``\inetpub\wwwroot\dasblogce`` on her server. Then, with some help from me, she
figured out enough of the horrible Ensim interface to create a virtual
directory, TeamIreland, pointing to the dasblogce folder.

At this point, we went to http://thewheel.biz/TeamIreland but we weren't
able to get in. We got some fairly unfriendly ASP.NET errors.
I had to wade through the Ensim UI and grant write access
to the content, siteconfig, and logs subdirectories, per the Install page.

Finally, we saw the default page provided by dasBlog!

She had read enough of the Install instructions earlier to know that she
needed to modify ``site.config`` and ``siteSecurity.config``, but she wasn't sure
how to modify them on the server. I suggested modifying the local copies
and uploading them.

Her first reaction on seeing ``site.config`` was that there needs to be some
paragraphs (blank lines) for readability. She nearly overlooked the <Root>
setting, but got that configured correctly.

    The default installation of ``site.config`` needs some comments. The stuff
    that you really have to modify should be in a clearly delimited block
    at the top. Something like this:

:

.. code-block:: xml

      <!-- Modify this section before installing -->

      <!-- Important: set this to the base URL of this blog, such as
           http://example com/joeuser/blog/ -->
      <Root>http://localhost/DasBlog/</Root>
      <!-- Banner text. (Note: not all themes show the Subtitle or Description.) -->
      <Title>My DasBlog!</Title>
      <Subtitle>newtelligence powered</Subtitle>
      <Description>A blog about my interests: computers, games, beer, etc.</Description>
      <!-- Email address of blog adminstrator -->
      <Contact>dasblog@example.com</Contact>
      <Copyright>Your Name Here</Copyright>
      <!-- Default visual theme -->
      <Theme>dasBlog</Theme>
      <!-- End of essential modifications -->

She was less sure what to do with ``siteSecurity.config``. She thought she
needed to use the same Name and Password as she uses to log in to the
server. (No. It's arbitrary.) She also needed to add a few additional
Users, since it's going to be a group blog.

There should be a commented-out example of a contributor user in
``siteSecurity.config``:

.. code-block:: xml

      <!-- example of a non-administrator user
        <User>
          <Name>SomeOtherUser</Name>
          <Password>blog-password</Password>
          <Role>contributor</Role>
          <Ask>true</Ask>
          <DisplayName>Some Other User</DisplayName>
          <EmailAddress>SomeOther@example.com</EmailAddress>
        </User>
      -->

She uploaded the modified ``site.config`` and ``siteSecurity.config``. It failed
horribly when she went to log in. I had to download the events.log file to
realize that she had deleted the </Users> in ``siteSecurity.config``.

That fixed, she was able finally log in and create a post. I won't detail
the pain we went through to upload images via FreeTextBox.

The dasBlog admin interface has not been working for her. It's unable to
write to the siteconfig directory. At some point last night, the content
directory somehow became unreadable and the site started throwing ASP.NET
errors.

I was able to fix that tonight by blowing away the content directory in
FileZilla and uploading a backup. I *think* I've fixed everything, by
explicitly granting read and write to the siteconfig and content
directories and everything contained therein.

-----

**Epilogue**: Every new entry in the TeamIreland blog is being created with the
wrong permissions, causing dasBlog to puke. It can be fixed by setting the
permissions for each new file to read/write through the Ensim interface,
but it's hardly a good experience for a group blog. I'm still waiting for
`iHostSites <http://www.ihostsites.net/>`_' support people to set the ACLs
properly.

.. _permalink:
    /blog/2006/02/10/UsabilityTestingDasBlogInstallation.html
