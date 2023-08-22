from rest_framework.permissions import BasePermission


class IsCourseOwner(BasePermission):
    """
    Данный класс определяет право доступа авторизованного пользователя к экземплярам класса Course.
    """

    def has_object_permission(self, request, view, obj):
        """
        Метод проверяет является ли текущий пользователь владельцем курса.

        :return: В результате проверки возвращается булевые значения.
        В случае, если текущий пользователь владелец курса (True) - то доступ разрешен.
        """

        if request.user == obj.course_owner:
            return True

        return False
