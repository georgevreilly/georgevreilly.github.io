---
title: "Setting Up a Pairing Workstation for Chrome and Git"
date: "2015-11-15"
permalink: "/blog/2015/11/15/PairingGit.html"
tags: [pair programming, git, agile, metabrite]
---



.. image:: /content/binary/paironChair.jpg
    :alt: PairOn Chair
    :target: https://www.globalnerdy.com/2008/08/28/pair-programming-chairs/

\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

At MetaBrite, we believe in the power of `pair programming`_.
We find that pairing helps for collaboration on difficult tasks,
for exploring new areas, for knowledge transfer,
and for spurring each other to better solutions.
I find it to be fun, though it can also be exhausting.
It's not ideal for all our work—\
there's no value in tying up two developers on some rote task that both know well.

Last week, I rebuilt our primary pairing workstation.
In its previous incarnation, we had an account for each developer.
Each of us had set up some personal preferences in our own user account,
configured our editor(s), and hooked up our GitHub credentials.
The arrangement worked but it was always disconcerting
to see a large number of Git checkins attributed only to "Fred"
when you knew that both "Fred" and "Jim" had paired on that feature.
We had adopted the convention of ending each commit message
with "Pair: Fred & Jim",
but that was easy to forget and hard to see.

Most of us have MacBooks as our work machines,
but the pairing workstation is a beefy desktop system
running Ubuntu 14.04.
It has two monitors, two keyboards, and two mice.
The monitors are mirrored so that each person can read the screen
without neck or eye strain.
The notion of a `PairOn chair`_ is amusing
but I doubt that it would work well for us—\
we each have our own chair.


Chrome Profiles
---------------

When I rebuilt the machine, I set up only one user account, ``pair``.
I configured Chrome to have `multiple profiles`_,
one for each developer.
This means that each of us can launch our own browser window
where we can read our own email,
access GitHub or StackOverflow using our own identity,
or log into our own copy of the `LastPass`_ password manager browser extension.


Git Pair
--------

I also changed how we manage local commits to Git
and how we push and pull from our GitHub repositories.

For local commits, we're using some `helper scripts from Pivotal`_.
The ``git pair`` command updates ``user.name`` and ``user.email`` in ``.git/config``
based on values in ``.git/pairs``:

For example, ``git pair fb sac`` updates ``.git/config`` thus:

.. code:: ini

    user.name = Fred Beebe and Sheila A. Corn
    user.email = pair+fred+sheila.a.corn@example.com

Based on ``.pairs`` in the project root:

.. code:: yaml

    # .pairs - configuration for 'git pair'
    pairs:
      # <initials>: <Firstname> <Lastname>[; <email-id>]
      fb: Fred Beebe; fred
      jo: Jim Osward; josward
      sac: Sheila A. Corn; sheila.a.corn
    email:
      prefix: pair
      domain: example.com
      no_solo_prefix: true
    global: false

(Fred, Jim, and Sheila are a nod to the `BBC Micro`_
of my youth, not actual MetaBrite developers.)

Now ``git log`` shows a series of commits attributed to:

.. code:: vctreestatus

    Author: Fred Beebe & Sheila A. Corn <pair+fred+sheila.a.corn@example.com>

These commits are created with ``git commit``, as usual.
You can use ``git pair-commit`` to attribute a commit
to just one, randomly chosen member of the pair.


Multiple SSH Keys
-----------------

I also wanted each of us to be able to push to or pull from the MetaBrite GitHub repositories,
without having a shared SSH key.

I had each of us create an `SSH key with passphrase`_,
which we uploaded to our own GitHub accounts.

We then configured ``~pair/.ssh/config`` with a series of `Host entries`_,
named after GitHub usernames:

.. code:: console

    Host            github-fredbeebe
        Hostname        github.com
        User            git
        IdentityFile    ~/.ssh/id_rsa_fredbeebe
        IdentitiesOnly yes
        PreferredAuthentications publickey

    Host            github-josward
        Hostname        github.com
        User            git
        IdentityFile    ~/.ssh/id_rsa_josward
        IdentitiesOnly yes
        PreferredAuthentications publickey

    # etc

And we set up a `Git remote`_ for each identity in each Git working copy:

.. code:: bash

    $ cd ~/src/example
    $ git remote -v
    fred    git@github-fredbeebe:our_org/example.git (fetch)
    fred    git@github-fredbeebe:our_org/example.git (push)
    jim	    git@github-josward:our_org/example.git (fetch)
    jim	    git@github-josward:our_org/example.git (push)

Here, ``our_org`` is the GitHub organization and ``example`` is the GitHub repository,
which can also be found at https://github.com/our_org/example.


Adding a New Remote
-------------------

To add a ``sheila`` remote,
create an SSH key called ``id_rsa_sheilacorn``,
upload the key to Sheila's GitHub account,
then add a ``github-sheilacorn`` Host entry to ``~/.ssh/config``:

.. code:: console

    Host            github-sheilacorn
        Hostname        github.com
        User            git
        IdentityFile    ~/.ssh/id_rsa_sheilacorn
        IdentitiesOnly yes
        PreferredAuthentications publickey

Finally, in each Git working copy:

.. code:: bash

    $ cd ~/src/example
    $ git remote add sheila git@github-sheilacorn:our_org/example.git

Now we can say:

- ``git fetch fred``
  — Using Fred's SSH key, fetch all branches and tags from the remote repository at GitHub.
- ``git pull jim master``
  — using Jim's remote, pull the ``master`` branch from GitHub.
- ``git push sheila feature/emoji-avatars``
  — push the ``feature/emoji-avatars`` branch using Sheila's credentials.
- ``git clone --origin jim git@github-josward:our_org/some_stuff.git``
  — Clone the ``some_stuff`` repo using Jim's key,
  creating a remote named ``jim``.

All other Git commands behave just as before.

So far, it seems to be working well.

.. tip:: If you get "Too many authentication failures for username" when using SSH,
    try using ``ssh -o 'IdentitiesOnly yes'`` instead.
    By default, ssh-agent will promiscuously offer many identities.

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/
.. _pair programming:
    http://dsouthard.github.io/CSCI5828_PairProgramming/
.. _PairOn chair:
    http://www.globalnerdy.com/2008/08/28/pair-programming-chairs/
.. _multiple profiles:
    https://support.google.com/chrome/answer/2364824?hl=en
.. _LastPass:
    https://lastpass.com/
.. _helper scripts from Pivotal:
    https://github.com/pivotal/git_scripts#git-pair
.. _BBC Micro:
    https://en.wikipedia.org/wiki/BBC_Micro#Hardware_features:_Models_A_and_B
.. _SSH key with passphrase:
    https://help.github.com/articles/generating-ssh-keys/
.. _Host entries:
    http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/
.. _Git remote:
    http://git.github.io/git-reference/remotes/#remote

.. _permalink:
    /blog/2015/11/15/PairingGit.html
