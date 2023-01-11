---
title: "Decrypting Blackbox secrets at build time with Paperkey"
date: "2019-09-02"
permalink: "/blog/2019/09/02/gpg-blackbox-paperkey.html"
tags: [gpg, blackbox, jenkins, bash]
---



    “Security is 1% technology plus 99% following the procedures correctly” — Tom Limoncelli

Having dealt with GPG last week at work,
I remembered that I had intended to write a blog post
about how we used GPG_, Blackbox_, and Paperkey_ to store secrets in Git
at my `previous job`_.

We used Blackbox to manage secrets that were needed
during development, build, deployment, and runtime.
These secrets included AWS credentials, Docker registry credentials,
our private PyPI credentials, database credentials, and certificates.
We wanted these secrets to be under version control,
but also to be secure.

For example, we had a ``credentials.sh`` that exported environment variables,
which was managed by Blackbox:

.. code-block:: bash

    # Save current value of xtrace option from $-; disable echoing of executed commands
    { if echo $- | grep -q "x"; then XT="-x"; else XT="+x"; fi; set +x; } 2>/dev/null

    # export environment variables, many containing secrets
    export AWS_ACCESS_KEY_ID='...'
    export AWS_SECRET_ACCESS_KEY='...'

    export PYPI_USER='build'
    export PYPI_PASSWD='...'
    export PIP_INDEX_URL="https://$PYPI_USER:$PYPI_PASSWD@pypi.example.com/pypi/"

    # Restore previous value of xtrace option
    set $XT

The ``XT`` prologue ensures that even if this script is ``source``’d
with `set -x`_ (debug tracing) enabled,
that executing this script will not leak secrets into build logs.
The epilogue turns the ``xtrace`` option back on again if it was on at the start.

We used LastPass_ to manage personal credentials that were needed in a browser,
but it wasn't suitable for automated use in CI.


How Blackbox Works
------------------

