"""
Django settings for delivery project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%)-4f#okzjg_q3_*sy*y%#4xon6vl6_m4&67_yqkt81fvju&!e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'bootstrap4',
    'social_django',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ProfileMiddleware',
]

ROOT_URLCONF = 'delivery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'delivery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


LOGIN_URL='/sign-in'
LOGIN_REDIRECT_URL ="/"


MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_FACEBOOK_KEY = "1478914612550357"
SOCIAL_AUTH_FACEBOOK_SECRET = "dc36e85c2c6d7ab03c9b4ca81dc93b13"
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]


SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pavelrudeniaaa@gmail.com'
EMAIL_HOST_PASSWORD='********'
DEFAULT_FROM_EMAIL = 'DeliveryApp <no-reply@delivery.localhost>'


FIREBASE_ADMIN_CREDENTIAL = os.path.join(BASE_DIR,"deliveryapp-b24e4-firebase-adminsdk-m1fma-6d2dc68d91.json")

STRIPE_API_PUBLIC_KEY='pk_test_51LNFJnC1arWGs47VmaCKuNJur9L9O66FniQvebE7usNCGA76eyR6lq7pkxhxVSG9y7GIsAkYUkA5cp1OrzqoEJOI009UJdRwQU'
STRIPE_API_SECRET_KEY='sk_test_51LNFJnC1arWGs47Vie1DN702iUZQUu2uEtnLDWwetp5O5iDl4XT0TFUQmbt7aA8by2ggnMhecOyWFUhOoXbdaTWR008vqcJxhz'


GOOGLE_MAP_API_KEY="AIzaSyAIlvbtx00myOYRBPdHrsvhBm2VJaM7phs"

PAYPAL_MODE = "sandbox"
PAYPAL_CLIENT_ID = "AW7-FkakUjrIvQPU2Ix9Nt2CMXQnsZRqGBKJbpp0Gw5vVeUpI4c4KiwYlOjHEzLUYTiqYcen4m4hLF7P"
PAYPAL_CLIENT_SECRET = "ENhuFY7f2zA0ncU-J76siYqrDCecOZj0M95kd7vGSF91MOqSSELSElUunrOTF_gJPoeaN0oG0rWTw3Cm"

NOTIFICATION_URL = "https://guarded-wildwood-06810.herokuapp.com/"
#
ASGI_APPLICATION = "delivery.asgi.application"


# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1',6379)],
        },
    },
}

# Activate Django Heroku
import django_on_heroku
django_on_heroku.settings(locals())
