---
title: "The Ironies of Spam"
date: "2006-05-04"
permalink: "/blog/2006/05/04/TheIroniesOfSpam.html"
tags: [humor]
---



I hang out on the SourceForge-hosted
`inkscape-user <http://www.inkscape.org/mailing_lists.php>`_ mailing list,
where I pick up useful tips for the `Inkscape <http://www.inkscape.org/>`_
SVG editor (vector drawing program).

For months, the list has been plagued with spam; largely because anyone can
send to the list. The policy has been not to require new users to sign up
for the list before being able to send questions. This is commendably
friendly and user-centric, but the spam has become a real annoyance.

One of the Inkscape developers finally said that, if a dozen or more people
said "yes, restrict posting to list members only" and no-one opposed it, he
would lock the list down. I attempted to vote yes and got the following
rejection letter from SourceForge::

    <inkscape-user@lists.sourceforge.net>:
    66.35.250.206 does not like recipient.
    Remote host said: 550-Postmaster verification failed while checking <george@reilly.org>
    550-Called:   205.158.62.206
    550-Sent:     RCPT TO:<postmaster@reilly.org>
    550-Response: 550 <postmaster@reilly.org>: User unknown
    550-Several RFCs state that you are required to have a postmaster
    550-mailbox for each mail domain. This host does not accept mail
    550-from domains whose servers reject the postmaster address.
    550 Sender verify failed
    Giving up on 66.35.250.206.

Such irony! I had received a similar bounce a few days before from the
`FlexWiki-Users
<http://www.flexwiki.com/default.aspx/FlexWiki/FlexWikiMailingList.html>`_
mailing list, which is also hosted by SourceForge, when I announced
`Vim Syntax Highlighting for FlexWiki
</blog/2006/05/04/VimSyntaxHighlightingForFlexWiki.html>`_.

I don't own the ``reilly.org`` domain. It (and thousands of others) are
owned by `NetIdentity <http://www.netidentity.com>`_. I had an exchange
with their postmaster, who said in part:

    I did talk to sourceforge.  They claimed it is an essential part of their spam
    filtering process to reject domains that dont have a postmaster mailbox.

    I've tried that (at least on a test basis) myself and with all due respect to
    them, it is passe' ... doesnt work too well.  And it has the added "advantage"
    of having to connect back to the sending mail domain every time to see if a
    postmaster for that domain exists.  This holds up email and creates additional
    smtp connections - and hence even more load on mailservers, in the case of
    domains - with postmaster up and running - that are forged into spam.

    I did suggest a few more rather efficient (and practical) filters they could
    use, but well, they didnt respond to those

He has since added a postmaster mailbox for reilly.org, so I can post to
SourceForge lists again.

The Inkscape vote passed, of course. Only subscribers can post now.
Non-subscribers can also use a webform to send questions, so it's not a big
impairment.

.. _permalink:
    /blog/2006/05/04/TheIroniesOfSpam.html
