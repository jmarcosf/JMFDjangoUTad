# -*- coding: utf-8 -*-
#**************************************************************************#
#*                                                                        *#
#* permissions.py                                                         *#
#* (c)2014 Jorge Marcos Fernandez                                         *#
#*                                                                        *#
#* Description: JMFDjangoUTad Project                                     *#
#*              Pictures REST Api End Point Permissions File              *#
#*              Practica Asignatura Backend de U-Tad                      *#
#*              www.u-tad.com                                             *#
#*                                                                        *#
#* Author:      Jorge Marcos Fernandez                                    *#
#*                                                                        *#
#**************************************************************************#
from rest_framework import permissions

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* CanListOrCreate Permission Class                                       *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class CanListOrCreate( permissions.BasePermission ):

    #**********************************************************************#
    #*                                                                    *#
    #* CanListOrCreate.has_permission()                                   *#
    #*                                                                    *#
    #**********************************************************************#
    def has_permission( self, request, view ):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'GET':
            return True

        return request.user.is_authenticated()

#**************************************************************************#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#* CanRetrieveUpdateOrDelete Permission Class                             *#
#*                                                                        *#
#*                                                                        *#
#*                                                                        *#
#**************************************************************************#
class CanRetrieveUpdateOrDelete( permissions.BasePermission ):

    #**********************************************************************#
    #*                                                                    *#
    #* CanRetrieveUpdateOrDelete.has_object_permission()                  *#
    #*                                                                    *#
    #**********************************************************************#
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET' and obj.isPublic == True:
            return True

        if request.user.is_authenticated():
            if ( request.user == obj.user or request.user.is_superuser ):
                return True

        return False