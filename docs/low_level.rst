Low Level
~~~~~~~~~

HttpClient
----------

A fast ``urllib3`` based HTTP client that features:

* Connection Pooling
* Concurrent Processing
* Automatic Node Failover

The functionality of ``HttpClient`` is encapsulated by ``Crea`` class. You shouldn't be using ``HttpClient`` directly,
unless you know exactly what you're doing.

.. autoclass:: creabase.http_client.HttpClient
   :members:

-------------

creabase
---------

creabase contains various primitives for building higher level abstractions.
This module should only be used by library developers or people with deep domain knowledge.

**Warning:**
Not all methods are documented. Please see source.

.. image:: https://i.imgur.com/A9urMG9.png

Account
=======

.. automodule:: creabase.account
   :members:

--------

Base58
======

.. automodule:: creabase.base58
   :members:

--------

Bip38
=====

.. automodule:: creabase.bip38
   :members:


--------

Memo
====

.. automodule:: creabase.memo
   :members:


--------

Operations
==========

.. automodule:: creabase.operations
   :members:


--------

Transactions
============

.. automodule:: creabase.transactions
   :members:



--------

Types
=====

.. automodule:: creabase.types
   :members:

--------

Exceptions
==========

.. automodule:: creabase.exceptions
   :members:
