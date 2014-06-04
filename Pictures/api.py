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
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from serializers import PublicPictureSerializer, UserPictureSerializer
from models import Picture

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* PictureList End Point Class                                            *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class PictureList( APIView ):

    def get( self, request ):
        if request.user.is_authenticated():
            PictureList = Picture.objects.filter( user = request.user )
            serializer = UserPictureSerializer( PictureList, many = True )
        else:
            PictureList = Picture.objects.filter( isPublic = True )
            serializer = PublicPictureSerializer( PictureList, many = True )

        return Response( serializer.data )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Picture End Point Class                                                *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class Picture( generics.CreateAPIView ):

    def post( self, request ):
        if request.DATA:
            if request.user.is_authenticated():
                serializer = NewPictureSerializer( data = request.DATA )
                serializer.save()
                return Response( serializer.data )
            else:
                return Response( status = status.HTTP_401_UNAUTHORIZED )
        else:
            return Response( status = status.HTTP_400_BAD_REQUEST )














