Low Level
~~~~~~~~~

HttpClient
----------

A fast ``urllib3`` based HTTP client that features:

* Connection Pooling
* Concurrent Processing
* Automatic Node Failover

The functionality of ``HttpClient`` is encapsulated by ``DPay`` class. You shouldn't be using ``HttpClient`` directly,
unless you know exactly what you're doing.

.. autoclass:: dpaybase.http_client.HttpClient
   :members:

-------------

dpaybase
---------

dpaybase contains various primitives for building higher level abstractions.
This module should only be used by library developers or people with deep domain knowledge.

**Warning:**
Not all methods are documented. Please see source.

.. image:: https://i.imgur.com/A9urMG9.png

Account
=======

.. automodule:: dpaybase.account
   :members:

--------

Base58
======

.. automodule:: dpaybase.base58
   :members:

--------

Bip38
=====

.. automodule:: dpaybase.bip38
   :members:


--------

Memo
====

.. automodule:: dpaybase.memo
   :members:


--------

Operations
==========

.. automodule:: dpaybase.operations
   :members:


--------

Transactions
============

.. automodule:: dpaybase.transactions
   :members:



--------

Types
=====

.. automodule:: dpaybase.types
   :members:

--------

Exceptions
==========

.. automodule:: dpaybase.exceptions
   :members:
