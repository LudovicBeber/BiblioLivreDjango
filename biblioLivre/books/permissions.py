from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Lecture ouverte à tous ; modification réservée aux admins."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOrOwnerOrAdmin(BasePermission):
    """Lecture ouverte à tous ; create aux authentifiés ; update/delete au créateur ou admin."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff
