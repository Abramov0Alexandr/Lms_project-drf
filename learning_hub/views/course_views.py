from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from learning_hub.models import Course
from learning_hub.pagination import CustomPaginationClass
from learning_hub.serializers import CourseListSerializer, CourseDetailSerializer
from learning_hub.permissions.course_permissions import IsCourseOwner
from learning_hub.permissions.common_permissions import IsModerator, IsNotModerator, IsSuperUser


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Контроллер для запросов POST, PUT, PATCH, DELETE
    Предоставляет всю информацию о Курсе
    """

    serializer_class = CourseListSerializer
    pagination_class = CustomPaginationClass

    permission_classes_by_action = {
        'create': [IsNotModerator | IsSuperUser],
        'update': [IsCourseOwner | IsModerator | IsAdminUser],
        'partial_update': [IsCourseOwner | IsModerator | IsAdminUser],
        'destroy': [IsCourseOwner | IsSuperUser],
    }

    def get_queryset(self):
        """
        Метод переопределен для корректного вывода информации в зависимости от роли пользователя
        :return: список объектов в зависимости от роли авторизованного пользователя
        """

        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.groups.filter(
                name="Модераторы").exists():
            return Course.objects.all()

        return Course.objects.filter(course_owner=self.request.user)

    def perform_create(self, serializer):
        """
        Метод для автоматического определения текущего пользователя и заполнения поля 'course_owner'
        """

        new_course = serializer.save(course_owner=self.request.user)
        new_course.course_owner = self.request.user
        new_course.save()

    def retrieve(self, request, *args, **kwargs):
        """
        Метод переопределен для вызова сериализатора 'CourseDetailSerializer' при RETRIEVE запросе
        """

        instance = self.get_object()
        serializer = CourseDetailSerializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Данный метод определяет право доступа к контроллеру в зависимости от роли пользователя.
        Если текущее действие не определено в словаре 'permission_classes_by_action',
        он возвращает список с правом доступа только для аутентифицированных пользователей.
        """

        if self.action in self.permission_classes_by_action:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        return [IsAuthenticated()]
