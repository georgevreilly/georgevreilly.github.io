---
title: "Shrinking PDF File Size"
date: "2016-05-26"
permalink: "/blog/2016/05/26/ShrinkingPDFFileSize.html"
tags: [tech, pdf, til]
---



Our poster designer sent me a PDF of this year's `Bloomsday poster`_.
I thought the file was too large at 7.2MB and I wanted to reduce the file size
without significant loss of image quality.
I was unable to achieve this in Preview or Acrobat Reader,
but Ghostscript did the trick,
thanks to an answer on `AskUbuntu`_::

    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
        -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH \
        -sOutputFile=output.pdf input.pdf

The results speak for themselves.

.. figure:: /content/binary/proteus-hades-01.png
    :alt: Original

    Crop of the Original PDF, size 7.2MB.

.. figure:: /content/binary/proteus-hades-02.png
    :alt: "/screen"

    Crop of ``-dPDFSETTINGS=/screen``. PDF size: 78KB

.. figure:: /content/binary/proteus-hades-03.png
    :alt: "/ebook"

    Crop of ``-dPDFSETTINGS=/ebook``. PDF size: 234KB

.. figure:: /content/binary/proteus-hades-04.png
    :alt: "/prepress"

    Crop of ``-dPDFSETTINGS=/prepress``. PDF size: 1.75MB

.. _Bloomsday poster:
    http://www.wildgeeseseattle.org/Joyce/Bloomsday/2016.html
.. _AskUbuntu:
    http://askubuntu.com/a/256449/956

.. _permalink:
    /blog/2016/05/26/ShrinkingPDFFileSize.html
