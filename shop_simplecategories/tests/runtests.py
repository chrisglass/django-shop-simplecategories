#!/usr/bin/env python
import os
import sys
from django.conf import settings


DIRNAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASES={
       "default": {
           "ENGINE": "django.db.backends.sqlite3",
           "NAME": ":memory:",
       }
    },
    SOUTH_TESTS_MIGRATE=False,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'shop',
        'shop_simplecategories',
    )
)


from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['shop_simplecategories']
    parent = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..")
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
