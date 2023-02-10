from .base import *

SECRET_KEY = 'django-insecure-^i&*nk$7$5&6-wt713-dyexy_lq(9m_z2+g3@7g2kabmv3u&uk'
# print(SECRET_KEY[:round(len(SECRET_KEY)/3)])
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nginx-dev.up.railway.app', 'localhost', '127.0.0.1', 'colorizer.up.railway.app', 'colorizer.dev.up.railway.app']
# ALLOWED_HOSTS = ['*']

# RAILWAY TEST MANUAL CONNECT POSTGRES 
# NOW: If run locally it takes defaults and waits for local portgres server
# if vars exist (online they do) run online server

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       # TO CONNECT TO ONLINE DB
    #    'NAME': 'railway',
    #    'USER': 'postgres',
    #    'PASSWORD': 'o8FbMYYcKAPgKYKEJIzc',
    #    'HOST': 'containers-us-west-146.railway.app',
    #    'PORT': '7010',
        # FOR ONLINE OFFLINE Automatic choice
        'NAME': os.environ.get('PGDATABASE', 'psql_test'),
       'USER': os.environ.get('PGUSER', 'postgres'),
       'PASSWORD': os.environ.get('PGPASSWORD', 'postgres'),
       'HOST': os.environ.get('PGHOST', '127.0.0.1'),
       'PORT': os.environ.get('PGPORT', '5432'),
   }
}

# LOCAL SQLITE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
