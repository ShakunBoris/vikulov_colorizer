from .base import *
import os

SECRET_KEY = os.environ['SECRET_KEY']
# print(os.environ['SECRET_KEY'])
# print('!!!!!!!!!!!!!!!!!!!!!!!!! PROD.Py!!!!!!!!!!!!!!!!!!!!!!')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']
