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
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from Pictures.api import *

urlpatterns = patterns\
(
    'Pictures.api.views',
    url( r'^api/pictures/$', PictureList.as_view() ),
    url( r'^api/pictures/(?P<pk>[0-9]+)/$', PictureDetail.as_view() ),

    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns( urlpatterns )






