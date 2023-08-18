from rest_framework import viewsets, mixins
from learning_hub.models import Course
from learning_hub.serializers import CourseListSerializer, CourseDetailSerializer


class CourseViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()


class CourseDetailViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

