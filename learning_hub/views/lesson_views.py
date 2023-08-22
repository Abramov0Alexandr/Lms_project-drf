from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from learning_hub.models import Lesson
from learning_hub.permissions.lesson_permissions import IsLessonOwner
from learning_hub.permissions.common_permissions import IsModerator, IsNotModerator
from learning_hub.serializers import LessonSerializer


class LessonListApiView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):

        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.groups.filter(
                name="Модераторы").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(lesson_owner=self.request.user)


class LessonCreateApiView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsNotModerator | IsAdminUser]

    def perform_create(self, serializer):
        new_lesson = serializer.save(lesson_owner=self.request.user)
        new_lesson.lesson_owner = self.request.user
        new_lesson.save()


class LessonRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsModerator | IsAdminUser]


class LessonUpdateApiView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsModerator | IsAdminUser]


class LessonDestroyApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsAdminUser]

