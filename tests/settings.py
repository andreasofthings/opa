#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4

SECRET_KEY = 'fake-key'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test.db"
    }
}
USE_TZ=True
INSTALLED_APPS = [
    "opa",
    "tests",
]
