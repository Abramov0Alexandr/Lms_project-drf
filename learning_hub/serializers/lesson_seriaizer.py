from rest_framework import serializers, permissions
from learning_hub.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        permission_classes = [permissions.AllowAny]
        fields = '__all__'