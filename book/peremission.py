from rest_framework import permissions


class IsUserOwnerOrGetOrPostOnly(permissions.BasePermission):
    """
    Custom permission to allow only user of review to edit the review
    """
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return obj.user == request.user

        return False