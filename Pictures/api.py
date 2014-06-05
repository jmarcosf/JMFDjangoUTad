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
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from models import Picture
from Pictures.serializers import *

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Picture List and Create End Point View Class                           *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureList( APIView ):

    #**********************************************************************#
    #*                                                                    *#
    #* GET (List) Method                                                  *#
    #*                                                                    *#
    #**********************************************************************#
    def get( self, request, format = None ):
        if request.user.is_authenticated():
            PictureList = Picture.objects.filter( user = request.user )
            serializer = PictureUserSerializer( PictureList, many = True )
        else:
            PictureList = Picture.objects.filter( isPublic = True )
            serializer = PicturePublicSerializer( PictureList, many = True )

        return Response( serializer.data )

    #**********************************************************************#
    #*                                                                    *#
    #* POST (Create) Method                                               *#
    #*                                                                    *#
    #**********************************************************************#
    def post( self, request, format = None):
        if not request.user.is_authenticated():
            return Response( status = status.HTTP_401_UNAUTHORIZED )

        serializer = PictureDetailsSerializer( data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = status.HTTP_201_CREATED )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Picture Retrieve, Update and Destroy End Point View Class              *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureDetail( APIView ):

    def get_object( self, pk ):
        try:
            return Picture.objects.get( pk = pk )
        except Picture.DoesNotExist:
            raise Http404

    #**********************************************************************#
    #*                                                                    *#
    #* GET (Retrieve) Method                                              *#
    #*                                                                    *#
    #**********************************************************************#
    def get( self, request, pk, format = None ):
        picture = self.get_object( pk )
        if picture.isPublic == True or request.user == picture.user:
            serializer = PictureDetailsSerializer( picture )
        else:
            serializer = PicturePublicSerializer( picture )

        return Response( serializer.data )

    #**********************************************************************#
    #*                                                                    *#
    #* PUT (Update) Method                                                *#
    #*                                                                    *#
    #**********************************************************************#
    def put( self, request, pk, format = None ):
        if not request.user.is_authenticated():
            return Response( status = status.HTTP_401_UNAUTHORIZED )

        picture = self.get_object( pk )
        if not request.user == picture.user and not request.user.is_superuser:
            return Response( status = status.HTTP_401_UNAUTHORIZED )

        serializer = PictureDetailsSerializer( picture, data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    #**********************************************************************#
    #*                                                                    *#
    #* DELETE (Destroy) Method                                            *#
    #*                                                                    *#
    #**********************************************************************#
    def delete( self, request, pk, format = None ):
        if not request.user.is_authenticated():
            return Response( status = status.HTTP_401_UNAUTHORIZED )

        picture = self.get_object( pk )
        if not request.user == picture.user and not request.user.is_superuser:
            return Response( status = status.HTTP_401_UNAUTHORIZED )

        picture.delete()
        return Response( status = status.HTTP_204_NO_CONTENT )

