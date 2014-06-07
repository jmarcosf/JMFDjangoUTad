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
from django.contrib.auth.models import User
from django.contrib.auth.hashers import  make_password
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Pictures.serializers import *
from Pictures.permissions import *
import datetime

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

    #**********************************************************************#
    #*                                                                    *#
    #* PictureDetail.post_save()                                          *#
    #*                                                                    *#
    #**********************************************************************#
    def post_save( self, obj, created = False ):
        obj.modificationDate = datetime.datetime.now()

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

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* User Sign Up End Point View Class                                      *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class SignUp( APIView ):

    #**********************************************************************#
    #*                                                                    *#
    #* SignUp.post()                                                      *#
    #*                                                                    *#
    #**********************************************************************#
    def post( self, request ):

        user_already_exists = unicode( '{&quot;username&quot; : &quot;already exists&quot;}', 'utf-8' )
        email_already_exists = unicode( '{&quot;email&quot; : &quot;already exists&quot;}', 'utf-8' )
        password_dont_match = unicode( '{&quot;password&quot; : &quot;password and password_confirm do not match&quot;}', 'utf-8' )

        serializer = UserSignUpSerializer( data = request.DATA )
        if serializer.is_valid():
            new_user = serializer.object
            if new_user.password != new_user.password_confirm:
                return Response( password_dont_match, status = status.HTTP_400_BAD_REQUEST )
            try:
                user = User.objects.get( username = new_user.username )
                return Response( user_already_exists, status = status.HTTP_400_BAD_REQUEST )
            except User.DoesNotExist:
                pass

            try:
                user = User.objects.get( email = new_user.email )
                return Response( email_already_exists, status = status.HTTP_400_BAD_REQUEST )
            except User.DoesNotExist:
                pass

            new_django_user             = User()
            new_django_user.first_name  = new_user.first_name
            new_django_user.last_name   = new_user.last_name
            new_django_user.username    = new_user.username
            new_django_user.email       = new_user.email
            new_django_user.password    = make_password( new_user.password )
            new_django_user.save()
            return Response( serializer.data )
        else:
            return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )
