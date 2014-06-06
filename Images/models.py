# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* models.py                                                              *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Images App Models File                                    *#
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
#*                                                                        *#
#* Image Model Class                                                      *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class Image( models.Model ):
    user                = models.ForeignKey( User, related_name = 'images' )
    imageUrl            = models.ImageField( upload_to = 'uploads', verbose_name = 'Image Location Url' )
    creationDate        = models.DateTimeField( auto_now_add = True, verbose_name = 'Creation Date' )

    def __unicode__( self ):
        return unicode( self.imageUrl )

