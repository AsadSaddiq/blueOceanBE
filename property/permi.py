from rest_framework import permissions
from rest_framework.permissions import BasePermission 


# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS
class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.author == request.user
        else:
            return False

class IsOwnerOfPost(BasePermission):
    def has_object_permission(self,request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.hotel.author == request.user
        else:
            return False