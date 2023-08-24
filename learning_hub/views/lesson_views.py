from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from learning_hub.models import Lesson
from learning_hub.permissions.common_permissions import IsModerator, IsNotModerator, IsSuperUser
from learning_hub.permissions.lesson_permissions import IsLessonOwner
from learning_hub.serializers import LessonSerializer


class LessonListApiView(generics.ListAPIView):
    """
    Контроллер для GET запросов информации об Уроке
    """

    serializer_class = LessonSerializer

    def get_queryset(self):
        """
        Метод преопределен для корректного вывода информации в зависимости от роли пользователя
        :return: список объектов в зависимости от роли авторизованного пользователя
        """

        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.groups.filter(
                name="Модераторы").exists():

            return Lesson.objects.all()

        return Lesson.objects.filter(lesson_owner=self.request.user)


class LessonCreateApiView(generics.CreateAPIView):
    """
    Контроллер для CREATE запросов при создании нового объекта класса Lesson
    Доступ к контроллеру имеют все кроме модераторов, суперюзер.
    """

    serializer_class = LessonSerializer
    permission_classes = [IsNotModerator | IsSuperUser]

    def perform_create(self, serializer):
        """
        Метод для автоматического определения текущего пользователя и заполнения поля 'lesson_owner'
        """

        new_lesson = serializer.save(lesson_owner=self.request.user)
        new_lesson.lesson_owner = self.request.user
        new_lesson.save()


class LessonRetrieveApiView(generics.RetrieveAPIView):
    """
    Контроллер для RETRIEVE запросов информации об Уроке
    Доступ к контроллеру имеют владелец урока, модераторы, суперюзер.
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsModerator | IsAdminUser]


class LessonUpdateApiView(generics.UpdateAPIView):
    """
    Контроллер для PUT, PATCH запросов при обновлении данных объектов класса Lesson
    Доступ к контроллеру имеют владелец урока, модераторы, суперюзер.
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsModerator | IsAdminUser]


class LessonDestroyApiView(generics.DestroyAPIView):
    """
    Контроллер для DELETE запросов.
    Доступ к контроллеру имеют владелец урока и суперюзер.
    """

    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsSuperUser]

