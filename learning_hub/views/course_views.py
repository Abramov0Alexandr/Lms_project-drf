from rest_framework import viewsets, mixins
from rest_framework.response import Response
from learning_hub.models import Course
from learning_hub.serializers import CourseListSerializer, CourseDetailSerializer


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        new_course = serializer.save(course_owner=self.request.user)
        new_course.course_owner = self.request.user
        new_course.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseDetailSerializer(instance)
        return Response(serializer.data)

