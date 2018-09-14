dPay - Your Starting Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick Start
-----------
You can start using the library with just a few lines of code, as seen in this quick example:

.. code-block:: python

   # first, we initialize DPay class
   from dpay import DPay
   s = DPay()

.. code-block:: python

   # check @jared's balance
   >>> s.get_account('jared')['bbd_balance']
   '980.211 BBD'

   # lets send $1.0 BBD to @jared
   >>> s.commit.transfer(to='jared', amount=1, asset='BBD', account='nomoreheroes')
   {'expiration': '2017-03-12T17:54:43',
    'extensions': [],
    'operations': [['transfer',
      {'amount': '1.000 BBD', 'from': 'nomoreheroes', 'memo': '', 'to': 'jared'}]],
    'ref_block_num': 23008,
    'ref_block_prefix': 961695589,
    'signatures': ['1f1322be9ca0c22b27c0385c929c9863901ac78cdaedea2162024ea040e22c4f8b542c02d96cbc761cbe4a188a932bc715bb7bcaf823b6739a44bb29fa85f96d2f']}

   # yup, its there
   >>> s.get_account('jared')['bbd_balance']
   '981.211 BBD'

Importing your dPay Account
============================
`dpay-python` comes with a BIP38 encrypted wallet, which holds your private keys.



Alternatively, you can also pass required WIF's to ``DPay()`` initializer.

::

    from dpay import DPay
    s = DPay(keys=['<private_posting_key>', '<private_active_key>'])

Using the encrypted wallet is however a recommended way.

Please check :doc:`cli` to learn how to set up the wallet.

Interfacing with dpayd
=======================
``DPay()`` inherits API methods from ``DPayd``, which can be called like so:

.. code-block:: python

   s = DPay()

   s.get_account('jared')
   s.get_block(8888888)
   s.get_content('author', 'permlink')
   s.broadcast_transaction(...)
   # and many more

You can see the list of available methods by calling ``help(DPay)``.
If a method is not available trough the Python API, we can call it manually using ``s.exec()``:

.. code-block:: python

   s = DPay()

   # this call
   s.get_followers('nomoreheroes', 'abit', 'blog', 10)

   # is same as
   s.exec('get_followers',
          'nomoreheroes', 'abit', 'blog', 10,
           api='follow_api')

Commit and Wallet
=================
``DPay()`` comes equipped with ``Commit`` and ``Wallet``, accessible via dot-notation.

.. code-block:: python

   s = DPay()

   # accessing Commit methods
   s.commit.transfer(...)

   # accessing Wallet methods
   s.wallet.get_active_key_for_account(...)

Please check :doc:`core` documentation to learn more.


DPay
-----

As displayed in the `Quick Start` above, ``DPay`` is the main class of this library. It acts as a gateway to other components, such as
``DPayd``, ``Commit``, ``Wallet`` and ``HttpClient``.

Any arguments passed to ``DPay`` as ``kwargs`` will naturally flow to sub-components. For example, if we initialize
DPay with ``dpay = DPay(no_broadcast=True)``, the ``Commit`` instance is configured to not broadcast any transactions.
This is very useful for testing.

.. autoclass:: dpay.dpay.DPay
   :members:


DPayd API
----------

DPayd contains API generating utilities. ``DPayd``'s methods will be automatically available to ``DPay()`` classes.
See :doc:`dpay`.

.. _dpayd-reference:

.. automodule:: dpay.dpayd
   :members:


Setting Custom Nodes
--------------------

There are 3 ways in which you can set custom ``dpayd`` nodes to use with ``dpay-python``.

**1. Global, permanent override:**
You can use ``dpaycli set nodes`` command to set one or more node URLs. The nodes need to be separated with comma (,)
and shall contain no whitespaces.

    ::

        ~ % dpaycli config
        +---------------------+--------------+
        | Key                 |     Value    |
        +---------------------+--------------+
        | default_vote_weight | 100          |
        | default_account     | nomoreheroes |
        +---------------------+--------------+
        ~ % dpaycli set nodes https://dpayd.dpays.io/
        ~ % dpaycli config
        +---------------------+-------------------------------+
        | Key                 | Value                         |
        +---------------------+-------------------------------+
        | default_account     | nomoreheroes                  |
        | default_vote_weight | 100                           |
        | nodes               | https://dpayd.dpays.io/           |
        +---------------------+-------------------------------+
        ~ % dpaycli set nodes https://dpayd.dpays.io/,https://dpayd.dpays.io
        ~ % dpaycli config
        +---------------------+----------------------------------------------------------+
        | Key                 | Value                                                    |
        +---------------------+----------------------------------------------------------+
        | nodes               | https://dp/,https://dpayd.dpays.io        |
        | default_vote_weight | 100                                                      |
        | default_account     | nomoreheroes                                             |
        +---------------------+----------------------------------------------------------+
        ~ %


To reset this config run ``dpaycli set nodes ''``.

**2. For Current Python Process:**
You can override default `DPayd` instance for current Python process, by overriding the `instance` singleton.
You should execute the following code when your program starts, and from there on out, all classes (Blockchain, Account,
Post, etc) will use this as their default instance.

    ::

        from dpay.dpayd import DPayd
        from dpay.instance import set_shared_dpayd_instance

        dpayd_nodes = [
            'https://dpayd.dpays.io',
            'https://dpayd.dpays.io',
        ]
        set_shared_dpayd_instance(DPayd(nodes=dpayd_nodes))


**3. For Specific Class Instance:**
Every class that depends on dpayd comes with a ``dpayd_instance`` argument.
You can override said dpayd instance, for any class you're initializing (and its children).

This is useful when you want to contain a modified ``dpayd`` instance to an explicit piece of code (ie. for testing).

    ::

        from dpay.dpayd import DPayd
        from dpay.account import Account
        from dpay.Blockchain import Blockchain

        dpayd_nodes = [
            'https://dpayd.dpays.io',
            'https://dpayd.dpays.io',
        ]
        custom_instance = DPayd(nodes=dpayd_nodes)

        account = Account('nomoreheroes', dpayd_instance=custom_instance)
        blockchain = Blockchain('head', dpayd_instance=custom_instance)
