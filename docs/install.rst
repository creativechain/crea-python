************
Installation
************

`dpay-python` requires Python 3.5 or higher. We don't recommend usage of Python that ships with OS.
If you're just looking for a quick and easy cross-platform solution, feel free to install Python 3.x via easy to use
`Anaconda <https://www.continuum.io/downloads>`_ installer.


Afterwards, you can install `dpay-python` with `pip`:

::

    $ pip install dpay

You can also perform the installation manually using `setup.py`:

::

    $ git clone https://github.com/dpays/dpay-python
    $ cd dpay-python
    $ make install

Upgrade
#######

::

   $ pip install -U dpay



Namespace Collision
===================

If you have used a dpaypy stack before v0.5, please remove it before installing official version of ``dpay-python``.

::

   curl https://raw.githubusercontent.com/dpays/dpay-python/master/scripts/nuke_legacy.sh | sh
