#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4
# pylint: disable=C0103

"""
TestRunner
"""

import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner
from coverage import coverage


"""
import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
"""


if __name__ == "__main__":
    """
    https://www.programcreek.com/python/example/97413/django.test.utils.get_runner
    """
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()
    TestRunner = get_runner(settings)
    testRunner = TestRunner()
    # Setup Coverage
    cov = coverage(source=["opa"], omit=[
        "opa/__init__.py",
        "opa/admin.py",
        "opa/migrations/__init__.py",
    ])
    cov.start()

    failures = testRunner.run_tests(["opa"])
    if bool(failures):
            cov.erase()
            sys.exit("Tests Failed. Coverage Cancelled.")

    # If success show coverage results
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='covhtml')
    sys.exit(bool(failures))
