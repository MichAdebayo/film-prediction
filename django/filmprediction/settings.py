"""
Django settings for filmprediction project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from dotenv import load_dotenv

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Charger les variables du fichier .env
load_dotenv(BASE_DIR / '.env')

ACCOUNT_URL = os.getenv("ACCOUNT_URL", "fake_account_url")
CONTAINER_NAME = os.getenv("CONTAINER_NAME", "fake_container_name")
BLOB_NAME =  os.getenv("BLOB_NAME", "fake_blob_name")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "fake_secret_key")

FASTAPI_URL = os.getenv("FASTAPI_URL", "fake_fast_api_url")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
TAILWIND_APP_NAME = "theme"

# Configuration de la base de données MSSQL
MSSQL_ENGINE = 'mssql'
MSSQL_NAME = os.getenv('databasedj_')  # Nom de la base de données
MSSQL_USER = os.getenv('usernamedj_')  # Nom d'utilisateur
MSSQL_PASSWORD = os.getenv('passworddj_')  # Mot de passe
MSSQL_HOST = os.getenv('serverdj_')  # Nom du serveur Azure SQL
MSSQL_PORT = os.getenv('portdj_')  # Port (1433 par défaut pour Azure SQL)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
     # Apps installées
    "tailwind",
    "films",
    "theme",
    'django_browser_reload',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "filmprediction.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "filmprediction.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

"""DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}"""

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': MSSQL_ENGINE,
        'NAME': MSSQL_NAME,
        'USER': MSSQL_USER,
        'PASSWORD': MSSQL_PASSWORD,
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',  # Utiliser le driver ODBC 18 pour SQL Server
            'Encrypt': 'yes',  # Activer le chiffrement
            'TrustServerCertificate': 'no',  # Ne pas faire confiance au certificat du serveur
            'Connection Timeout': 30,  # Timeout de connexion
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

#STATIC_URL = "static/"
#STATIC_URL = '/static/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / "theme" / "static_src",
    BASE_DIR / "theme" / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


import platform

if platform.system() == "Windows":
    NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
else:
    NPM_BIN_PATH = "/usr/bin/npm"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

#FASTAPI_URL = "http://localhost:8000"

LOGIN_URL = 'films:login'  # Redirige vers la page de login si non connecté
LOGIN_REDIRECT_URL = 'dashboard'  # Redirige après une connexion réussie
LOGOUT_REDIRECT_URL = 'films:login'  # Redirige après déconnexion

DATEPICKER_FORMAT_STRING="%Y-%m-%d"
FASTAPI_URL = os.getenv("FASTAPI_URL", "fake_fast_api_url")