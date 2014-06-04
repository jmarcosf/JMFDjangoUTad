# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* wsgi.py                                                                *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Project WSGI Settings File                                *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
#Reference:https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault( "DJANGO_SETTINGS_MODULE", "JMFDjangoUTad.settings" )
application = get_wsgi_application()
