Changelog
=========

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
