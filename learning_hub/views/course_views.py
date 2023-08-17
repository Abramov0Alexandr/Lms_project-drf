from rest_framework import viewsets
from learning_hub.models import Course
from learning_hub.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
