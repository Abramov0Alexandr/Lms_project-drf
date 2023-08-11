from rest_framework import generics
from learning_hub.models import Lesson
from learning_hub.serializers import LessonSerializer


class LessonListApiView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateApiView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateApiView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
