Crea - Your Starting Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick Start
-----------
You can start using the library with just a few lines of code, as seen in this quick example:

.. code-block:: python

   # first, we initialize Crea class
   from crea import Crea
   s = Crea()

.. code-block:: python

   # check @jared's balance
   >>> s.get_account('jared')['cbd_balance']
   '980.211 CBD'

   # lets send $1.0 CBD to @jared
   >>> s.commit.transfer(to='jared', amount=1, asset='CBD', account='nomoreheroes')
   {'expiration': '2017-03-12T17:54:43',
    'extensions': [],
    'operations': [['transfer',
      {'amount': '1.000 CBD', 'from': 'nomoreheroes', 'memo': '', 'to': 'jared'}]],
    'ref_block_num': 23008,
    'ref_block_prefix': 961695589,
    'signatures': ['1f1322be9ca0c22b27c0385c929c9863901ac78cdaedea2162024ea040e22c4f8b542c02d96cbc761cbe4a188a932bc715bb7bcaf823b6739a44bb29fa85f96d2f']}

   # yup, its there
   >>> s.get_account('jared')['cbd_balance']
   '981.211 CBD'

Importing your Crea Account
============================
`crea-python` comes with a BIP38 encrypted wallet, which holds your private keys.



Alternatively, you can also pass required WIF's to ``Crea()`` initializer.

::

    from crea import Crea
    s = Crea(keys=['<private_posting_key>', '<private_active_key>'])

Using the encrypted wallet is however a recommended way.

Please check :doc:`cli` to learn how to set up the wallet.

Interfacing with cread
=======================
``Crea()`` inherits API methods from ``Cread``, which can be called like so:

.. code-block:: python

   s = Crea()

   s.get_account('jared')
   s.get_block(8888888)
   s.get_content('author', 'permlink')
   s.broadcast_transaction(...)
   # and many more

You can see the list of available methods by calling ``help(Crea)``.
If a method is not available trough the Python API, we can call it manually using ``s.exec()``:

.. code-block:: python

   s = Crea()

   # this call
   s.get_followers('nomoreheroes', 'abit', 'blog', 10)

   # is same as
   s.exec('get_followers',
          'nomoreheroes', 'abit', 'blog', 10,
           api='follow_api')

Commit and Wallet
=================
``Crea()`` comes equipped with ``Commit`` and ``Wallet``, accessible via dot-notation.

.. code-block:: python

   s = Crea()

   # accessing Commit methods
   s.commit.transfer(...)

   # accessing Wallet methods
   s.wallet.get_active_key_for_account(...)

Please check :doc:`core` documentation to learn more.


Crea
-----

As displayed in the `Quick Start` above, ``Crea`` is the main class of this library. It acts as a gateway to other components, such as
``Cread``, ``Commit``, ``Wallet`` and ``HttpClient``.

Any arguments passed to ``Crea`` as ``kwargs`` will naturally flow to sub-components. For example, if we initialize
Crea with ``crea = Crea(no_broadcast=True)``, the ``Commit`` instance is configured to not broadcast any transactions.
This is very useful for testing.

.. autoclass:: crea.crea.Crea
   :members:


Cread API
----------

Cread contains API generating utilities. ``Cread``'s methods will be automatically available to ``Crea()`` classes.
See :doc:`crea`.

.. _cread-reference:

.. automodule:: crea.cread
   :members:


Setting Custom Nodes
--------------------

There are 3 ways in which you can set custom ``cread`` nodes to use with ``crea-python``.

**1. Global, permanent override:**
You can use ``creacli set nodes`` command to set one or more node URLs. The nodes need to be separated with comma (,)
and shall contain no whitespaces.

    ::

        ~ % creacli config
        +---------------------+--------------+
        | Key                 |     Value    |
        +---------------------+--------------+
        | default_vote_weight | 100          |
        | default_account     | nomoreheroes |
        +---------------------+--------------+
        ~ % creacli set nodes https://cread.creativechain.net/
        ~ % creacli config
        +---------------------+-------------------------------+
        | Key                 | Value                         |
        +---------------------+-------------------------------+
        | default_account     | nomoreheroes                  |
        | default_vote_weight | 100                           |
        | nodes               | https://cread.creativechain.net/           |
        +---------------------+-------------------------------+
        ~ % creacli set nodes https://cread.creativechain.net/,https://cread.creativechain.net
        ~ % creacli config
        +---------------------+----------------------------------------------------------+
        | Key                 | Value                                                    |
        +---------------------+----------------------------------------------------------+
        | nodes               | https://dp/,https://cread.creativechain.net        |
        | default_vote_weight | 100                                                      |
        | default_account     | nomoreheroes                                             |
        +---------------------+----------------------------------------------------------+
        ~ %


To reset this config run ``creacli set nodes ''``.

**2. For Current Python Process:**
You can override default `Cread` instance for current Python process, by overriding the `instance` singleton.
You should execute the following code when your program starts, and from there on out, all classes (Blockchain, Account,
Post, etc) will use this as their default instance.

    ::

        from crea.cread import Cread
        from crea.instance import set_shared_cread_instance

        cread_nodes = [
            'https://cread.creativechain.net',
            'https://cread.creativechain.net',
        ]
        set_shared_cread_instance(Cread(nodes=cread_nodes))


**3. For Specific Class Instance:**
Every class that depends on cread comes with a ``cread_instance`` argument.
You can override said cread instance, for any class you're initializing (and its children).

This is useful when you want to contain a modified ``cread`` instance to an explicit piece of code (ie. for testing).

    ::

        from crea.cread import Cread
        from crea.account import Account
        from crea.Blockchain import Blockchain

        cread_nodes = [
            'https://cread.creativechain.net',
            'https://cread.creativechain.net',
        ]
        custom_instance = Cread(nodes=cread_nodes)

        account = Account('nomoreheroes', cread_instance=custom_instance)
        blockchain = Blockchain('head', cread_instance=custom_instance)
