from rest_framework import serializers, permissions
from learning_hub.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    course_title = serializers.SerializerMethodField(read_only=True)
    lesson_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = '__all__'

    @staticmethod
    def get_course_title(instance):
        return instance.course.title


class PreviewLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'description',)
