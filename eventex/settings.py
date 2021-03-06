# coding: utf-8
"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Project Imports.

from unipath import Path
from decouple import config
from dj_database_url import parse as db_url

# General Configuration.

BASE_DIR = Path(__file__).parent
SECRET_KEY = config(
    'SECRET_KEY',
    default='8y)@(krme@28r2e3j5=irunc8(+8)fxqbevlg%1xmkov%6$6=='
)
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

# Apps enabled.

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'eventex.core',
    'eventex.subscriptions',
    'eventex.myauth',
)

# Middleware enabled.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Authentication User Model

AUTH_USER_MODEL = 'myauth.User'

# Location of the root URL map.

ROOT_URLCONF = 'eventex.urls'

# WSGI object.

WSGI_APPLICATION = 'eventex.wsgi.application'

# Database using dj-database-url for Heroku and Unipath.

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url
    )
}

# Internationalization.

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Files to be served by Django with dj-static.

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

# Disable South Migration for database used in tests.

SOUTH_TEST_MIGRATE = False
