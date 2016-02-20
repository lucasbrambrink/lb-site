__author__ = 'lb'
import os
from os.path import (dirname, basename, join, normpath)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(PROJECT_DIR)
# Site name:
SITE_NAME = basename(PROJECT_DIR)
#### END PATH CONFIGURATION

ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

###---< Database >---###
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}
TEMPLATE_DEBUG = False
DEBUG = False
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECRET_KEY = os.environ['SECRET_KEY']
