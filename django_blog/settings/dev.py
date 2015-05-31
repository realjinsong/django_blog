from base import *

DEBUG = True

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'song',
        'PASSWORD': 'etaoin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS += ["debug_toolbar", ]

ALLOWED_HOSTS = ['localhost', ]

MIDDLEWARE_CLASSES += (
    'middleware.profile.ProfilerMiddleware',
)
