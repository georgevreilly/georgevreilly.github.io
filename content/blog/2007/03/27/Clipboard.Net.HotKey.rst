---
title: "Hotkey for Clipboard.NET"
date: "2007-03-27"
permalink: "/blog/2007/03/27/HotkeyForClipboardNET.html"
tags: [tech, windows]
---



.. image:: https://files.bountysource.com/system/files/LibraryEntry/144/screenshot.jpg.medium.jpg
    :alt: Clipboard.NET
    :target: https://clipmon32.bountysource.com/
    :width: 320

I use `Clipboard.NET`_ as a clipboard manager on Windows.
It stores the last few entries sent to the clipboard.

There's one problem: the default hotkey is Ctrl+Comma,
which also happens to be an important key for Outlook
(previous message).
I figured out a while ago how to `change the hotkey`_,
but my `report`_ doesn't show up when you search for it.

Net: using a key name from the `ConsoleKey table`_,
change the value of ``ShortcutKey`` in 
``%ProgramFiles%\Tom Medhurst\Clipboard.NET\clipmon32.exe.config``::

    <applicationSettings>
        <clipmon32.Properties.Settings>
              <setting name="ShortcutKey" serializeAs="String">
                      <value>OemComma</value>

The new hotkey will be Ctrl+keyname.

.. _Clipboard.NET:
    https://clipmon32.bountysource.com/
.. _change the hotkey: report_
.. _report:
    https://clipmon32.bountysource.com/task/show/1213
.. _ConsoleKey table:
    http://msdn2.microsoft.com/en-us/library/system.consolekey.aspx

.. _permalink:
    /blog/2007/03/27/HotkeyForClipboardNET.html
