from .base import *  # noqa

DEBUG = False

# NOTIFICATIONS
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/2.2/ref/settings/#admins
ADMINS = (("Service status notices", CONFIG["sysadmin_email"]),)
MANAGERS = ADMINS

# DJANGO-COMPRESSOR SETTINGS
# STATICFILES_FINDERS = STATICFILES_FINDERS + (
#    'compressor.finders.CompressorFinder',
# )
