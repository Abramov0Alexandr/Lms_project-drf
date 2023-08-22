from rest_framework import serializers, permissions
from learning_hub.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Lesson.
    Также используется, как вложенный сериализатор в CourseDetailSerializer при RETRIEVE запросе

    course_title: выводит информацию о названии курса
    lesson_owner: выводит email владельца урока вместо его ID
    """

    course_title = serializers.SerializerMethodField(read_only=True)
    lesson_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = '__all__'

    @staticmethod
    def get_course_title(instance):
        return instance.course.title


class PreviewLessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Lesson. Предоставляет краткую информацию об Уроке.
    Используется только при GET запросе информации об Уроках
    """

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'description',)
