# -*- coding: utf-8 -*-
import os

from _conf.core import *


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'TIMEOUT': 900,
    }
}


ALLOWED_HOSTS = [
    '127.0.0.1',
    '.localhost',
    '195.201.129.56',
]
