# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* admin.py                                                               *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures App Admin Models File                            *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.contrib import admin
from models import Picture

class PictureAdmin( admin.ModelAdmin ):
    list_display    = ( 'user', 'title', 'url', 'coordinates', 'modificationDate', 'isPublic' )
    list_filter     = ( 'modificationDate', )
    search_fields   = ( 'title', 'creationDate', 'modificationDate' )
    ordering        = ( '-modificationDate', )
    readonly_fields = ( 'creationDate', 'modificationDate', )

    fieldsets =\
    (
        ( 'User',       { 'fields'      : ('user',),
                          'description' : 'Select Picture User:' } ),
        ( 'Data',       { 'fields'      : ( 'title', 'description', 'url', 'isPublic' ), } ),
        ( 'Location',   { 'fields'      : ( ( 'latitude', 'longitude' ), ),
                          'classes'     : ( 'wide', 'expand', ),
                          'description' : 'Enter coordiantes values:' } ),
        ( 'Dates',      { 'fields'      : ( 'creationDate', 'modificationDate' ), } ),
    )

    def coordinates( self, obj ):
        return str( obj.latitude ) + ', ' + str( obj.longitude )

    coordinates.admin_order_field = 'latitude'

admin.site.register( Picture, PictureAdmin )

