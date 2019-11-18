import os
from .base import *  # noqa

DEBUG = False

# IMPORTANT!:
# You must keep this secret, you can store it in an
# environment variable and set it with:
# export SECRET_KEY="phil-dunphy98!-bananas12"
# https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#secret-key
SECRET_KEY = os.environ["SECRET_KEY"]

# NOTIFICATIONS
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/2.2/ref/settings/#admins
ADMINS = (("Your Name", "your_email@example.com"),)
MANAGERS = ADMINS

# DJANGO-COMPRESSOR SETTINGS
# STATICFILES_FINDERS = STATICFILES_FINDERS + (
#    'compressor.finders.CompressorFinder',
# )
