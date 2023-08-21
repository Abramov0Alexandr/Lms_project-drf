from rest_framework import serializers
from learning_hub.models import Course
from learning_hub.serializers.lesson_serializer import PreviewLessonSerializer, LessonSerializer


class CourseListSerializer(serializers.ModelSerializer):

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

    lessons_count = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(source='course', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(instance):
        return instance.course.all().count()
