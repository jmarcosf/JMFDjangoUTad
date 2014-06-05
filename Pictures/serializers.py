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
from django.contrib.auth.models import User
from rest_framework import serializers
from models import Picture, UserSignUp

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

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* UserSignUpSerializer Class                                             *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class UserSignUpSerializer( serializers.Serializer ):

    first_name          = serializers.CharField()
    last_name           = serializers.CharField()
    username            = serializers.CharField()
    email               = serializers.EmailField()
    password            = serializers.CharField()
    password_confirm    = serializers.CharField()

    #**********************************************************************#
    #*                                                                    *#
    #* UserSignUpSerializer.restore_object()                              *#
    #*                                                                    *#
    #**********************************************************************#
    def restore_object( self, attrs, instance = None ):

        if instance is None:
            obj                         = UserSignUp()
            obj.first_name              = attrs.get( 'first_name', None )
            obj.last_name               = attrs.get( 'last_name', None )
            obj.username                = attrs.get( 'username', None )
            obj.email                   = attrs.get( 'email', None )
            obj.password                = attrs.get( 'password', None )
            obj.password_confirm        = attrs.get( 'password_confirm', None )
            return obj
        else:
            instance.first_name         = attrs.get( 'first_name', instance.first_name )
            instance.last_name          = attrs.get( 'last_name', instance.last_name )
            instance.username           = attrs.get( 'username', instance.username )
            instance.email              = attrs.get( 'email', instance.email )
            instance.password           = attrs.get( 'password', instance.password )
            instance.password_confirm   = attrs.get( 'password_confirm', instance.password_confirm )
            return instance
