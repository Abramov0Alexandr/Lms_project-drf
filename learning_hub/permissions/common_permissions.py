from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Данный класс определяет права доступа к контроллерам для определенной группы пользователей.
    В данную группу входят модераторы, суперпользователи или пользователями, у которых указан флаг is_staff.
    """

    def has_permission(self, request, view):
        """
        :return: Метод возвращает булевые значения. В случае, если это True, то доступ предоставляется и наоборот.
        """

        if request.user.is_superuser or request.user.is_staff:
            return True

        return request.user.groups.filter(
            name="Модераторы").exists()


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
