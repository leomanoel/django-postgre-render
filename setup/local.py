from pathlib import Path
from .settings import *

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

ROOT_URLCONF = 'setup.urls'
WSGI_APPLICATION = 'setup.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'









