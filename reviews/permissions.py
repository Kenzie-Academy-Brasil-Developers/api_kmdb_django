from rest_framework import permissions


class MyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (request.user.is_authenticated and request.user.is_critic)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj.critic_id == request.user.id
