# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* api.py                                                                 *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Images REST Api End Point Views File                      *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from rest_framework import generics
from rest_framework import permissions
from Images.models import Image
from Images.serializers import *

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* Image Create End Point View Class                                      *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class ImageCreate( generics.CreateAPIView ):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #**********************************************************************#
    #*                                                                    *#
    #* ImageCreate.pre_save()                                             *#
    #*                                                                    *#
    #**********************************************************************#
    def pre_save( self, obj ):
        obj.user = self.request.user

