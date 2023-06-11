:tocdepth: 1

Toxicsecrets: secrets management for toxicbuild
===============================================

Toxicsecrets is a server that manages secrets for toxicbuild. Secrets are
encrypted using `AESGCM <https://cryptography.io/en/latest/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM>`_
and then saves it to database. Toxicsecrets uses mongo as database.

Install
-------

To install it use pip:

.. code-block:: sh

   $ pip install toxicsecrets



Setup & config
--------------

Before executing builds you must create an environment for toxicsecrets.
To do so use:

.. code-block:: sh

   $ toxicsecrets create ~/secrets-env

This is going to create a ``~/secrets-env`` directory with a ``toxicsecrets.conf``
file in it. This file is used to configure toxicsecrets.

Check the configuration instructions for details

.. toctree::
   :maxdepth: 1

   config


Run the server
--------------

When the configuration is done you can run the server with:

.. code-block:: sh

   $ toxicsecrets start ~/secrets-env


For all options for the toxicsecrets command execute

.. code-block:: sh

   $ toxicsecrets --help


Secrets server API
==================

With the server running you can store and retrieve secrets. Check the
api documentation for details

.. toctree::
   :maxdepth: 1

   secrets_api.rst


CHANGELOG
---------

.. toctree::
   :maxdepth: 1

   CHANGELOG
