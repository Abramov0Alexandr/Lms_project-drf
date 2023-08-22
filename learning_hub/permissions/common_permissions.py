from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True

        return request.user.groups.filter(
            name="Модераторы").exists()


class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        return not (request.user.is_staff or request.user.groups.filter(name="Модераторы").exists())
