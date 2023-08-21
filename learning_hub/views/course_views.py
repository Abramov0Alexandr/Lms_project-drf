from rest_framework import viewsets, mixins
from learning_hub.models import Course
from learning_hub.serializers import CourseListSerializer, CourseDetailSerializer


class CourseViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        new_course = serializer.save(course_owner=self.request.user)
        new_course.course_owner = self.request.user
        new_course.save()


class CourseDetailViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

