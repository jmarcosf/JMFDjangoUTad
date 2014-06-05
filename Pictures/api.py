# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* api.py                                                                 *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures REST Api End Point Views File                    *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from rest_framework import generics
from Pictures.serializers import *
from Pictures.permissions import *

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* Picture List and Create End Point View Class                           *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureList( generics.ListCreateAPIView ):

    permission_classes = ( CanListOrCreate, )

    #**********************************************************************#
    #*                                                                    *#
    #* PictureList.pre_save()                                             *#
    #*                                                                    *#
    #**********************************************************************#
    def pre_save( self, obj ):
        obj.user = self.request.user

    #**********************************************************************#
    #*                                                                    *#
    #* PictureList.get_queryset()                                         *#
    #*                                                                    *#
    #**********************************************************************#
    def get_queryset( self ):
        if self.request.method == 'GET':
            if self.request.user.is_authenticated():
                PictureList = Picture.objects.filter( user = self.request.user )
            else:
                PictureList = Picture.objects.filter( isPublic = True )
            return PictureList

        return Picture.objects.all()

    #**********************************************************************#
    #*                                                                    *#
    #* PictureList.get_serializer_class()                                 *#
    #*                                                                    *#
    #**********************************************************************#
    def get_serializer_class( self ):
        if self.request.method == 'GET':
            if self.request.user.is_authenticated():
                Serializer = PictureUserSerializer
            else:
                Serializer = PicturePublicSerializer
            return Serializer

        return PictureDetailsSerializer

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* Picture Retrieve, Update and Destroy End Point View Class              *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureDetail( generics.RetrieveUpdateDestroyAPIView ):

    queryset = Picture.objects.all()
    serializer_class = PictureDetailsSerializer
    permission_classes = ( CanRetrieveUpdateOrDelete, )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* User List End Point View Class                                         *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class UserList( generics.ListAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* User Retrieve End Point View Class                                     *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class UserDetail( generics.RetrieveAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer