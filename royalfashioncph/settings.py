"""
Django settings for royalfashioncph project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..').replace('\\', '/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# Make this unique, and don't share it with anybody.
from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

HTTPS = False

ADMINS = (
    ('RamiAhmed', 'rami@alphastagestudios.com'),
)

MANAGERS = ADMINS

# Django Sites ID
SITE_ID = 1

# Allowed hosts - # Update for new domain
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(':')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import dj_database_url
DATABASES = {'default': dj_database_url.config()}

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'gunicorn',
    'compressor',
    'analytical',
    'jquery',
    'bootstrap3',
    'robots',
)

LOCAL_APPS = (
    'royalfashioncph',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'htmlmin.middleware.HtmlMinifyMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'royalfashioncph.urls'

WSGI_APPLICATION = 'royalfashioncph.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'da-DK'

# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Copenhagen'

# If you set this to False, Django will make some optimizations so as not to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute filesystem path to the directory
# that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'mediafiles'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'staticfiles'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Compress should send to and look in static url
COMPRESS_URL = STATIC_URL

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)


# Robots caching
ROBOTS_CACHE_TIMEOUT = 60*60*24 # = 24 hours

# Activate Google Analytics
GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID')
GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = True
GOOGLE_ANALYTICS_SITE_SPEED = True
GOOGLE_ANALYTICS_ANONYMIZE_IP = True

GOOGLE_ANALYTICS_INTERNAL_IPS = ['87.61.152.173']


# Security # Enable for  HTTPS
SECURE_SSL_REDIRECT = HTTPS
SECURE_HSTS_SECONDS = 60 * 60  # 1 hour
SECURE_HSTS_INCLUDE_SUBDOMAINS = HTTPS
SECURE_FRAME_DENY = HTTPS
SECURE_CONTENT_TYPE_NOSNIFF = HTTPS
SECURE_BROWSER_XSS_FILTER = HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
