from .base import *

SECRET_KEY = 'django-insecure-^i&*nk$7$5&6-wt713-dyexy_lq(9m_z2+g3@7g2kabmv3u&uk'
print(SECRET_KEY[:round(len(SECRET_KEY)/3)])
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']