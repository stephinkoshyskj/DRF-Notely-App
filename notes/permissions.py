from rest_framework.permissions import BasePermission

"""
custom permissions

"""
class OwnerOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner   #returns true or false