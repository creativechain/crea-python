************
Installation
************

`crea-python` requires Python 3.5 or higher. We don't recommend usage of Python that ships with OS.
If you're just looking for a quick and easy cross-platform solution, feel free to install Python 3.x via easy to use
`Anaconda <https://www.continuum.io/downloads>`_ installer.


Afterwards, you can install `crea-python` with `pip`:

::

    $ pip install crea

You can also perform the installation manually using `setup.py`:

::

    $ git clone https://github.com/creativechain/crea-python
    $ cd crea-python
    $ make install

Upgrade
#######

::

   $ pip install -U crea



Namespace Collision
===================

If you have used a creapy stack before v0.5, please remove it before installing official version of ``crea-python``.

::

   curl https://raw.githubusercontent.com/creas/crea-python/master/scripts/nuke_legacy.sh | sh
