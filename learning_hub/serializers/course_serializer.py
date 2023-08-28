from rest_framework import serializers
from learning_hub.models import Course
from learning_hub.serializers.lesson_serializer import PreviewLessonSerializer, LessonSerializer
from subscription.models import CourseSubscription
from ..validators import description_validator


class CourseListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course. Вызывается при GET запросе

    lessons_count: выводит информацию о количестве уроков данного курса
    lessons_info: выводит сокращенную информацию о связанных с курсом уроках
    course_owner: выводит email владельца курса вместо его ID
    is_subscribed: показывает информацию о статусе подписки на курс True/False
    """

    lessons_count = serializers.SerializerMethodField()
    lessons_info = PreviewLessonSerializer(source='course', many=True, read_only=True)
    #: Теперь, при создании через POST, это поле не будет требоваться к заполнению (read_only=True)

    course_owner = serializers.CharField(default=serializers.CurrentUserDefault())
    description = serializers.CharField(validators=[description_validator])

    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(instance):
        return instance.course.all().count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return CourseSubscription.objects.filter(user=user, course=obj).exists()


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course. Вызывается при RETRIEVE запросе

    lessons_count: выводит информацию о количестве уроков данного курса
    lessons_info: выводит полную информацию о связанных с курсом уроках
    course_owner: выводит email владельца курса вместо его ID
    is_subscribed: показывает информацию о статусе подписки на курс True/False
    """

    lessons_count = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(source='course', many=True, read_only=True)
    course_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(instance):
        return instance.course.all().count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return CourseSubscription.objects.filter(user=user, course=obj).exists()
