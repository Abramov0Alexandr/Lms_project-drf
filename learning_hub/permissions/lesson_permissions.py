from rest_framework.permissions import BasePermission


class IsLessonOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.lesson_owner:
            return True
        return False
