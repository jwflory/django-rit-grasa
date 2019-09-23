from .base import *  # noqa

DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

SECRET_KEY = "secret"
ALLOWED_HOSTS = ["grasa.larrimore.de", "abba.larrimore.de"]
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

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache"
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# DJANGO DEBUG TOOLBAR SETTINGS
# https://django-debug-toolbar.readthedocs.org
def show_toolbar(request):
    return not request.is_ajax() and request.user and request.user.is_superuser

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware", ]
INSTALLED_APPS += ["debug_toolbar", ]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
    'SHOW_TOOLBAR_CALLBACK': 'grasa_event_locator.settings.development.show_toolbar',
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

try:
    from local_settings import * # noqa
except ImportError:
    pass
