import os
import dj_database_url
from .settings import *

if os.path.exists('env.py'):
    import env

DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

# ALLOWED HOSTS
ALLOWED_HOSTS=[
    os.environ.get("PRODUCTION_HOST")
]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("HEROKU_DB"))
}