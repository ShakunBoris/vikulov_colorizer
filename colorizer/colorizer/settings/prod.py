from .base import *
import os

SECRET_KEY = os.environ['SECRET_KEY']
# print(os.environ['SECRET_KEY'])
# print('!!!!!!!!!!!!!!!!!!!!!!!!! PROD.Py!!!!!!!!!!!!!!!!!!!!!!')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['nginx-dev.up.railway.app', 'colorizer.up.railway.app',]
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
    #    'NAME': os.environ['DB_NAME'],
    #    'USER': os.environ['DB_USER'],
    #    'PASSWORD': os.environ['DB_PASSWORD'],
    #    'HOST': os.environ['DB_HOST'],
    #    'PORT': os.environ['DB_PORT'],
        'NAME': os.environ.get('PGDATABASE', 'psql_test'),
       'USER': os.environ.get('PGUSER', 'postgres'),
       'PASSWORD': os.environ.get('PGPASSWORD', 'postgres'),
       'HOST': os.environ.get('PGHOST', '127.0.0.1'),
       'PORT': os.environ.get('PGPORT', '5432'),
   }
}
# ??
# LAST BEFORE NGINX