Blackbox builds on top of `GNU Privacy Guard`_ (aka GnuPG aka GPG)
to automate the secure management
of a set of files containing secrets
that are “encrypted at rest”
and stored in a Version Control System (VCS), such as Git.
These registered files are owned collectively by a set of administrators,
each of whom has their own separate keypair
(a public key and a private key)
stored in their own keyrings.
The administrators' public keys are also present in Blackbox's keyring,
which is stored in the VCS.
Using Blackbox's commands,
any administrator can decrypt a file containing secrets,
update the secrets in the file,
encrypt the updated secrets file,
and commit that encrypted file into the VCS.
Administrators can be removed from a Blackbox installation,
after which they will not be able to decrypt the updated secrets files\ [#revocation]_.

How does Blackbox encrypt a file so that any administrator can decrypt it?
It uses GPG to encrypt the file for multiple recipients,
say, `Alice, Bob, and Carol`_.

When GPG encrypts a file, it:

* creates a random *session key* for `symmetric encryption`_
* writes a header for *each recipient*, containing:

  - the ID of the recipient's public key
  - the result of asymmetrically encrypting the session key
    with the recipient's public key

* possibly signs the data
* compresses the (signed) data
* symmetrically encrypts the compressed data with the session key
* writes the encrypted, compressed data

Only the recipients have the private keys (in theory, at least).
Therefore, only a recipient can decrypt the encrypted file.

To decrypt the file for a recipient, GPG:

* finds the encrypted session key packet
  whose keyID matches the recipient's public key
* decrypts the session key using the recipient's private key
* decrypts the encrypted, compressed data using the session key
* decompresses the decrypted data
* verifies the signature, if present
* writes the cleartext

This is a hybrid scheme.
Symmetric encryption is a lot `faster and more compact`_
than public key/private key asymmetric encryption,
so it's used to encrypt the actual data.
Furthermore, if the data were entirely encrypted with a recipient's public key,
then encrypting for *N* recipients would mean that the size of the result
would be proportional to the
(number of recipients) × (the length of the original data).
With the hybrid scheme,
the header grows a `few hundred bytes`_ for each recipient
but the data is encrypted only once, with faster encryption.

Blackbox encrypts a registered file
with all of the administrators as the recipients,
so any administrator can decrypt the file.

.. figure:: /content/binary/typical-pgp-message.jpg
    :alt: Typical PGP Message
    :target: http://www.cse.tkk.fi/fi/opinnot/T-110.5240/2009/luennot-files/Lecture%202.pdf

    Typical PGP Message

    (Figure from `Network Security\: Email Security, PKI`_, Tuomas Aura)

You can use ``gpg --list-packets`` to dump the contents of any GPG message.
`An Advanced Intro to GnuPG`_ dives into the message format in more detail.

Going back to my original example,
``credentials.sh`` is a file registered in ``blackbox-files.txt``.
This file should never be committed to the VCS—\
add it to `gitignore`_ to prevent accidentally committing it.
Instead, ``credentials.sh.gpg`` is committed.
Since the latter is a binary file,
comparing two versions in cleartext is tricky.

.. [#revocation]  If they have a snapshot of the VCS before their access was revoked,
    they will still be able to decrypt the secrets as they were then.
    In principle, you should be changing passwords and certificates
    every time someone's access is revoked.


Private Keys and Paperkey
-------------------------

Administrators can encrypt and decrypt Blackbox'd files
because they have their private key on a local keyring.

Getting a private key onto other hosts can be tricky.
We developed this technique when we were using Atlassian's hosted Bamboo CI service.
We later used it with hosted Jenkins at Cloudbees.
Because we were using a hosted Continuous Integration (CI) service,
we had limited control over what we could install.
If I remember correctly,
Bamboo had support for secret environment variables,
but did not provide a way to store a keyring file.
There was also a limit on the length of the environment variables, I believe.

We were able to get past this by using Paperkey_
to (de)serialize the secret key.
Paperkey can extract just the secret part of a secret key:
‘Due to metadata and redundancy,
OpenPGP secret keys are significantly larger than just the "secret bits".
In fact, the secret key contains a complete copy of the public key.’

We created a keypair for the CI on a secure host,
serialized the secret with Paperkey,
and pasted the secret into the CI's UI to become an environment variable.
At build time, we used Paperkey on the CI box to deserialize the secret key
from the environment variable,
before decrypting the secrets needed with Blackbox.

To create the CI keypair,
follow the portion of the `Blackbox "role accounts" instructions`_
that create a sub-key with no password for ``ci@example.com``.

Then, serialize the public key and the secret with Paperkey:

.. code-block:: bash

    cd /tmp/NEWMASTER
    gpg --homedir . --export ci@example.com \
        | base64 > public_key.txt
    gpg --homedir . --export-secret-keys ci@example.com \
        | paperkey --output-type=raw \
        | base64 > secret.txt

Copy and paste the contents of ``public_key.txt``
to the ``GPG_PUBLIC_KEY`` environment variable in the CI.
Similarly, copy ``secret.txt`` to ``GPG_SECRET``.

Securely delete everything in ``/tmp/NEWMASTER``.

We used a script like this on the CI to reconstitute the keypair
and to decrypt the other secrets from Blackbox:

.. code-block:: bash

    #!/usr/bin/env bash

    # Run during a CI build to decrypt all Blackbox-encrypted files in this repo.
    # Can also be used interactively.

    set -ex

    # Root of Git working tree
    SERVICES_DIR="$(cd "$(dirname "$0")/.."; pwd)"

    if [ "$CI_BUILD" = "true" ]; then
        GPG_HOMEDIR="$(mktemp -d -t gnupg.XXX)"
        SECRET_KEY_FILE="$GPG_HOMEDIR/secret.key"
        PUBLIC_KEY_FILE="$GPG_HOMEDIR/public_key.gpg"

        # this variable is how you can customize how GPG is used in Blackbox
        GPG="gpg --homedir=$GPG_HOMEDIR"

        # Remove secrets from filesystem on exit.
        function clean_up {
            # TODO: use shred, if available
            rm -rf "$GPG_HOMEDIR"
        }
        trap clean_up EXIT;

        echo "Unpacking keys; exiting debug mode to redact..."
        set +x

        if [ -z "$GPG_PUBLIC_KEY" -o -z "$GPG_SECRET" ]; then
            echo "Missing CI credential env vars for GPG key and secret"
            exit 1
        fi

        # unpack public key
        echo "$GPG_PUBLIC_KEY" | base64 --decode > "$PUBLIC_KEY_FILE"

        # unpack secret key
        echo "$GPG_SECRET" | base64 --decode > "$SECRET_KEY_FILE"

        echo "Secrets unpacked..."
        set -x

        # reconstitute and import full key into $GPG_HOMEDIR
        paperkey --pubring "$PUBLIC_KEY_FILE" --secrets "$SECRET_KEY_FILE" \
            | $GPG --import

        # TODO: vendor Blackbox
        BLACKBOX_DIR="$(mktemp -d -t blackbox.XXX)"
        BLACKBOX_BIN=$BLACKBOX_DIR/bin

        # Shallow clone of Blackbox with most-recent commit only
        git clone --depth 1 https://github.com/StackExchange/blackbox.git $BLACKBOX_DIR
    else
        # So that you only have to enter your password once when running interactively
        eval "$(gpg-agent --daemon)"

        # No custom GPG_HOMEDIR needed
        GPG="gpg"

        BLACKBOX_POSTDEPLOY="$(command -v blackbox_postdeploy)" || ret=$?
        if [ -n "$BLACKBOX_POSTDEPLOY" ]; then
            # Use the Blackbox that's on the path
            BLACKBOX_BIN="$(dirname $BLACKBOX_POSTDEPLOY)"
        else
            # Assume Blackbox is checked out in a sibling dir to $SERVICES_DIR
            BLACKBOX_BIN="$(cd "$SERVICES_DIR/.."; pwd)"/blackbox/bin
            if [ ! -f "$BLACKBOX_BIN/blackbox_postdeploy" ]; then
                echo "Can't find Blackbox binaries"
                exit 1
            fi
        fi
    fi

    # decrypt secrets in $SERVICES_DIR using custom GPG_HOMEDIR
    GPG="$GPG" $BLACKBOX_BIN/blackbox_postdeploy

    # test that decryption worked
    grep 'congrats!' test_secret.txt

At the end of the build,
run ``blackbox_shred_all_files`` to destroy any decrypted files.


More Reading
------------

* `Blackbox`_
* `Paperkey`_
* `Protect your documents with GPG`_
* `Anatomy of a GPG Key`_
* `Creating the perfect GPG keypair`_
* `How GPG works\: Encrypt`_
* `GPG import and export`_
* `An Advanced Intro to GnuPG`_
* `Network Security\: Email Security, PKI`_

.. _GPG:
.. _GNU Privacy Guard:
    https://gnupg.org/
.. _Blackbox:
    https://github.com/StackExchange/blackbox
.. _Paperkey:
    http://www.jabberwocky.com/software/paperkey/
.. _previous job:
    /blog/2018/12/31/2018-review.html
.. _LastPass:
    https://www.lastpass.com/
.. _set -x:
    https://renenyffenegger.ch/notes/Linux/shell/bash/built-in/set/x
.. _symmetric encryption:
    https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences
.. _Alice, Bob, and Carol:
    https://en.wikipedia.org/wiki/Alice_and_Bob#Cast_of_characters
.. _faster and more compact:
    https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences
.. _GPG file size with multiple recipients:
.. _few hundred bytes:
    https://security.stackexchange.com/questions/8245/gpg-file-size-with-multiple-recipients
.. _Network Security\: Email Security, PKI:
    http://www.cse.tkk.fi/fi/opinnot/T-110.5240/2009/luennot-files/Lecture%202.pdf
.. _An Advanced Intro to GnuPG:
    https://begriffs.com/posts/2016-11-05-advanced-intro-gnupg.html
.. _gitignore:
    https://git-scm.com/docs/gitignore
.. _Blackbox "role accounts" instructions:
    https://github.com/StackExchange/blackbox#set-up-automated-users-or-role-accounts
.. _Anatomy of a GPG Key:
    https://davesteele.github.io/gpg/2014/09/20/anatomy-of-a-gpg-key/
.. _How GPG works\: Encrypt:
    https://www.darkcoding.net/software/how-gpg-works-encrypt/
.. _GPG import and export:
    https://gist.github.com/chrisroos/1205934
.. _Creating the perfect GPG keypair:
    https://alexcabal.com/creating-the-perfect-gpg-keypair
.. _Protect your documents with GPG:
    http://www.linux-magazine.com/Online/Features/Protect-your-Documents-with-GPG

.. _permalink:
    /blog/2019/09/02/gpg-blackbox-paperkey.html
