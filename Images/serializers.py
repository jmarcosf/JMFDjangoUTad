# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* serializers.py                                                         *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Images REST Api End Point Serializers File                *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.contrib.auth.models import User
from rest_framework import serializers
from models import Image

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* ImageSerializer Class                                                  *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class ImageSerializer( serializers.ModelSerializer ):
    owner = serializers.Field( source = 'user.username' )
    image_url = serializers.Field( source = 'imageUrl.url', label = 'ImageURL' )

    class Meta:
        model = Image
        fields = ( 'imageUrl', 'owner', 'image_url' )











