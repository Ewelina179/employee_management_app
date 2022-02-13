from .base import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'employees',

        'USER': 'postgres',

        'PASSWORD': 'postgres',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

DEBUG = True