---
title: "Python: Import subclass from dynamic path"
date: "2016-03-02"
permalink: "/blog/2016/03/02/PythonImportSubclassFromDynamicPath.html"
tags: [python, til]
---



I needed to import some plugin code written in Python
from a directory whose path isn't known until runtime.
Further, I needed a class object that was a subclass of the plugin base class.

.. code:: python

    from somewhere import PluginBase

    class SomePlugin(PluginBase):
        def f1(self): ...
        def f2(self): ...

You can use the imp_ module to actually load the module from ``impl_dir``.
Note that ``impl_dir`` needs to be temporarily prepended to ``sys.path``.
Then you can find the plugin subclass using dir_ and issubclass_.

.. code:: python

    import os, imp

    def import_class(implementation_filename, base_class):
        impl_dir, impl_filename = os.path.split(implementation_filename)
        module_name, _ = os.path.splitext(impl_filename)

        try:
            sys.path.insert(0, impl_dir)
            fp, filename, description = imp.find_module(module_name)
            module = imp.load_module(module_name, fp, filename, description)
            for name in dir(module):
                obj = getattr(module, name)
                if (type(obj) == type(base_class)
                    and issubclass(obj, base_class)
                    and obj != base_class):
                        return obj
            raise ValueError("No subclass of {0} in {1}".format(
                    base_class.__name__, implementation_filename))
        finally:
            sys.path.pop(0)

.. _imp:
    https://pymotw.com/2/imp/
.. _dir:
    https://docs.python.org/2/library/functions.html#dir
.. _issubclass:
    https://docs.python.org/2/library/functions.html#issubclass

.. _permalink:
    /blog/2016/03/02/PythonImportSubclassFromDynamicPath.html
