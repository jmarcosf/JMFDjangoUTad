# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* views.py                                                               *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Images App Views File                                     *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.shortcuts import render
from django.http import Http404, HttpResponseServerError
from models import Image

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* Show Image View                                                        *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
def ShowImage( request, imageName ):

    ImageRequested = None

    try:
        ImageRequested = Image.objects.get( imageUrl__icontains = imageName )

        context = { 'Image' : ImageRequested, }
        return render( request, 'show_picture.html', context )

    except Image.DoesNotExist:
        raise Http404

    except:
        raise HttpResponseServerError

