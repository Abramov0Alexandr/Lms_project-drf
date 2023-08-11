from rest_framework import serializers, permissions
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        permission_classes = [permissions.AllowAny]
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        permission_classes = [permissions.AllowAny]
        fields = '__all__'
