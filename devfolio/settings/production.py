# devfolio/settings/production.py

from dotenv import load_dotenv
from pathlib import Path
import dj_database_url

# Load .env.production into os.environ
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env.production')

from .base import *

# Production-specific overrides
load_dotenv()
DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# database configuration
#DB_NAME = os.environ.get("DB_NAME")
#DB_USER = os.environ.get("DB_USER")
#DB_PASSWORD = os.environ.get("DB_PASSWORD")
#DB_HOST = os.environ.get("DB_HOST", "db")
#DB_PORT = os.environ.get("DB_PORT")

#MYSQL database configuration For Docker
#MYSQL_HOST = os.environ.get("MYSQL_HOST")
#MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
#MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
#MYSQL_ALLOW_EMPTY_PASSWORD = os.environ.get("MYSQL_ALLOW_EMPTY_PASSWORD")

# Email settings
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER =os.environ.get ('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY',"")
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY',"")


# ✅ Database (Render PostgreSQL)
DATABASES = {
    "default": dj_database_url.config(
        default='DATABASE_URL',
        conn_max_age=600,
        ssl_require=True,
    )
}




# Database (Render will give you this)
DATABASE_URL = os.environ.get('DATABASE_URL')

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'




#DATABASES = {
        #'default': {
            #'ENGINE': 'django.db.backends.mysql',
            #'NAME': DB_NAME,
            #'USER': DB_USER,
            #'PASSWORD': DB_PASSWORD,
            #'HOST': DB_HOST,
            #'PORT': DB_PORT,

            #MYSQL
            #'MYSQL_HOST': MYSQL_HOST,
            #"MYSQL_ROOT_PASSWORD": MYSQL_ROOT_PASSWORD,
            #"MYSQL_DATABASE": MYSQL_DATABASE,
            #'MYSQL_ALLOW_EMPTY_PASSWORD': MYSQL_ALLOW_EMPTY_PASSWORD,

            #Email settings
            #'EMAIL_HOST': EMAIL_HOST,
            #'EMAIL_PORT': EMAIL_PORT,
            #'EMAIL_HOST_USER': EMAIL_HOST_USER,
            #'EMAIL_HOST_PASSWORD': EMAIL_HOST_PASSWORD,
            #'DEFAULT_FROM_EMAIL': DEFAULT_FROM_EMAIL,
            #'EMAIL_USE_TLS': EMAIL_USE_TLS,
            #'EMAIL_BACKEND': EMAIL_BACKEND,
            #'RECAPTCHA_PUBLIC_KEY': RECAPTCHA_PUBLIC_KEY,
            #'RECAPTCHA_PRIVATE_KEY': RECAPTCHA_PRIVATE_KEY,




#            'OPTIONS': {
#                'charset': 'utf8mb4',
#
#
#            },
#            'TEST': {
#                'NAME': 'test_db'
#            }
#        }
#    }







