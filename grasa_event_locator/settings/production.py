import os
from .base import *  # noqa

DEBUG = False

# DATABASE SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grasa_event_locator',
        'USER': 'grasaadmin',
        'PASSWORD': 'djangoGrasa2019',
        'HOST': 'db',
        'PORT': '3306',
	'OPTIONS': {'charset': 'utf8mb4'},
    },
}

# IMPORTANT!:
# You must keep this secret, you can store it in an
# environment variable and set it with:
# export SECRET_KEY="phil-dunphy98!-bananas12"
# https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#secret-key
SECRET_KEY = os.environ['SECRET_KEY']

# WSGI SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application
WSGI_APPLICATION = 'grasa_event_locator.wsgi.application'

# NOTIFICATIONS
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/2.2/ref/settings/#admins
ADMINS = (
         ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# DJANGO-COMPRESSOR SETTINGS
STATICFILES_FINDERS = STATICFILES_FINDERS + (
    'compressor.finders.CompressorFinder',
)

try:
    from local_settings import * # noqa
except ImportError:
    pass
