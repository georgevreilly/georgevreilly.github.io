---
title: "CSS in Email"
date: "2009-04-16"
permalink: "/blog/2009/04/16/CSSInEmail.html"
tags: [css]
---



.. image:: /content/binary/email-css.png
    :alt: CSS support in web email clients
    :target: http://www.campaignmonitor.com/css/

I spent part of my day fighting with CSS for an email template.
CSS support is poor in both desktop and web clients,
and much worse than in current browsers.

Gmail, for example, does not support ``<style>``
in either the head or the body of HTML email.
You have to explicitly set ``style`` attributes on individual nodes.
You might as well be using ``<font>`` tags!

You can't assume that images will be downloaded,
so the mail has to make sense without them.
And forget iframes.

CampaignMonitor seems to have the `definitive guide to CSS support`_.

.. _definitive guide to CSS support:
    http://www.campaignmonitor.com/css/

.. _permalink:
    /blog/2009/04/16/CSSInEmail.html
