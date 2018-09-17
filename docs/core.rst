Transactions and Accounts
~~~~~~~~~~~~~~~~~~~~~~~~~

Commit
======

The Commit class contains helper methods for `posting, voting, transferring funds, updating witnesses` and more.
You don't have to use this class directly, all of its methods are accessible trough main ``Crea`` class.

.. code-block:: python

   # accessing commit methods trough Crea
   s = Crea()
   s.commit.transfer(...)

   # is same as
   c = Commit(crea=Crea())
   c.transfer(..)

.. autoclass:: crea.crea.Commit
   :members:

--------


TransactionBuilder
==================

.. autoclass:: crea.transactionbuilder.TransactionBuilder
   :members:

--------

Wallet
======

Wallet is a low-level utility.
It could be used to create 3rd party cli and GUI wallets on top of ``crea-python``'s infrastructure.

.. automodule:: crea.wallet
   :members:
