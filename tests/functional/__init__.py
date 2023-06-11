# -*- coding: utf-8 -*-

import os
import sys
from unittest import TestCase

from tests import TEST_DATA_DIR

PYVERSION = ''.join([str(n) for n in sys.version_info[:2]])
REPO_DIR = os.path.join(TEST_DATA_DIR, 'repo')
SLAVE_ROOT_DIR = TEST_DATA_DIR
SOURCE_DIR = os.path.join(TEST_DATA_DIR, '..')
TOXICSECRETS_CMD = os.path.join(SOURCE_DIR, 'toxicsecrets', 'cmds.py')

toxicsecrets_conf = os.environ.get('TOXICSECRETS_SETTINGS')
if not toxicsecrets_conf:
    toxicsecrets_conf = os.path.join(SLAVE_ROOT_DIR, 'toxicsecrets.conf')
    os.environ['TOXICSECRETS_SETTINGS'] = toxicsecrets_conf


class BaseFunctionalTest(TestCase):
    """An AsyncTestCase that a slave process on
    setUpClass and stops it on tearDownClass"""

    @classmethod
    def start_secrets(cls):
        start_secrets()

    @classmethod
    def stop_secrets(cls):
        stop_secrets()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.start_secrets()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.stop_secrets()


def start_secrets():
    """Starts an slave server in a new process for tests"""

    toxicsecrets_conf = os.environ.get('TOXICSECRETS_SETTINGS')
    pidfile = 'toxicsecrets{}.pid'.format(PYVERSION)
    cmd = ['export', 'PYTHONPATH="{}"'.format(SOURCE_DIR), '&&', 'python',
           TOXICSECRETS_CMD, 'start', SLAVE_ROOT_DIR, '--daemonize',
           '--pidfile', pidfile, '--loglevel', 'debug']

    if toxicsecrets_conf:
        cmd += ['-c', toxicsecrets_conf]

    print(' '.join(cmd))
    os.system(' '.join(cmd))


def stop_secrets():
    """Stops the test slave"""
    pidfile = 'toxicsecrets{}.pid'.format(PYVERSION)
    cmd = ['export', 'PYTHONPATH="{}"'.format(SOURCE_DIR), '&&',
           'python', TOXICSECRETS_CMD, 'stop', SLAVE_ROOT_DIR,
           '--pidfile', pidfile, '--kill']

    os.system(' '.join(cmd))
