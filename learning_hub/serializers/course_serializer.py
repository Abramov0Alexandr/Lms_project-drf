from rest_framework import serializers
from learning_hub.models import Course
from learning_hub.serializers.lesson_serializer import PreviewLessonSerializer, LessonSerializer


class CourseListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course. Вызывается при GET запросе

    lessons_count: выводит информацию о количестве уроков данного курса
    lessons_info: выводит сокращенную информацию о связанных с курсом уроках
    course_owner: выводит email владельца курса вместо его ID
    """

    lessons_count = serializers.SerializerMethodField()
    lessons_info = PreviewLessonSerializer(source='course', many=True, read_only=True)  #: Теперь, при создании через POST, это поле не будет требоваться к указанию (read_only=True)
    course_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(instance):
        return instance.course.all().count()


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course. Вызывается при RETRIEVE запросе

    lessons_count: выводит информацию о количестве уроков данного курса
    lessons_info: выводит полную информацию о связанных с курсом уроках
    course_owner: выводит email владельца курса вместо его ID
    """

    lessons_count = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(source='course', many=True, read_only=True)
    course_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(instance):
        return instance.course.all().count()
