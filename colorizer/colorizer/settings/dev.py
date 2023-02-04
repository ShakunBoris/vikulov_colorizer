from .base import *

SECRET_KEY = 'django-insecure-^i&*nk$7$5&6-wt713-dyexy_lq(9m_z2+g3@7g2kabmv3u&uk'
# print(SECRET_KEY[:round(len(SECRET_KEY)/3)])
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'colorizer.up.railway.app', 'colorizer.dev.up.railway.app']
# ALLOWED_HOSTS = ['*']


#local POSTGRES
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'psql_test',
#        'USER': 'postgres',
#        'PASSWORD': 'postgres',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
# }

#RAILWAY TEST MANUAL CONNECT POSTGRES
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'railway',
       'USER': 'postgres',
       'PASSWORD': 'o8FbMYYcKAPgKYKEJIzc',
       'HOST': 'containers-us-west-146.railway.app',
       'PORT': '7010',
   }
}

# LOCAL SQLITE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
