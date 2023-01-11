---
title: "HTTPS for GitHub Pages Custom Domain: Not Yet"
date: "2016-08-29"
permalink: "/blog/2016/08/29/HTTPSforGitHubPagesCustomDomainNotYet.html"
tags: [security]
---



This website, http://www.georgevreilly.com/, is hosted at GitHub Pages.
It's actually https://georgevreilly.github.io/
but I've configured the former as the “custom domain”,
so the latter is unconditionally redirected to the custom domain.

GitHub Pages gives me free, fast hosting and an easy publication model:
I commit the latest changes to my ``master`` branch,
I push the branch to GitHub,
and seconds later, my site is updated.
I'm using Acrylamid__ to generate the content from reStructuredText source
on the ``blog`` branch
and `ghp-import`__ to commit the HTML to the ``master`` branch.

GitHub Pages supports HTTPS__ as of June 2016, but not for custom domains.
There are some hacks__ but I don't feel like using them.
I'm hoping that GitHub will add support for custom domains soon.

Why HTTPS?
It's secure, it engenders trust, and `it's faster than HTTP`__.
The latter surprised me and the (big) caveat is that HTTPS's speed is due to HTTP/2,
which *requires* a secure connection using TLSv1.2.
HTTP/1.1 is indeed slower than HTTP/2.

I have never quite trained myself `not to say SSL`__,
even though Secure Sockets Layer 3.0 was released *twenty* years ago in 1996
and has long been superseded by Transport Layer Security (TLS).
And it's “HTTP Secure”, not “HTTP over SSL”.

I briefly looked at `Let's Encrypt`__ while thinking about generating a certificate.
I installed its Certbot__ tool using Homebrew
and I saw that it depended upon something called Augeas__,
which turns out to be a configuration-editing tool.
Ironically, Augeas is hosted at http://augeas.net/ [sic].
I tweeted__ about it.

__ https://posativ.org/acrylamid/
__ https://github.com/davisp/ghp-import
__ https://github.com/blog/2186-https-for-github-pages
__ https://konklone.com/post/github-pages-now-sorta-supports-https-so-use-it
__ https://scotthelme.co.uk/still-think-you-dont-need-https/
__ https://thoughtstreams.io/glyph/there-is-no-ssl/
__ https://letsencrypt.org/
__ https://certbot.eff.org/
__ http://augeas.net/
__ https://twitter.com/georgevreilly/status/770501648955211776

.. _permalink:
    /blog/2016/08/29/HTTPSforGitHubPagesCustomDomainNotYet.html
