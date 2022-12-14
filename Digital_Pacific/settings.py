from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'aplicaciones/templates/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=8)at39j01pg^5e57)(e49qk8&p_0qguycsa0f9-=h+g+-$wm&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MESSAGE_STORAGE= "django.contrib.messages.storage.cookie.CookieStorage"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',    
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicaciones.apps.AplicacionesConfig',
    'import_export',
    
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

IMPORT_EXPORT_USE_TRANSACTIONS = True 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Digital_Pacific.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'Digital_Pacific.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


#LEER *** LEER *** LEER *** LEER *** LEER
#si te conectas desde PA, deja comentado el DATABASES de digital pacific y descomenta el DATABASES  de Nato$default

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bd_pacific',                      # Or path to database file if using sqlite3.                                                   # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {

#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'Nato$default',                      # Or path to database file if using sqlite3.                                                   # The following settings are not used with sqlite3:
#         'USER': 'Nato',
#         'PASSWORD': 'administrador',
#         'HOST': 'Nato.mysql.pythonanywhere-services.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.

#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = 'static/'

 
#Configuracion para agregar campos al usuario
AUTH_USER_MODEL = 'aplicaciones.Usuario'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#descomentar static_root y comentar STATICFILES_DIRS para lanzar un collecttatic

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
