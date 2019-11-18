"""
Project main settings file. These settings are common to the project
if you need to override something do it in local.pt
"""

from sys import path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import yaml


# PATHS
# Path containing the django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path.append(BASE_DIR)


# CONFIGURATION
# Load configuration from disk
CONFIG = yaml.safe_load(os.environ.get("CONFIGPATH", open("config.yml")))

# Path of the top level directory.
# This directory contains the django project, apps, libs, etc...
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# IMPORTANT!:
# You must keep this secret. Control this in your config.yml file.
# https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#secret-key
SECRET_KEY = CONFIG["secret_key"]

# SITE SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/2.2/ref/settings/#installed-apps
INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
    "django.contrib.syndication",
    "django.contrib.staticfiles",
    # Third party apps
    "compressor",
    "haystack",
    "whoosh",
    # Local apps
    "grasa_event_locator",
]

# https://docs.djangoproject.com/en/2.2/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]


# DATABASE SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": CONFIG["database"]["db"],
        "USER": CONFIG["database"]["username"],
        "PASSWORD": CONFIG["database"]["password"],
        "HOST": CONFIG["database"]["host"],
        "PORT": CONFIG["database"]["port"],
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# DEBUG SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/2.2/ref/settings/#internal-ips
INTERNAL_IPS = ["127.0.0.1", "localhost"]


# LOCALE SETTINGS
# Local time zone for this installation.
# https://docs.djangoproject.com/en/2.2/ref/settings/#time-zone
TIME_ZONE = "America/New_York"

# https://docs.djangoproject.com/en/2.2/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

# https://docs.djangoproject.com/en/2.2/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/2.2/ref/settings/#use-l10n
USE_L10N = False

# https://docs.djangoproject.com/en/2.2/ref/settings/#use-tz
USE_TZ = True


# MEDIA AND STATIC SETTINGS
# Absolute filesystem path to the directory that will hold user-uploaded files.
# https://docs.djangoproject.com/en/2.2/ref/settings/#media-root
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "public/media")

# URL that handles the media served from MEDIA_ROOT. Use a trailing slash.
# https://docs.djangoproject.com/en/2.2/ref/settings/#media-url
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-root
STATIC_ROOT = os.path.join(PROJECT_ROOT, "public/static")

# URL prefix for static files.
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-url
STATIC_URL = "/static/"

# Additional locations of static files
# https://docs.djangoproject.com/en/2.2/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# TEMPLATE SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


# URL SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#root-urlconf.
ROOT_URLCONF = "grasa_event_locator.urls"


# MIDDLEWARE SETTINGS
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# LOGGING
# https://docs.djangoproject.com/en/2.2/topics/logging/
LOGGING = {"version": 1, "loggers": {"grasa_event_locator": {"level": "DEBUG"}}}


# WSGI SETTINGS
# https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application
WSGI_APPLICATION = "grasa_event_locator.wsgi.application"


# SMTP EMAIL SETTINGS
# Used for outgoing email. Managed by config.yml.
EMAIL_HOST = CONFIG["outgoing_smtp"]["host"]
EMAIL_USE_SSL = True
EMAIL_PORT = CONFIG["outgoing_smtp"]["port"]
EMAIL_HOST_USER = CONFIG["outgoing_smtp"]["username"]
EMAIL_HOST_PASSWORD = CONFIG["outgoing_smtp"]["password"]


# MISC. SETTINGS
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(os.path.dirname(__file__), "whoosh_index"),
    }
}

LOGIN_REDIRECT_URL = "/grasa_event_locator/templates/search/search.html"
