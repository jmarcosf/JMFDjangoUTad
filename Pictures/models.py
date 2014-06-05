# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* models.py                                                              *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures App Models File                                  *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.db import models
from django.contrib.auth.models import User

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Picture Model Class                                                    *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class Picture( models.Model ):
    user                = models.ForeignKey( User, related_name = 'pictures' )
    url                 = models.URLField()
    title               = models.CharField( max_length = 50 )
    description         = models.CharField( max_length = 300 )
    latitude            = models.FloatField( null = True, blank = True )
    longitude           = models.FloatField( null = True, blank = True )
    isPublic            = models.BooleanField( verbose_name = 'Public?' )
    creationDate        = models.DateTimeField( auto_now_add = True, verbose_name="Creation Date" )
    modificationDate    = models.DateTimeField( auto_now_add = True, verbose_name="Modification Date" )

    def __unicode__( self ):
        return self.title

    def coordinates( self ):
        return str( self.latitude ) + ', ' + str( self.longitude )

    class Meta:
        ordering = ['title']




#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* RegisterUser Model Class                                               *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class RegisterUser( object ):

    def __init__( self, *args, **kwargs ):
        self.first_name         = kwargs.get( 'first_name', None )
        self.last_name          = kwargs.get( 'last_name', None )
        self.username           = kwargs.get( 'username', None )
        self.email              = kwargs.get( 'email', None )
        self.password           = kwargs.get( 'password', None )
        self.password_confirm   = kwargs.get( 'password_confirm', None )



