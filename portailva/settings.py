"""
Django settings for portailva project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '%8r$1anftcza)6)uth+ij(2o)si0)l^8o4=t!7^c_0_sz%1gkz')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not os.environ.get('APP_DEBUG', False)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', os.environ.get('SITE_DNS')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'anymail',
    'bootstrapform',
    'crispy_forms',
    'rest_framework',
    'social.apps.django_app.default',
    'ckeditor',
    'ckeditor_uploader',

    'portailva.utils',
    'portailva.association',
    'portailva.directory',
    'portailva.event',
    'portailva.file',
    'portailva.pages',
    'portailva.member',
    'portailva.newsletter'
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

AUTHENTICATION_BACKENDS = [
    'portailva.member.backends.UserModelEmailBackend'
]
AUTH_USER_MODEL = 'auth.User'

LOGIN_URL = 'member-login'
LOGIN_REDIRECT_URL = 'homepage'
LOGOUT_REDIRECT_URL = 'homepage'

ROOT_URLCONF = 'portailva.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portailva.association.context_processors.my_associations',
                'portailva.utils.context_processors.app_settings',
                'portailva.utils.context_processors.git_version',
            ],
        },
    },
]

WSGI_APPLICATION = 'portailva.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite')))
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'dist'),
    os.path.join(BASE_DIR, 'assets'),
)

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Datetime picker
PICKER_OPTIONS = {
    "format": "DD/MM/YYYY HH:mm",
    "sideBySide": True,
    "allowInputToggle": True,
    "locale": "fr",
    "widgetPositioning": {
        "vertical": "top"
    },
}

PICKER_DATE_OPTIONS = PICKER_OPTIONS.copy()
PICKER_DATE_OPTIONS['format'] = 'DD/MM/YYYY'
PICKER_TIME_OPTIONS = PICKER_OPTIONS.copy()
PICKER_TIME_OPTIONS['format'] = 'HH:mm'
PICKER_DATETIME_OPTIONS = PICKER_OPTIONS.copy()
PICKER_DATETIME_OPTIONS['format'] = 'DD/MM/YYYY HH:mm'

# Files upload
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler'
]
MAGIC_BIN = os.environ.get("MAGIC_BIN")

# Mail
ANYMAIL = {
    'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY')
}
EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@asso-insa-lyon.fr')

# REST API
REST_FRAMEWORK = {
    # By default, we only want authenticated requests
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


PORTAILVA_APP = {
    'site': {
        'name': "PortailVA",
        'litteral_name': "Portail VA",
        'url': os.environ.get('SITE_URL', "http://127.0.0.1:8000"),
        'api_url': os.environ.get('API_URL', "http://127.0.0.1:8000/api"),
        'email_contact': "contact@asso-insa-lyon.fr",
        'email_noreply': "noreply@asso-insa-lyon.fr",
        'contribute_link': "https://github.com/VAINSALyon/portailva/blob/dev/CONTRIBUTING.md",
        'repository': {
            'url': "https://github.com/VAINSALyon/portailva",
            'bugtracker': "https://github.com/VAINSALyon/portailva/issues",
            'api': "https://api.github.com/repos/VAINSALyon/portailva"
        },
        'licences': {
            'source': {
                'code': "GPL v3",
                'url_license': "http://www.gnu.org/licenses/gpl-3.0.html",
                'provider_name': "Zeste de Savoir",
                'provider_url': "http://zestedesavoir.com"
            }
        },
        'hosting': {
            'name': "OVH",
            'address': "2 rue Kellermann - 59100 Roubaix - France"
        },
        'cnil': "-"
    },
    'file': {
        'file_max_size': 20 * 1024 * 1024  # 20Mo
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'ck_editor')
