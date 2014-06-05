# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* urls.py                                                                *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures REST Api End Point URLs File                     *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from Pictures.api import *

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* Pictures App URL Patterns                                              *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
urlpatterns = patterns\
(
    'Pictures.api.views',
    url( r'^api/pictures/$', PictureList.as_view() ),
    url( r'^api/pictures/(?P<pk>[0-9]+)/$', PictureDetail.as_view() ),

    url( r'^api/users/$', UserList.as_view() ),
    url( r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view() ),

    url( r'^api/login/', include('rest_framework.urls', namespace = 'rest_framework' ) ),
)

urlpatterns = format_suffix_patterns( urlpatterns )






