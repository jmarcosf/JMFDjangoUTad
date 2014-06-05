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

    def get( self, request, format = None ):
        if request.user.is_authenticated():
            PictureList = Picture.objects.filter( user = request.user )
            serializer = PictureUserSerializer( PictureList, many = True )
        else:
            PictureList = Picture.objects.filter( isPublic = True )
            serializer = PicturePublicSerializer( PictureList, many = True )

        return Response( serializer.data )

    def post( self, request, format = None):
        serializer = PictureDetailsSerializer( data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = status.HTTP_201_CREATED )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Picture Retrieve, Update and Delete End Point View Class               *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureDetail( APIView ):

    def get_object( self, pk ):
        try:
            return Picture.objects.get( pk = pk )
        except Picture.DoesNotExist:
            raise Http404

    def get( self, request, pk, format = None ):
        picture = self.get_object( pk )
        if picture.isPublic == True or request.user == picture.user:
            serializer = PictureDetailsSerializer( picture )
        else:
            serializer = PicturePublicSerializer( picture )

        return Response( serializer.data )

    def put( self, request, pk, format = None ):
        snippet = self.get_object( pk )
        serializer = PictureDetailsSerializer( snippet, data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    def delete( self, request, pk, format = None ):
        snippet = self.get_object( pk )
        snippet.delete()
        return Response( status = status.HTTP_204_NO_CONTENT )










