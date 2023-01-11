---
title: "Display driver nvlddmkm stopped responding and has successfully recovered"
date: "2009-06-12"
permalink: "/blog/2009/06/12/DisplayDriverNvlddmkmStoppedRespondingAndHasSuccessfullyRecovered.html"
tags: [windows]
---



.. image:: /content/binary/wddm_timeout.gif
    :alt: Display driver lddmkm stopped responding and has successfully recovered
    :target: http://www.microsoft.com/whdc/device/display/wddm_timeout.mspx

This morning, the video adapters on my Vista dev box were resetting
2–3 times per *minute*.

After a pile of Windows Updates landed on my machine at 3am yesterday,
it would occasionally freeze solid for a few seconds.
Once in a while, all the monitors would go black briefly, then restore.
Each time, I would see a status update pop up from the system tray,
"Display driver nvlddmkm stopped responding and has successfully recovered."

This was irritating enough that I downloaded the latest NVidia drivers this morning,
``185.85_desktop_winvista_32bit_english_whql.exe``.
That really screwed me.
The video adapters started resetting 2–3 times per minute,
rendering the machine almost unusable.
I have two video adapters, NVidia GeForce 8600 GT and NVidia GeForce 7600 GT.

The eventlog was full of `Event ID 4101 - Display Driver Timeout Detection and Recovery`_.

I reverted to the 178.24 drivers and that helped.
When I'm not touching the machine,
the adapters only get reset every few minutes instead of several times a minute.
When I am using it, something as simple as clicking a window
to bring it to the foreground can trigger a reset.

It's very irritating but I can live with it for a little while, unlike the other.
I don't want to repave my box: apart from the time loss,
I'm not convinced that it would help if I got the same driver config all over again.

I contacted a friend at Microsoft who tried to hook me up with a driver guy,
who is unfortunately out of office.
I'm hoping that it can be fixed early next week
or my temper is going to fray rapidly.

*Update: June 19th*: See `When Video Cards Go Bad`_.

.. _Event ID 4101 - Display Driver Timeout Detection and Recovery:
    http://www.microsoft.com/whdc/device/display/wddm_timeout.mspx
.. _When Video Cards Go Bad:
    /blog/2009/06/20/WhenVideoCardsGoBad.html

.. _permalink:
    /blog/2009/06/12/DisplayDriverNvlddmkmStoppedRespondingAndHasSuccessfullyRecovered.html
