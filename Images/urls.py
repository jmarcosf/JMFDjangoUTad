# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* urls.py                                                                *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Images REST Api End Point URLs File                       *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from Images.api import *

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* Images App URL Patterns                                                *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
urlpatterns = patterns\
(
    'Pictures.api.views',
    url( r'^api/images/$', ImageCreate.as_view() ),
#   url( r'^api/images/(?P<pk>[0-9]+)/$', ImageShow.as_view() ),
    url( r'^api/images/(?P<imageUrl>.+)/$', ImageShow.as_view() ),
)

urlpatterns = format_suffix_patterns( urlpatterns )















