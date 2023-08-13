from rest_framework import serializers, permissions
from learning_hub.models import Course
from learning_hub.serializers.lesson_seriaizer import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.IntegerField(source='course.all.count', read_only=True)
    lessons_info = LessonSerializer(source='course', many=True)

    class Meta:
        model = Course
        permission_classes = [permissions.AllowAny]
        fields = '__all__'
