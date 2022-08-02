from mysite.base import *

DEBUG = False

ADMINS = (
    ('Mohammad', 'mosalman1379@gmail.com')
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config['database']['NAME'],
        'USER': config['database']['USER'],
        'PASSWORD': config['database']['PASS']
    }
}

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = '518400'

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
