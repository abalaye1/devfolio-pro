# devfolio/settings/development.py

from dotenv import load_dotenv
from pathlib import Path

# Load .env.development into os.environ
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env.development')

from .base import *

# Development-specific overrides
DEBUG = True
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")


# Database configuration - Use SQLite for development (or MySQL if preferred)
# Option A: SQLite (simpler, no setup needed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}





# reCAPTCHA settings (optional for development)
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', '')

# Security settings - Disable for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"






# Option B: If you want to use MySQL locally (uncomment this and comment SQLite above)
#DB_NAME = os.environ.get("DB_NAME")
#DB_USER = os.environ.get("DB_USER")
#DB_PASSWORD = os.environ.get("DB_PASSWORD")
#DB_HOST = os.environ.get("DB_HOST", "localhost")  # Use 'localhost' for local MySQL
#DB_PORT = os.environ.get("DB_PORT", "3306")
#
#DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': DB_NAME,
#         'USER': DB_USER,
#         'PASSWORD': DB_PASSWORD,
#         'HOST': DB_HOST,
#         'PORT': DB_PORT,
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }

# Email settings - Use console backend for development (no real emails)
# This will print emails to the console instead of sending them
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Or if you want to send real emails in development, use:
#EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
#EMAIL_HOST = os.environ.get('EMAIL_HOST')
#EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
#EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
#EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
#DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')


# Additional development settings
#ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.*']  # Add your local IP if needed

# Enable debug toolbar or other development tools (optional)
#if DEBUG:
#     INSTALLED_APPS += ['debug_toolbar']
#     MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
#     INTERNAL_IPS = ['127.0.0.1']