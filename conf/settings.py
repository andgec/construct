"""
Django settings for co_manager project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
#from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't(auwl)iz9o_ovf6lstrql_w)9kt@6(m_nw_nn5r3&nyvdv_!%'

RUNTIME_ENV = os.environ.get('RUNTIME_ENV', 'local')

LOCAL_ENV = RUNTIME_ENV not in ('PROD', 'PRODUCTION', 'PROD-DEBUG', 'STAGING', 'DEV')



# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = str(os.environ.get('DEBUG', RUNTIME_ENV not in ('PROD', 'PRODUCTION'))).lower() in ('true', '1')

ALLOWED_HOSTS = ['127.0.0.1', '10.0.0.111', os.environ.get('WEB_HOST', 'localhost')]

INTERNAL_IPS=['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_select2',
    'parler',
    'wkhtmltopdf',
    'djauth',
    'inventory',
    'general',
    'receivables',
    'salary',
    'reports'
]

APP_ORDER = [
        'djauth',
        'general',
        'salary',
        'inventory',
        'receivables',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Localization
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'co_manager.urls'

AUTH_USER_MODEL = 'djauth.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',                
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
'''
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
)
'''
WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#authent-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'lt'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES=(
    ('nb', 'Norwegian Bokmål'),
    ('lt', 'Lithuanian'),
    ('en', 'English'),
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'nb',},
        {'code': 'lt',},
        {'code': 'en',},
    ),
    'default': {
        'fallback': 'lt',             # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}

LOCALE_PATHS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale'),
)

MAX_DIGITS_PRICE        = 14
MAX_DIGITS_CURRENCY     = 14
MAX_DIGITS_QTY          = 14

DECIMAL_PLACES_PRICE    = 4
DECIMAL_PLACES_CURRENCY = 2
DECIMAL_PLACES_QTY      = 3

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

LOGIN_REDIRECT_URL = '/'

TIMELIST_LINES_PER_PAGE = 28

try:
    if LOCAL_ENV:
        from .settings_local import *

    if RUNTIME_ENV in ('PROD', 'PRODUCTION', 'PROD-DEBUG'):
        from .settings_production import *

    if RUNTIME_ENV == 'STAGING':
        from .settings_staging import *

    if RUNTIME_ENV == 'DEV':
        from .settings_dev import *

except ImportError:
    pass

