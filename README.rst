.. -*- mode: rst -*-

.. image:: https://img.shields.io/pypi/v/pybitflyer.svg?maxAge=2592000   :target:

.. image:: https://img.shields.io/pypi/dd/pybitflyer.svg?maxAge=2592000   :target:

bfex
==========

``bfex`` is a python wrapper for bitFlyer's REST API.

Usage
-----

.. code:: python

  import pybitflyer
  api = pybitflyer.API(api_key="xxx...", api_secret="yyy...")

If you use HTTP Public API, API Key and API Secret can be omitted.

Example
-------

Order Book
~~~~~~~~~~

.. code:: python

  api.board(product_code="BTC_JPY")

Ticker
~~~~~~

.. code:: python

  api.ticker(product_code="BTC_JPY")
