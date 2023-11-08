from rest_framework import permissions


class IsAuthenticatedOnRetrieve(permissions.BasePermission):
    """Permission to allow creation without authentication but using it to
    retrieve data.
    """

    def has_permission(self, request, view):
        # For creation requests, POST, allow
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated


class NoDeletes(permissions.BasePermission):
    """Doesn't allow deletes for the resource."""

    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return False
        return True


class NoUpdates(permissions.BasePermission):
    """Doesn't allow deletes for the resource."""

    def has_permission(self, request, view):
        if request.method in ("PUT", "PATCH"):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "PATCH"):
            return False
        return True


class IsSuperUser(permissions.BasePermission):
    """Check if User is SuperUser"""

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
