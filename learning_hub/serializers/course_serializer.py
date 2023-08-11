from rest_framework import serializers, permissions
from learning_hub.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        permission_classes = [permissions.AllowAny]
        fields = '__all__'
