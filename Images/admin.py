# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* admin.py                                                               *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Images App Admin Models File                              *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.contrib import admin
from models import Image

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* ImageAdmin Class                                                       *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class ImageAdmin( admin.ModelAdmin ):
    list_display    = ( 'user', 'imageUrl' )
    list_filter     = ( 'creationDate', )
    search_fields   = ( 'imageUrl', 'creationDate' )
    ordering        = ( '-creationDate', )
    readonly_fields = ( 'creationDate', )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Image Admin Register                                                   *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
admin.site.register( Image, ImageAdmin )


