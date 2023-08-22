from rest_framework import serializers
from .models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Payments.

    user: выводит email владельца курса вместо его ID
    paid_course: выводит название курса вместо его ID
    paid_lesson: выводит название урока вместо его ID
    """

    user = serializers.ReadOnlyField(source='user.email')
    paid_course = serializers.ReadOnlyField(source='paid_course.title')
    paid_lesson = serializers.ReadOnlyField(source='paid_lesson.title')

    class Meta:
        model = Payments
        fields = '__all__'
