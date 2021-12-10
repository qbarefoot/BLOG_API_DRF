from rest_framework import permissions


"""IsOwnerOrReadOnly permission checks whether the requesting user is the owner of the given object. Owners can perform actions such as updating or deleting a post"""
"""Non-owners can still retrieve a post, since this is a read-only action"""
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user