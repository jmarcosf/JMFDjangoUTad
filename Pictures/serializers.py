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
#* PicturePublicSerializer Class                                          *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PicturePublicSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Picture

        fields = ( 'title', 'url' )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* PictureUserSerializer Class                                            *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureUserSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Picture

        fields = ( 'title', 'url', 'isPublic' )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* PictureDetailsSerializer Class                                         *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureDetailsSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Picture

        fields =\
        (
            'id', 'url', 'title', 'description', 'latitude', 'longitude',
            'isPublic', 'creationDate', 'modificationDate'
        )