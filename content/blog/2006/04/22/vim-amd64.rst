---
title: "Win64 port of Vim"
date: "2006-04-22"
permalink: "/blog/2006/04/22/Win64PortOfVim.html"
tags: [vim, windows]
---



I've ported Vim to Win64. Native binaries for AMD64 can be found on my
`Vim page <//www.georgevreilly.com/vim/>`_.

In the end, it wasn't all that hard. Last weekend, I fixed approximately
400 warnings that were thrown up by the x86_amd64 cross compiler.
Most of them were due to the widening of ``size_t`` (especially the value
returned from ``strlen()``) and ``ptrdiff_t`` to 64\-bits.
Several years ago, I went through a similar exercise in fixing these
warnings for Vim6, but I never finished the port.

This week, I scrounged access to an AMD64 box at work. Today, I turned on
the `/Wp64 flag <http://msdn2.microsoft.com/en-us/library/yt4xw8fh(VS.80).aspx>`_,
which found several new, subtler problems, where pointers where being
truncated to ``__int32``\ s or conversely
``__int32``\ s were being widened to
pointers. Judicious introduction of (the equivalent of) ``(INT_PTR)`` casts
fixed most of those.

At that point, I tried running the binary. It refused to start!
After a few detours, I had `WinDbg
<http://www.microsoft.com/whdc/devtools/debugging/default.mspx>`_
installed, and ran gvim under WinDbg. That showed that the error was 14001
(ERROR_SXS_CANT_GEN_ACTCTX, "The application has failed to start because its
side-by-side configuration is incorrect. Please see the application event
log for more detail.") The event log showed nothing.

After more investigation, I found a WinSxS manifest for the Windows Common
Controls:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
      <assemblyIdentity
        processorArchitecture="X86"
        version="6.2.0.0"
        type="win32"
        name="Vim"
      />
      <description>Vi Improved - A Text Editor</description>
      <dependency>
        <dependentAssembly>
          <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            publicKeyToken="6595b64144ccf1df"
            language="*"
            processorArchitecture="X86"
          />
        </dependentAssembly>
      </dependency>
    </assembly>

Once the two instances of ``processorArchitecture="X86"`` were set to
``processorArchitecture="AMD64"``, Vim started working without a hitch.
Despite my naïve expectations, none of the other fields in the comctl32
assembly needed to be changed.

.. _permalink:
    /blog/2006/04/22/Win64PortOfVim.html
