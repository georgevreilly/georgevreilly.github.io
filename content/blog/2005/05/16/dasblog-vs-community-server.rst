---
title: "dasBlog vs. Community Server"
date: "2005-05-16"
permalink: "/blog/2005/05/16/dasBlogVsCommunityServer.html"
tags: [dasblog]
---



I've set up a new personal blog at `www.georgevreilly.com/blog`__.
I'll be posting non-technical stuff there
and I'll be cross-posting on technical matters to Weblogs @ ASP.net.
Here's how I ended up running dasBlog on the new blog.

In the spring of last year, I attempted
to install both `.Text`__ and dasBlog__ on my XP Pro laptop.
I failed, signally, to get either one working.
The details have mercifully faded with time,
leaving me only with a residue of frustration.

I've been meaning to put some photos of mine up on the web for a while.
A week ago, I went to download `nGallery`__,
as I remembered hearing good things about it in the past.
I learned that nGallery is now part of `Community Server`__ (as is .Text).
After navigating through the somewhat confusing portal,
I downloaded a copy of Community Server 1.0.

__ http://www.georgevreilly.com/blog/
__ http://scottwater.com/blog
__ https://github.com/shanselman/dasblog
__ http://www.ngallery.org/
__ http://www.communityserver.org/

Then I spent several frustrating hours trying to get it running on my laptop.
Community Server requires a SQL Server back-end,
but you can also use `MSDE`__, the standalone Microsoft SQL Desktop Engine,
which comes without a GUI.
I downloaded MSDE and the `SQL Web Data Administrator`__, as well as `MSDE Query`__.
I can spell "SQL", but that's about where my knowledge of SQL stops.
I tried to follow the instructions to create the database tables.
I did manage to create the master table,
but I could not figure out how to set the various permissions that the instructions demanded.
I googled extensively and looked through the archived forums
at CommunityServer.org and `SqlJunkies.com`__, to no avail.

__ http://www.asp.net/msde/default.aspx
__ http://www.microsoft.com/downloads/details.aspx?FamilyID=C039A798-C57A-419E-ACBC-2A332CB7F959&displaylang=en
__ http://www.msde.biz/msdequery/download.htm
__ http://www.sqljunkies.com/Forums/ShowForum.aspx?ForumID=140

Really!
If I can't figure this stuff out,
most people are never going to get Community Server running on their own systems.
Don't get me wrong.
Community Server/.Text is a good blogging system,
if you can surmount the barriers to entry.
I'm a competent, skilled developer,
but I've never needed to learn SQL,
and I wasn't motivated enough to dig further.

(I've since realized that my hosting package at `iHostSites`__
includes MySql, but not SQL Server,
so this would have been all for naught.
I think.
Double aargh!)

I gave up on Community Server in frustration, and decided to fall back to nGallery.
I got nGallery installed and running easily enough.
Alas, it was flaky and it was all too easy
to get ASP.net throwing unhandled exceptions back at me. 
spend too much of my life troubleshooting other people's bugs,
and I wasn't prepared to invest any more time on this avenue.

At this point, I googled for "web album software" and came up with `JAlbum`__.
I'm much happier with JAlbum.
It worked flawlessly as soon as I ran it and it's versatile.
Photos will start appearing on my personal website, www.GeorgeVReilly.com, soon.

__ http://www.ihostsites.net/
__ http://jalbum.net/

Yesterday, I decided to give dasBlog another try.
That was altogether more successful.
I did not manage to get it running on my laptop,
but I did get it running on a XP Pro desktop system,
as well as on my public website. 
did have a little difficulty getting it to run on my desktop system,
but that went away as soon as I ran aspnet_regiis -i to reset ASP.net.

I'm not sure why it doesn't run on my laptop,
but the enormous amount of stuff that I've installed on this system
surely plays a role.
Indeed that may have been the reason why nGallery puked on my laptop.
Someday, I'm going to have to flatten the system and reinstall only the important stuff.

Net results:

Album software: JAlbum 1, nGallery 0.

Blogging software: dasBlog 1, Community Server 0.

.. _permalink:
    /blog/2005/05/16/dasBlogVsCommunityServer.html
