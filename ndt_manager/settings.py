import os
import dj_database_url
import rollbar
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY',)
DEBUG = bool(os.environ.get('DEBUG', False))

ALLOWED_HOSTS = ['*', 'http://ndtmanager.dzmitrysha.repl.co/', 'localhost',
                 'https://ndtmanager-production.up.railway.app/']
# CSRF_TRUSTED_ORIGINS = []
# X_FRAME_OPTIONS = '*'

CSRF_TRUSTED_ORIGINS = [
    'https://ndtmanager-production.up.railway.app'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'django_select2',
    'ndt_manager.apps.NDTManagerConfig',
    'equipment.apps.EquipmentConfig',
    'equiptypes.apps.EquiptypesConfig',
    'reports.apps.ReportsConfig',
    'stations.apps.StationsConfig',
    'users.apps.UsersConfig',
    'certificates.apps.CertificatesConfig',
    'django_filters',
    'django_cleanup',
]

# Rollbar access
ROLLBAR = {
    'access_token': os.environ.get('ROLLBAR_ACCESS_TOKEN',),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}
rollbar.init(**ROLLBAR)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'ndt_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ndt_manager.wsgi.application'

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600)
}

AUTH_USER_MODEL = 'users.User'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa 501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa 501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa 501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa 501
    },
]

# Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LOCALE_URL = "locale/"
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# fixtures directory
FIXTURE_DIRS = ['fixtures']

# default login redirect url
# LOGIN_REDIRECT_URL = "/"

# print SQL queries in shell_plus
if DEBUG:
    INSTALLED_APPS.insert(0, 'django_extensions')
    SHELL_PLUS_PRINT_SQL = True
