from rest_framework.permissions import BasePermission


class IsLessonOwner(BasePermission):
    """
    Данный класс определяет право доступа авторизованного пользователя к экземплярам класса Lesson.
    """

    def has_object_permission(self, request, view, obj):
        """
        Метод проверяет является ли текущий пользователь владельцем урока.

        :return: В результате проверки возвращается булевые значения.
        В случае, если текущий пользователь владелец урока (True) - то доступ разрешен.
        """

        if request.user == obj.lesson_owner:
            return True
        return False
