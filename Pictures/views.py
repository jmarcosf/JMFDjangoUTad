# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* views.py                                                               *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures App Views File                                   *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import Http404, HttpResponseServerError
from models import Picture

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* PictureList View                                                       *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
def PictureList( request ):

    RequestUser = None
    PublicPictureList = None
    OwnPictureList = None

    try:
        RequestUser = User.objects.get( username = request.user.username )
        PublicPictureList = Picture.objects.filter( isPublic = True ).exclude( user = RequestUser )
        if RequestUser.is_authenticated():
            OwnPictureList = Picture.objects.filter( user = request.user )

    except:
        PublicPictureList = Picture.objects.filter( isPublic = True )

    PictureListContext =\
    {
        'RequestUser'       : RequestUser,
        'PublicPictureList' : PublicPictureList,
        'OwnPictureList'    : OwnPictureList,
    }
    return render( request, 'picture_list.html', PictureListContext )

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* User Public Pictures List View                                         *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
def UserPublicPictures( request, urlUserName ):

    RequestUser = None
    PublicPictureList = None

    try:
        RequestUser = User.objects.get( username__iexact = urlUserName.strip( '/' ) )
        PublicPictureList = Picture.objects.filter( isPublic = True ).filter( user = RequestUser )

        context =\
        {
            'RequestUser'       : RequestUser,
            'PublicPictureList' : PublicPictureList,
            'OwnPictureList'    : None,
        }
        return render( request, 'user_public_picture_list.html', context )

    except User.DoesNotExist:
        raise Http404

    except:
        raise HttpResponseServerError

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#* Logout View                                                            *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
def Logout( request ):
    logout( request )
    return render( request, 'registration/logout.html' )
