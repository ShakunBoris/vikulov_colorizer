from .base import *

SECRET_KEY = 'django-insecure-^i&*nk$7$5&6-wt713-dyexy_lq(9m_z2+g3@7g2kabmv3u&uk'
# print(SECRET_KEY[:round(len(SECRET_KEY)/3)])
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'colorizer.up.railway.app']
# ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'postgresDB',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
