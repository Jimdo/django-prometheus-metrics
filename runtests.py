#!/usr/bin/env python
import os
import sys

import django

from django.conf import settings


DEFAULT_SETTINGS = dict(
    DEBUG = False,

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },

    SITE_ID = 1,

    MIDDLEWARE = [
        'django_prometheus.middleware.PrometheusBeforeMiddleware',
        'django.middleware.common.CommonMiddleware',
    ],

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django_prometheus': {
                'handlers': ['console'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            },
        },
    },

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.admin',
        'django_prometheus',
    ],

    ROOT_URLCONF = 'django_prometheus.urls',

    USE_TZ = True,

    PROMETHEUS_METRICS_PORT = 8000
)


def runtests(*test_args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        if not test_args:
            test_args = ["django_prometheus.tests"]
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        if not test_args:
            test_args = ["tests"]

    failures = runner_class(verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)

if __name__ == "__main__":
    runtests(*sys.argv[1:])