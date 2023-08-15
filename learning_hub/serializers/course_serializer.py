from rest_framework import serializers, permissions
from learning_hub.models import Course
from learning_hub.serializers.lesson_serializer import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(source='course', many=True, read_only=True)  #: Теперь, при создании через POST, это поле не будет требоваться к указанию (read_only=True)

    class Meta:
        model = Course
        permission_classes = [permissions.AllowAny]
        fields = '__all__'

    @staticmethod
    def get_lessons_count(instance):
        return instance.course.all().count()
