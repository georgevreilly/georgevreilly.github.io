---
title: "USB 3 Drivers on a Lenovo E545"
date: "2015-12-09"
permalink: "/blog/2015/12/09/USB3DriversLenovoE545.html"
tags: [linux]
---



.. image:: https://upload.wikimedia.org/wikipedia/commons/7/7e/USB_3.0_A_Buchse_13.jpg
    :alt: USB 3
    :target: https://en.wikipedia.org/wiki/USB_3.0
    :width: 200
    :class: right-float

Emma's been complaining for some time that USB devices only worked in one port
on her Lenovo E545 laptop.
The USB 2 port worked;
the `USB 3 <https://en.wikipedia.org/wiki/USB_3.0>`_ ports didn't.

I took a look at `Device Manager <http://www.howtogeek.com/167094/how-to-use-the-windows-device-manager-for-troubleshooting/>`_,
and I noticed that most of the USB nodes looked wrong.
She went to the Lenovo website and downloaded two USB-related drivers,
the AMD USB Filter Driver and the AMD USB 3.0 Driver.
Between them, they fixed the problem and she now has all ports working.

This machine is running Windows 7.
At some point, she wiped the machine to get rid of Lenovo crapware,
and installed a clean copy of Windows 7.
She downloaded a pile of drivers from Lenovo at the time,
but the USB drivers must have been overlooked.

.. _permalink:
    /blog/2015/12/09/USB3DriversLenovoE545.html
