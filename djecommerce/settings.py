
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))))

ALLOWED_HOSTS = ['127.0.0.1', '.elasticbeanstalk.com']
DEBUG = True

SECRET_KEY = "kobl@t=yw9d*0y%jt2gjnq78=u!z_rrxb&w8e47l!(jz@m79zy"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'rest_framework',
    'core',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
    ]

ROOT_URLCONF = 'djecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

WSGI_APPLICATION = 'djecommerce.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'spices-store',
        'USER': 'postgres',
        'PASSWORD': 'shikha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# if DEBUG:
#     STRIPE_PUBLIC_KEY = os.environ['STRIPE_TEST_PUBLIC_KEY']
#     STRIPE_SECRET_KEY = os.environ['STRIPE_TEST_SECRET_KEY']
# else:
#     STRIPE_PUBLIC_KEY = os.environ['STRIPE_LIVE_PUBLIC_KEY']
#     STRIPE_SECRET_KEY = os.environ['STRIPE_LIVE_SECRET_KEY']


if DEBUG:
    STRIPE_PUBLIC_KEY = 'pk_test_51Ihou6SA5kVB8WAKYFRfhpTtKNgqeuQhB6PaMr6eIRvgmoyMTs5dIxGIoCZcXQaRSepKa5q7KtKDeWsGK4k0oze900HEWNTzIY'
    STRIPE_SECRET_KEY = 'sk_test_51Ihou6SA5kVB8WAKBgATPte4ApVHw8DUS8dWq6CtiUBAN1lWWAVe0RMo1iEtpA9oERIxEzFqd0YT3JEFDQei2bpY00FsR2VoQO'
else:
    STRIPE_PUBLIC_KEY = ''
    STRIPE_SECRET_KEY = ''
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
