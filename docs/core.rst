Transactions and Accounts
~~~~~~~~~~~~~~~~~~~~~~~~~

Commit
======

The Commit class contains helper methods for `posting, voting, transferring funds, updating witnesses` and more.
You don't have to use this class directly, all of its methods are accessible trough main ``DPay`` class.

.. code-block:: python

   # accessing commit methods trough DPay
   s = DPay()
   s.commit.transfer(...)

   # is same as
   c = Commit(dpay=DPay())
   c.transfer(..)

.. autoclass:: dpay.dpay.Commit
   :members:

--------


TransactionBuilder
==================

.. autoclass:: dpay.transactionbuilder.TransactionBuilder
   :members:

--------

Wallet
======

Wallet is a low-level utility.
It could be used to create 3rd party cli and GUI wallets on top of ``dpay-python``'s infrastructure.

.. automodule:: dpay.wallet
   :members:
