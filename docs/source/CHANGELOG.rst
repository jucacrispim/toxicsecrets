Changelog
=========

* v0.10.9

  - Fix ``create_cryto_key``: it wrote a bcrypt hash instead of an AESGCM
    key and crashed writing bytes into a text replacement. It now generates
    a real key with ``gen_key()`` and writes it as a bytes literal
  - ``crypto`` now coerces ``settings.CRYPTO_KEY`` to bytes (it may be
    defined as ``str``)

* v0.10.8

  - Call ``create_cryto_key`` from ``create`` so the ``{{CRYPTO_KEY}}``
    placeholder is replaced in the generated config

* v0.10.7

  - Fix missing ``importlib.resources`` import that broke ``create`` on a
    fresh virtualenv
  - Use ``toxiccore.cmd``'s ``main`` so the console script exits with status
    0 after ``create``

* v0.10.6

  - Print token with a stable marker
  - Remove python3.11 from CI

* v0.10.5

  - Update toxiccore

* v0.10.4

  - Update mongomotor

* v0.10.3

  - Update mongomotor

* v0.10.2

  - Fix environment creation
  - Fix packaging

* v0.10.1

  - Loosen toxiccore version

* v0.10.0

  - First version on its own repo outside toxicuild
