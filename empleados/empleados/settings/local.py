from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR.child('db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbempleado',
        'USER': 'rjjimenezr',
        'PASSWORD': 'Ul1s3s18!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS =[BASE_DIR.child('static')]
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.child('media')

# probar:
# MEDIA_ROOT = BASE_DIR.parent/'media/' MEDIA_URL = '/media/'