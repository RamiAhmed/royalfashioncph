"""
Django settings for royalfashioncph project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# General import statements
import os

# Make this unique, and don't share it with anybody.
from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

HTTPS = False

ADMINS = (
    ('RamiAhmed', 'rami@alphastagestudios.com'),
)

MANAGERS = ADMINS

# Django Sites ID
SITE_ID = 1

# Allowed hosts - # Update for new domain
ALLOWED_HOSTS = ['*',]#os.environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(':')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#import dj_database_url
#DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
from postgresify import postgresify
DATABASES = postgresify()

# Cache
from memcacheify import memcacheify
CACHES = memcacheify()

# Application definition

GRAPPELLI = (
    'grappelli',            
)             

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
    'storages',
    'sorl.thumbnail',
    'haystack',
    'wysihtml5',
    'collectfast',
)

LOCAL_APPS = (
    'royalfashioncph',
    'shop',
    'contact',
    'news',
)

INSTALLED_APPS = GRAPPELLI + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',                    
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',   
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
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Amazon S3 with Compressor
# http://jeanphix.me/2012/02/08/django-heroku-compressor-storages/

# Amazon AWS S3 credientials
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

# S3 boto backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'royalfashioncph.storage.CachedS3BotoStorage'
STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

# Path settings
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
MEDIA_UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

MEDIA_URL = STATIC_URL + 'media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# AWS S3 settings
AWS_AUTO_CREATE_BUCKET = True
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = True
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False
AWS_PRELOAD_METADATA = True

# Compressor
COMPRESS_ENABLED = DEBUG is False
if COMPRESS_ENABLED:
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    ]
    COMPRESS_STORAGE = 'royalfashioncph.storage.CachedS3BotoStorage'
    COMPRESS_URL = STATIC_URL
    COMPRESS_OFFLINE = False


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'shop.context_processors.shop_collections',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
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


# Elastic Search Engine with Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('SEARCHBOX_URL'),
        'INDEX_NAME': 'haystack',
        },
    }

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Grappelli Admin Site Settings
GRAPPELLI_ADMIN_TITLE = "Admin | Royal Fashion Copenhagen"


# Mandrill email settings
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MANDRILL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MANDRILL_APIKEY')
EMAIL_USE_TLS = True

SERVER_EMAIL = "Royal Fashion Copenhagen <notifications@royalfashioncph.dk>"
DEFAULT_FROM_EMAIL = SERVER_EMAIL


# Wysihtml5 rich text editor options
EDITOR_CONF = {
    # Give the editor a name, the name will also be set as class
    # name on the iframe and on the iframe's body
    'name': 'wysihtml5 editor',
    # Whether the editor should look like the textarea (by adopting styles)
    'style': 'true',
    # Id of the toolbar element, pass falsey value if you don't want
    # any toolbar logic
    'toolbar': 'null',
    # Whether urls, entered by the user should automatically become
    # clickable-links
    'autoLink': 'true',
    # Object which includes parser rules (set this to
    # examples/rules/spec.json or your own spec, otherwise only span
    # tags are allowed!)
    'parserRules': 'wysihtml5ParserRules',
    # Parser method to use when the user inserts content via copy & paste
    'parser': 'wysihtml5.dom.parse || Prototype.K',
    # Class name which should be set on the contentEditable element in
    # the created sandbox iframe, can be styled via the 'stylesheets' option
    'composerClassName': '"wysihtml5-editor"',
    # Class name to add to the body when the wysihtml5 editor is supported
    'bodyClassName': '"wysihtml5-supported"',
    # By default wysihtml5 will insert <br> for line breaks, set this to
    # false to use <p>
    'useLineBreaks': 'false',
    # Array (or single string) of stylesheet urls to be loaded in the
    # editor's iframe
    'stylesheets': '["%s"]' % (STATIC_URL +
                               "wysihtml5/css/stylesheet.css"),
    # Placeholder text to use, defaults to the placeholder attribute
    # on the textarea element
    'placeholderText': 'null',
    # Whether the composer should allow the user to manually resize
    # images, tables etc.
    'allowObjectResizing': 'true',
    # Whether the rich text editor should be rendered on touch devices
    # (wysihtml5 >= 0.3.0 comes with basic support for iOS 5)
    'supportTouchDevices': 'true'
}

WYSIHTML5_TOOLBAR = {
    "formatBlockHeader": {
        "active": False,
        "command_name": "formatBlock",
        "render_icon": "wysihtml5.widgets.render_formatBlockHeader_icon"
    },
    "formatBlockParagraph": {
        "active": True,
        "command_name": "formatBlock",
        "render_icon": "wysihtml5.widgets.render_formatBlockParagraph_icon"
    },
    "bold": {
        "active": True,
        "command_name": "bold",
        "render_icon": "wysihtml5.widgets.render_bold_icon"
   },
    "italic": {
        "active": True,
        "command_name": "italic",
        "render_icon": "wysihtml5.widgets.render_italic_icon"
    },
    "underline": {
        "active": True,
        "command_name": "underline",
        "render_icon": "wysihtml5.widgets.render_underline_icon"
    },
    "justifyLeft": {
        "active": False,
        "command_name": "justifyLeft",
        "render_icon": "wysihtml5.widgets.render_justifyLeft_icon"
    },
    "justifyCenter": {
        "active": False,
        "command_name": "justifyCenter",
        "render_icon": "wysihtml5.widgets.render_justifyCenter_icon"
    },
    "justifyRight": {
        "active": False,
        "command_name": "justifyRight",
        "render_icon": "wysihtml5.widgets.render_justifyRight_icon"
    },
    "insertOrderedList": {
        "active": True,
        "command_name": "insertOrderedList",
        "render_icon": "wysihtml5.widgets.render_insertOrderedList_icon"
    },
    "insertUnorderedList": {
        "active": True,
        "command_name": "insertUnorderedList",
        "render_icon": "wysihtml5.widgets.render_insertUnorderedList_icon"
    },
    "insertImage": {
        "active": False,
        "command_name": "insertImage",
        "render_icon": "wysihtml5.widgets.render_insertImage_icon",
        "render_dialog": "wysihtml5.widgets.render_insertImage_dialog"
    },
    "createLink": {
        "active": True,
        "command_name": "createLink",
        "render_icon": "wysihtml5.widgets.render_createLink_icon",
        "render_dialog": "wysihtml5.widgets.render_createLink_dialog"
    },
    "insertHTML": {
        "active": True,
        "command_name": "insertHTML",
        "command_value": "<blockquote>quote</blockquote>",
        "render_icon": "wysihtml5.widgets.render_insertHTML_icon"
    },
    "foreColor": {
        "active": False,
        "command_name": "foreColor",
        "render_icon": "wysihtml5.widgets.render_foreColor_icon"
    },
    "changeView": {
        "active": True,
        "command_name": "change_view",
        "render_icon": "wysihtml5.widgets.render_changeView_icon"
    },
}

WYSIHTML5_ALLOWED_TAGS = ('h3 h4 h5 h6 div p br b i u ul ol li span a blockquote')


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


