Toxicslave config
=================

The configuration of toxicsecrets is done using the a configuration file. The configuration
file can be passed using the  ``-c`` flag to the ``toxicsecrets`` command
or settings the environment variable ``TOXICSECRETS_SETTINGS``.

This file is a python file, so do what ever you want with it.

Config values
-------------

.. note::

   Although the config is done using a config file, the default
   configuration file created by ``toxicsecrets create`` can use
   environment variables instead.


* ``PORT`` - The port for the server to listen. Defaults to `7777`.
  Environment variable: ``SECRETS_PORT``

* ``USE_SSL`` - Defaults to False.
  Environment variable: ``SECRETS_USE_SSL``. Possible values are `0` or `1`.

* ``CERTIFILE`` - Path for a certificate file.
  Environment variable: ``SECRETS_CERTIFILE``

* ``KEYFILE`` - Path for a key file.
  Environment variable: ``SECRETS_KEYFILE``

* ``ACCESS_TOKEN`` - An sha512 encrypted string used to authenticate an
  incomming request.
  Environment variable: ``SECRETS_ENCRYPTED_TOKEN``.

.. note::

   You can create a new access token using the ``toxicsecrets create_token``
   command. For more information use:

   .. code-block:: sh

       $ toxicsecrets create_token --help


* ``CRYPTO_KEY`` - A random generated key for encrypting secrets.
  Environment variable: ``SECRETS_CRYPTO_KEY``.

.. note::

   You can create a new crypto_key using the ``toxicsecrets create_crypto_key``
   command. For more information use:

   .. code-block:: sh

       $ toxicsecrets create_crypto_key --help


* ``DBHOST`` - Host for the database connection.
  Environment variable: ``SECRETS_DBHOST``.

* ``DBPORT`` - Port for the database connection. Defaults to `27017`.
  Environment variable: ``SECRETS_DBPORT``.

* ``DBNAME`` - The database name. Defaults to `toxicsecrets`.
  Environment variable: ``SECRETS_DBNAME``

* ``DBUSER`` - User name for authenticated access to the database
  Environment variable: ``SECRETS_DBUSER``

* ``DBPASS`` - Password for authenticated access to the database
  Environment variable: ``SECRETS_DBPASS``
