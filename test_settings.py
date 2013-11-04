import os
PROJECT_DIR = os.path.dirname(__file__)

STATIC_URL = PROJECT_DIR + '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb',
    }
}

INSTALLED_APPS = (
    'floppy_gumby_forms',
    'floppyforms',
    'django.contrib.staticfiles',
    'south',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

SITE_ID = 1

ROOT_URLCONF = "test_urls"
