from rest_framework import serializers, permissions
from learning_hub.models import Course


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.IntegerField(source='course.all.count', read_only=True)

    class Meta:
        model = Course
        permission_classes = [permissions.AllowAny]
        fields = '__all__'
