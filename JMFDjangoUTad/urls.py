# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* urls.py                                                                *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Project URL's File                                        *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from Pictures.api import PictureList

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Auto Admin Discover option                                             *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
admin.autodiscover()

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* URL Patterns                                                           *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
urlpatterns = patterns\
(   '',

    #Pictures Web End Points
    url( r'^$', login ),
    url( r'^login/$', login ),
    url( r'^logout/$', 'Pictures.views.Logout' ),
    url( r'^pictures/(?P<urlUserName>.+)', 'Pictures.views.UserPublicPictures' ),
    url( r'^pictures/', 'Pictures.views.PictureList' ),

    #Admin End Points
    url( r'^admin/', include( admin.site.urls ) ),

    #Api REST End Points
    url(r'^', include( 'Pictures.urls' ) ),
)
