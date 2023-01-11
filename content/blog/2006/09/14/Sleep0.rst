---
title: "Never Sleep(0) in an Infinite Loop"
date: "2006-09-14"
permalink: "/blog/2006/09/14/NeverSleep0InAnInfiniteLoop.html"
tags: [c-sharp, windows, til]
---



.. image:: /content/binary/infinite-loop.jpg
    :alt: Infinite Loop

I ran into a problem installing some COM+ components today. The installer
was using `Regsvcs.exe <http://msdn2.microsoft.com/en-us/library/04za0hca.aspx>`_
to register each COM+ component. I noticed after a while that the installer
wasn't making any progress and that my dual-proc system was stuck at 50%
CPU utilization. I attached a debugger to the offending process, regsvcs,
and found that it was stuck in the following infinite loop
(disassembly courtesy of `Reflector <http://www.aisto.com/roeder/dotnet/>`_):

.. code-block:: csharp

    internal void System.EnterpriseServices.CatalogSync.Wait()
    {
      if (this._set)
      {
        RegistryKey key1
          = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\Classes\CLSID");
        while (true)
        {
          int num1 = (int) key1.GetValue("CLBVersion", 0);
          if (num1 != this._version)
          {
            break;
          }
          Thread.Sleep(0);
        }
        this._set = false;
      }
    }

There are two severe problems with this code.

1. The loop should time out. There must be some reasonable limit after
    which you can incontrovertibly say that something must have gone wrong,
    and throw an exception. There has to be some way to terminate a loop.

2. Never use ``Sleep(0)`` in a loop. ``Sleep(0)`` yields the processor only
    if there's a runnable thread. If there isn't, ``Sleep(0)`` will return
    immediately. If the code is sitting in a tight loop, the net effect is
    that it will maximize the CPU until the thread's quantum is exhausted.
    There are no other runnable threads, so the scheduler immediately
    starts this thread again. This code will run until your CPU burns out.

(And, yes, I have committed both of these sins in shipping code. Why do you ask?)

I don't know what the calling code is doing or why ``CLBVersion`` isn't
being altered by some other thread or process. I had to use RegEdit to
modify this value to get the loop to terminate, whereupon RegSvcs
immediately did its work and terminated. And then it started all over
again, with the next invocation of RegSvcs on another COM+ component.
I don't know if the components are really installed properly. I had to
leave at that point.

.. _permalink:
    /blog/2006/09/14/NeverSleep0InAnInfiniteLoop.html
