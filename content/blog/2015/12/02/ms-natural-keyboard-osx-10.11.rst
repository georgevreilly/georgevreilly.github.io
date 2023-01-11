---
title: "Microsoft Natural Keyboard 4000 on Mac OS X 10.11: Alt/Windows key no longer swapped"
date: "2015-12-02"
permalink: "/blog/2015/12/02/MSNaturalKeyboardOSXElCapitanSwapWindowsAltKeys.html"
tags: [mac]
---



When I upgraded my home and work MacBooks to
`OS X 10.11 (El Capitan) <https://en.wikipedia.org/wiki/OS_X_El_Capitan>`_,
the single biggest annoyance for me was that my external keyboards,
all `Microsoft Natural Keyboard 4000`_\ s,
no longer swapped the Alt & Windows key.

.. image:: /content/binary/windows-keyboard.jpg
    :alt: Windows Keyboard
    :class: right-float

.. image:: /content/binary/mackeyboard_zoom.jpg
    :alt: Mac Keyboard
    :class: right-float

By default, when a PC keyboard is plugged into a Mac,
the Alt key,
which is immediately to the left of the spacebar,
is mapped to the Alt/Option key,
which is two keys left of the spacebar on a Mac keyboard.
And the Windows key,
which is two keys to the left of the spacebar on a PC keyboard,
is mapped to the Command key,
which is next to the spacebar on a Mac keyboard.

On a Mac, the Command modifier is heavily used for keyboard shortcuts,
while the Alt/Option modifier is hardly used at all.
On a Windows machine, the Alt modifier is heavily used,
while the Windows key is not.
In other words,
if you're touch typing rather than looking at the legends on the keycaps,
you will find a naively mapped PC keyboard's layout annoying
if you're used to a Mac keyboard.
On both PC and Mac keyboards, you will find various modifier keys to the right of the spacebar;
I never use them.

In versions of Mac OS X before 10.11,
Microsoft's Intellitype_ software remapped the Alt & Windows keys,
so that the key labeled Alt, just to the left of the spacebar, became the Command key,
while the Windows key acted as the Alt/Options key.
It also enabled a lot of other functionality,
such as volume control and scrolling,
but I never ever bothered with that.
All I cared about was that I could type with equal facility
on my Mac laptop's keyboard and on my external MS keyboard.
And I couldn't when the key that acted as Command wasn't just to the left of the spacebar.

I asked a question about it on the `Microsoft Answers Forum`_.
I was referred to the `Apple Support Communities`_.
I was told that the reason that the Intellitype software no longer worked
was likely due to security changes in El Capitan.

I got two useful suggestions:

1. Go to System Preferences > Keyboard > Modifier Keys.
   Swap the Option and Command keys.
2. Install Karabiner_.

The first suffices for me since I don't care about the other features of the Natural Keyboard.

.. _Microsoft Natural Keyboard 4000:
    https://www.microsoft.com/accessories/en-us/products/keyboards/natural-ergonomic-keyboard-4000/b2m-00012
.. _Intellitype:
    https://www.microsoft.com/hardware/en-us/d/wireless-comfort-keyboard-for-mac

.. _Natural Keyboard 4000 on Mac OS X 10.11: Alt/Windows key no longer swapped:
.. _Microsoft Answers Forum:
    http://answers.microsoft.com/en-us/mac/forum/macofficepreview-macstart/natural-keyboard-4000-on-mac-os-x-1011-altwindows/c20b94ab-4341-4f5d-ba61-87370f2b8e91

.. _Microsoft Natural Keyboard 4000 on Mac OS X 10.11: Alt/Windows key no longer swapped:
.. _Apple Support Communities:
    https://discussions.apple.com/message/29052150

.. _Karabiner:
    https://pqrs.org/osx/karabiner/

.. _permalink:
    /blog/2015/12/02/MSNaturalKeyboardOSXElCapitanSwapWindowsAltKeys.html
