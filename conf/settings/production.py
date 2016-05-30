# -*- coding: utf-8 -*-

import os

DEBUG = 'DEBUG' in os.environ
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".{{ product_name }}.com", "{{ project_name }}.herokuapp.com"]

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Uncomment if you'd like to use S3 for static file storage.
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'statictastic.backends.VersionedS3BotoStorage'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedFileSystemStorage'

BASE_URL = "https://{{ project_name }}.herokuapp.com"
