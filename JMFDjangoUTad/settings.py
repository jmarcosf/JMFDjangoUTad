# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* settings.py                                                            *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Django Project Settings File                              *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#* References:  https://docs.djangoproject.com/en/1.6/topics/settings/    *#
#*              https://docs.djangoproject.com/en/1.6/ref/settings/       *#
#*                                                                        *#
#**************************************************************************#

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Build paths                                                            *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Quick-start development settings (unsuitable for production)           *#
#* See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/  *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_r^jsbqe+%v#chb5(rxzj$q@y6_a#-)u8hwcgj36lds7g$(%pj'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Application settings                                                   *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
INSTALLED_APPS =\
(
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'Pictures',
)

MIDDLEWARE_CLASSES =\
(
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'JMFDjangoUTad.urls'
WSGI_APPLICATION = 'JMFDjangoUTad.wsgi.application'

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Database settings                                                      *#
#* See https://docs.djangoproject.com/en/1.6/ref/settings/#databases      *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
DATABASES =\
{
    'default':
    {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'JMFDjangoUTad.db',
    }
}

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Internationalization settings                                          *#
#* See https://docs.djangoproject.com/en/1.6/topics/i18n/                 *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Static files (CSS, JavaScript, Images) settings                        *#
#* See https://docs.djangoproject.com/en/1.6/howto/static-files/          *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
STATIC_URL = '/static/'

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Templates settings                                                     *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
TEMPLATE_DIRS =\
(
    os.path.join( BASE_DIR,  'templates' ),
)

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* REST Framework Paging settings                                         *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
REST_FRAMEWORK = \
{
    'PAGINATE_BY' : 5
}
