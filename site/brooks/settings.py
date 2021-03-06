#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Arcovid-19 Brooks.
# Copyright (c) 2020, Juan B Cabral, Vanessa Daza, Diego García Lambas,
#                     Marcelo Lares, Nadia Luczywo, Dante Paz, Rodrigo Quiroga,
#                     Bruno Sanchez, Federico Stasyszyn.
# License: BSD-3-Clause
#   Full Text: https://github.com/ivco19/brooks/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

# flake8: noqa

"""Django settings for brooks project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/

"""


# =============================================================================
# SETTINGS
# =============================================================================

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHANGELOG_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "CHANGELOG.md"))

ABOUT_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "README.md"))

REQUIRED_BIN_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "required_bin.txt"))

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '_media/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iy7m=jh@n-z9r!r=0mn*d&ru_lj@#*$i2gvse69@1xrha7te$2'

# SECURITY WARNING: don't run with debug turned on in production!
PRODUCTION = os.environ.get("BROOKS_PRODUCTION", "false").lower() == "true"
DEBUG = not PRODUCTION


DEMO_MODE = os.environ.get("BROOKS_DEMO_MODE", "false").lower() == "true"


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third parties
    'django_extensions',
    'crispy_forms',
    "solo",
    'django_summernote',
    "django_tables2",

    # locals
    'brooks.apps.BrooksConfig',
    'ingest.apps.IngestConfig',
    'reporter.apps.ReporterConfig',
    'webtools.apps.WebtoolsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'brooks.middleware.DemoUserMiddleware'  # this is only used when demo
                                            # mode is True
]


ROOT_URLCONF = 'brooks.urls'

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
                "brooks.context_processors.export_some_settings",
                "ingest.context_processors.export_available_models",
            ],
        },
    },
]

WSGI_APPLICATION = 'brooks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "brooks", "static")
]


# AUTH
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'
LOGOUT_REDIRECT_URL = '/'


CACHES = {
    'default': {
        'BACKEND': 'diskcache.DjangoCache',
        'LOCATION': os.environ.get(
            "BROOKS_DISK_CACHE_LOCATION",
            os.path.join(BASE_DIR, "_cache")),
        'TIMEOUT': 300,
        # ^-- Django setting for default timeout of each key.
        'SHARDS': 8,
        'DATABASE_TIMEOUT': 0.010,  # 10 milliseconds
        # ^-- Timeout for each DjangoCache database transaction.
        'OPTIONS': {
            'size_limit': 2 ** 30   # 1 gigabyte
        },
    },
}


# CRISPY FORMS
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# EXTENSION
SHELL_PLUS = "ipython"

# djenago summer note
SUMMERNOTE_THEME = 'lite'

SUMMERNOTE_CONFIG = {
    # Or, you can set it as False to use SummernoteInplaceWidget by default -
    # no iframe mode In this case, you have to load Bootstrap/jQuery stuff by
    # manually. Use this when you're already using Bootstraip/jQuery based
    # themes.
    'iframe': False,
}

# list of sites with interesting functionalities to integrate with brooks
WEBTOOLS = {
    "Calculadora Epidémica SEIR": "https://epacalc-arg.now.sh/",
    "Covid dashboard by IBM": "https://accelerator.weather.com/bi/",
    "COVID-19 Map - Johns Hopkins Coronavirus Resource Center": "https://coronavirus.jhu.edu/map.html",
}


# dynamic model description
MODELS_DESCRIPTION = os.environ.get("BROOKS_MODELS_DECRIPTION", "")


# the list of configurations to export to the template view
TO_EXPORT = ["DEMO_MODE", "WEBTOOLS"]


# django tables-2
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

if DEBUG:
    try:
        from local_settings import *  # noqa
    except ImportError:
        import shutil
        import sys

        print("[ALERT] 'local_settings.py' not found.")

        print("[ALERT] Creating an empty one")

        org = os.path.join(BASE_DIR, "brooks", "local_settings.template")
        dest = os.path.join(BASE_DIR, "local_settings.py")
        shutil.copy(org, dest)

        print("[ALERT] Please edit 'local_settings.py'")
        print("")

        sys.exit(1)
else:
    # Configure Django App for Heroku.
    import django_heroku  # noqa
    django_heroku.settings(locals())
