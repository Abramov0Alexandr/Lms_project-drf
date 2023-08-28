from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Данный класс определяет права доступа к контроллерам для определенной группы пользователей.
    В данную группу входят модераторы или пользователи, у которых указан флаг is_staff.
    """

    def has_permission(self, request, view):
        """
        :return: Метод возвращает булевые значения. В случае, если это True, то доступ предоставляется и наоборот.
        """

        return bool(request.user.groups.filter(name="Модераторы").exists())


class IsNotModerator(BasePermission):
    """
    Данный класс определяет права доступа к контроллерам для обычных пользователей (не являются модераторами,
    флаг is_staff=False.
    """

    def has_permission(self, request, view):
        """
        :return: Метод возвращает булевые значения. В случае, если это True, то доступ предоставляется и наоборот.
        """

        return not (request.user.is_staff or request.user.groups.filter(name="Модераторы").exists())


class IsSuperUser(BasePermission):
    """
    Данный класс определяет права доступа для пользователей, у которых стоит флаг 'is_superuser'.
    В отличие от IsAdminUser, 'IsSuperUser' предоставляет доступ только суперпользователям
    """

    def has_permission(self, request, view):
        return bool(request.user.is_superuser)
