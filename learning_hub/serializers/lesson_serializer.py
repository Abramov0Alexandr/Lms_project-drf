from rest_framework import serializers, permissions
from learning_hub.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    course_title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        permission_classes = [permissions.AllowAny]
        fields = '__all__'

    @staticmethod
    def get_course_title(instance):
        return instance.course.title
