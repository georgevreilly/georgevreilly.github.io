---
title: "XML Scripts -- For the Theater"
date: "2005-06-16"
permalink: "/blog/2005/06/16/XMLScriptsForTheTheatre.html"
tags: [dramaturgy, jamesjoyce]
---



For the last three years, I've been involved with
`The Wild Geese Players of Seattle`_,
an amateur group that does readings of Irish literature,
particularly the works of James Joyce and W.B. Yeats.
Our big event every year is Bloomsday_,
June 16th, commemorating Joyce's Ulysses,
which takes place on June 16th, 1904.
It's a tale of a Jewish everyman, Leopold Bloom,
wandering through Dublin one day,
and of the young writer (and Joyce's alter ego), Stephen Dedalus.
We're working our way through the book,
reading a chapter or two each year.
In this, our eighth year, we'll be reading Chapter 11, Sirens_,
at the Brechemin Auditorium in the School of Music
at the University of Washington, on Thursday 16th and Saturday 18th.
Congressman Jim McDermott will be reading
the part of Bloom on the Saturday.

Last year and this year, I have been the assistant dramaturge,
helping to turn chapters into a script to be read by 15-20 readers.
In previous years, the director made a photocopy of the book,
wrote attributions ("Narrator 1", "Bloom", "Stephen", etc)
on the paper, then photocopied that text and handed it out to the readers.
Since the script was a moving target,
everyone ended up with a set of scruffy, tatty,
inconsistently hand-annotated sheets.
It was a mess.

I knew there had to be a better way.
Now, we've adapted the etext_
of the 1922 Paris Edition, prepared by `Project Gutenberg`_,
which saves a lot of typing.
The script is marked up in XML and styled with XSLT
to produce an HTML page.
After a rehearsal or two,
when it's apparent that the script isn't quite right,
it's an easy matter to make a few changes,
render fresh HTML, and print new scripts.

The XSLT required is fairly straightforward.
About the only mildly interesting thing is defining
one template in terms of another;
e.g., I want all the speakers to share the same styling,
so I defined a parameterized ``speaker`` template:

.. code-block:: xslt

    <xsl:template name="speaker">
        <xsl:param name="name" />
        <div class="speaker">
            <span class="speaker"><xsl:value-of select="$name"/>: </span>
            <xsl:apply-templates />
        </div>
    </xsl:template>

which is called thus:

.. code-block:: xslt

    <xsl:template match="bloom">
        <xsl:call-template name="speaker">
            <xsl:with-param name="name">Bloom</xsl:with-param>
        </xsl:call-template>
    </xsl:template>

The *real* challenge in preparing the script is dramaturgical.
*Ulysses* is a notoriously difficult and dense text,
woven through with Bloom's stream-of-consciousness interior monologue.
Each chapter is written in a different style.
Sirens, for example, has musical themes running through it,
and we'll be accompanied by a piano player this year.

What would you do with this?

    Bloom heard a jing, a little sound. He's off. Light sob of breath Bloom
    sighed on the silent bluehued flowers. Jingling. He's gone. Jingle. Hear.

Here's what we came up with:

.. raw:: html

    <b>N1:</b> Bloom heard a jing, a little sound.<br>
    <b>Bloom:</b> He's off.<br>
    <b>N1:</b> Light sob of breath Bloom sighed on the silent bluehued flowers.
               Jingling.<br>
    <b>Bloom:</b> He's gone.<br>
    <b>N1:</b> Jingle.<br>
    <b>Bloom:</b> Hear.

Or with this paragraph?

    --Yes, Mr Bloom said, teasing the curling catgut line. It certainly is.
    Few lines will do. My present. All that Italian florid music is. Who is
    this wrote? Know the name you know better. Take out sheet notepaper,
    envelope: unconcerned. It's so characteristic.

We chose this:

.. raw:: html

    <b>Bloom (Aloud):</b> Yes.<br>
    <b>N1:</b> Mr Bloom said, teasing the curling catgut line.<br>
    <b>Bloom (Aloud):</b> It certainly is.<br>
    <b>Bloom:</b> Few lines will do. My present.<br>
    <b>Bloom (Aloud):</b> All that Italian florid music is.<br>
    <b>Bloom:</b> Who is this wrote? Know the name you know better.
                  Take out sheet notepaper, envelope: unconcerned.<br>
    <b>Bloom (Aloud):</b> It's so characteristic.

We ended up with three narrators in this chapter:
N1 deals with Bloom, primarily;
N2 is mostly for Miss Douce and Miss Kennedy, the siren barmaids;
and N3 handles the other characters.

Lest I scare you off, much of the chapter is quite clear
and often very funny, even for people who are unfamiliar with the book.

The `James Joyce Portal`_
is a good starting point for matters Joycean.

.. _The Wild Geese Players of Seattle:
    http://www.wildgeeseseattle.org/
.. _Bloomsday:
    http://en.wikipedia.org/wiki/Bloomsday
.. _Sirens:
    http://www.wildgeeseseattle.org/Joyce/Bloomsday/2005.html
.. _etext:
    http://www.gutenberg.org/etext/4300
.. _Project Gutenberg:
    http://www.gutenberg.org/
.. _James Joyce Portal:
    http://www.robotwisdom.com/jaj/portal.html

.. _permalink:
    /blog/2005/06/16/XMLScriptsForTheTheatre.html
