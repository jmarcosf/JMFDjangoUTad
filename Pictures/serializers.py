# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* serializers.py                                                         *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures REST Api End Point Serializers File              *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from rest_framework import serializers
from models import Picture

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* PublicPictureSerializer Class                                          *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PublicPictureSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Picture
        fields = ( 'id', 'title', 'url' )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* UserPictureSerializer Class                                            *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class UserPictureSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Picture
        fields = ( 'id', 'title', 'url', 'isPublic' )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* NewPictureSerializer Class                                             *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class NewPictureSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Picture
        fields = ( 'user', 'title', 'url', 'description', 'latitude', 'longitude', 'isPublic', )

