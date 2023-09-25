---
title: "Random Fade"
# date: 2021-11-27 22:52
tags: [programming]
permalink: "/__drafts/2023/mm/dd/RandomFade.html"
filter: markdown+fenced_code+codehilite
draft: true
---

**Summary**: An efficient technique for *randomly fading in*
a picture using Linear Congruential Generators.

## Inadequate Approaches to Random Fades

How would you *fade in* a picture *randomly*?

Here's a naive and deeply flawed HTML/TypeScript approach
to making a picture gradually and randomly appear.

```typescript
// Terrible approach
function randomFade(canvasId: string, image: HTMLImageElement) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext("2d");
    
    while (!finished()) {
        const x = Math.floor(canvas.width * Math.random());
        const y = Math.floor(canvas.height * Math.random());
        ctx.drawImage(image, x, y, 1, 1); // one pixel
    }
}
```

You can make this a bit faster
by copying more than one pixel at a time, say, 4x4,
but that would complicate the simple algorithm above.

Several questions arise:

* What's to prevent you from visiting some pixels
  over and over again? (Inefficiency.)
* How do you know if you ever visit a particular pixel?
* How do you know when you are finished? That all pixels have been visited?

One way to make the loop terminate is
to keep an auxiliary data structure, one bit per pixel.
Whenever a pixel has been copied,
the corresponding bit is set
and a counter is decremented.
If you've passed a certain time threshold,
you can walk through the bitmap
to copy all the remaining pixels.
This is obviously horrible.

A better approach would be to
*shuffle* the coordinates of the pixels,
using something like [Fisher-Yates]:

[Fisher-Yates]: https://bost.ocks.org/mike/shuffle/

```typescript
// Somewhat better approach
function randomFade(canvasId: string, image: HTMLImageElement) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext("2d");
    const offsets: number[] = [];

    for (let y = 0; y < canvas.height; y++) {
      for (let x = 0; x < canvas.width; x++) {
        const offset = y * canvas.width + x;
        offsets.push(offset);
      }
    }

    offsets = shuffle(offsets);

    for (let offset of offsets) {
      const x = offset % canvas.width;
      const y = (offset - x) / canvas.width; // integer
      ctx.drawImage(image, x, y, 1, 1); // one pixel
    }
```

This should work.
Its big drawback is *memory usage*:
the length of the `offsets` array
is equal to the area of the image in pixels.
I computed a single number, `offset`,
rather than an `[x, y]` pair to halve the amount of memory used,
but it's still significant for a multi-megapixel image.
It can be reduced somewhat by copying larger regions,
say 2x2 or 4x4.

When I first tackled this problem, almost thirty years ago,
the memory usage of the `shuffle` approach was unacceptable.

## Random Fades in 1994

I spent several months in 1994
working on a team developing an IBM 3270 terminal emulator
that targeted Windows 3.1,
a 16-bit operating system.
Most of our users would have had a 386 or a 486,
probably with at most 4MB of RAM,
one-thousandth the memory of a modern computer.
MS-DOS was still very common,
but we didn't have to worry about that.
Pentiums were rare and expensive.
Windows 95, the first consumer 32-bit Windows,
was a year in the future.
We were developing on Windows NT 3.1, another 32-bit Windows,
but very few of our users were using NT.

I mostly worked on the installer.
To make the installation more visually interesting,
we wanted the initial [splash screen] image to *fade in*.
It was easy enough to make the image appear
in a deterministic fashion,
one row or one column at a time.

I wanted to make the image appear in random order,
but the approaches that initially occurred to me
didn't work well in those memory-constrained systems.
I don't remember the dimension of the splash screen image,
but it was probably 640x480.

I was at a loss at how to do it efficiently
until a dim memory of reading about
[linear congruential generator]s
in Knuth's *Seminumerical Algorithms* surfaced.

[splash screen]: https://en.wikipedia.org/wiki/Splash_screen
[linear congruential generator]: https://en.wikipedia.org/wiki/Linear_congruential_generator


## Linear Congruential Generator

LCG:

<em>X</em><sub><em>n</em>+1</sub> = (<em>aX</em><sub><em>n</em></sub> + <em>c</em>) mod <em>m</em>

Stuff

<iframe height="360" style="width: 100%;" scrolling="no" title="LCG animation" src="https://codepen.io/georgevreilly/embed/NWvmwwv?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/georgevreilly/pen/NWvmwwv">
  LCG animation</a> by George V. Reilly (<a href="https://codepen.io/georgevreilly">@georgevreilly</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

# More stuff

<iframe height="480" style="width: 100%;" scrolling="no" title="Random FadeCell Diagram" src="https://codepen.io/georgevreilly/embed/eYGOgbW?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/georgevreilly/pen/eYGOgbW">
  Random FadeCell Diagram</a> by George V. Reilly (<a href="https://codepen.io/georgevreilly">@georgevreilly</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

paragraph 1

<iframe height="520" style="width: 100%;" scrolling="no" title="Random Fade"
src="https://codepen.io/georgevreilly/embed/PoKrPor?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/georgevreilly/pen/PoKrPor">
  Random Fade</a> by George V. Reilly (<a href="https://codepen.io/georgevreilly">@georgevreilly</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>
paragraph 2

<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
