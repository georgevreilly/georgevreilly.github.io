---
title: "Obfuscating Passwords in URLs in Python"
date: "2016-01-04"
permalink: "/blog/2016/01/04/PythonObfuscateUrlPassword.html"
tags: [python, urls, metabrite, til]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

`RFC 1738`_ allows passwords in URLs,
in the form ``<scheme>://<username>:<password>@<host>:<port>/<url-path>``.
Although passwords are deprecated by `RFC 3986`_ and other newer RFCs,
it's occasionally useful.
Several important packages in the Python world allow such URLs,
including SQLAlchemy_ (``'postgresql://scott:tiger@localhost:5432/mydatabase'``)
and Celery_ (``'amqp://guest:guest@localhost:5672//'``).
It's also useful to be able to log such URLs without exposing the password.

Python 2 has `urlparse.urlparse`_
(known as `urllib.parse.urlparse`_ in Python 3
and ``six.moves.urllib_parse.urlparse`` in the Six_ compatibility library)
to split a URL into six components,
*scheme*, *netloc*, *path*, *parameters*, *query*, and *fragment*.
The *netloc* corresponds to ``<user>:<password>@<host>:<port>``.

Unfortunately, neither Python 2 nor 3's ``urlparse``
properly handle the *userinfo*
(*username* + optional *password* in the *netloc*),
as they must be encoded.
RFC 1798: “Within the user and password field,
any ``:``, ``@``, or ``/`` must be encoded
[as ``%3A``, ``%40``, and ``%2F`` respectively].”
(Not said: ``%`` also needs to be encoded as ``%25``.)
Consider a username like ``fred@example.com``
or a password like ``b@d:/st%ff``,
which would create ambiguous URLs if they were not encoded.

The following demonstrates both how to obfuscate a password (if present) in a URL,
as well as how to encode and decode the username and password correctly.

.. code:: python
    :number-lines:

    from six.moves.urllib_parse import urlparse, urlunparse, unquote

    def obfuscate_url_password(url):
        """Obfuscate password in URL for use in logging"""
        parts = urlparse(url)
        if parts.password:
            url = urlunparse(
                (parts.scheme,
                 make_netloc(parts.hostname, parts.port, netloc_username(parts.netloc), '***'),
                 parts.path, parts.params, parts.query, parts.fragment))
        return url

    def netloc_username(netloc):
        """Extract decoded username from `netloc`."""
        if "@" in netloc:
            userinfo = netloc.rsplit("@", 1)[0]
            if ":" in userinfo:
                userinfo = userinfo.split(":", 1)[0]
            return unquote(userinfo)
        return None

    def netloc_password(netloc):
        """Extract decoded password from `netloc`."""
        if "@" in netloc:
            userinfo = netloc.rsplit("@", 1)[0]
            if ":" in userinfo:
                return unquote(userinfo.split(":", 1)[1])
        return None

    def make_netloc(host, port=None, username=None, password=None):
        """Make a netloc for URL."""
        if username:
            userinfo = rfc_1738_quote(username)
            if password is not None:
                userinfo += ':' + rfc_1738_quote(password)
            userinfo += '@'
        else:
            userinfo = ''

        if ':' in host:
            netloc = '[' + host + ']'  # IPv6 literal
        else:
            netloc = host
        if port:
            netloc += ':' + str(port)
        return userinfo + netloc

    def rfc_1738_quote(text):
        # RFC 1798: Within the user and password field, any ":", "@", or "/" must be encoded.
        # (Also "%" must be encoded.) Adapted from SQLAlchemy
        return re.sub(r'[:@/%]', lambda m: "%%%X" % ord(m.group(0)), text)


.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/
.. _RFC 1738:
    https://www.ietf.org/rfc/rfc1738.txt
.. _RFC 3986:
    https://www.ietf.org/rfc/rfc3986.txt
.. _SQLAlchemy:
    https://www.sqlalchemy.org/
.. _Celery:
    https://docs.celeryproject.org/en/stable/
.. _urlparse.urlparse:
    https://docs.python.org/2/library/urlparse.html#urlparse.urlparse
.. _urllib.parse.urlparse:
    https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
.. _Six:
    https://six.readthedocs.io/

.. _permalink:
    /blog/2016/01/04/PythonObfuscateUrlPassword.html
