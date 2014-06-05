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
from django.contrib.auth.models import User
from models import Picture

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* PicturePublicSerializer Class                                          *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PicturePublicSerializer( serializers.ModelSerializer ):
    owner = serializers.Field( source = 'user.username' )

    class Meta:
        model = Picture
        fields = ( 'title', 'url', 'owner' )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* PictureUserSerializer Class                                            *#
#*                                                                        *#
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
#*                                                                        *#
#* PictureDetailsSerializer Class                                         *#
#*                                                                        *#
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

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* UserSerializer Class                                                   *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class UserSerializer( serializers.ModelSerializer ):

    class Meta:
        model = User
        fields = ( 'id', 'username', 'pictures' )