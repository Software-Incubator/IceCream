from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}

STATIC_ROOT = os.path.join('/home/si', 'Assets/IceCream/static')

MEDIA_ROOT = os.path.join('/home/si', "Assets/IceCream/media")
