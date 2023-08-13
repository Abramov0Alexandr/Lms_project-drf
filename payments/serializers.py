from rest_framework import serializers, permissions
from .models import Payments


class PaymentsSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    paid_course = serializers.ReadOnlyField(source='paid_course.title')
    paid_lesson = serializers.ReadOnlyField(source='paid_lesson.title')

    class Meta:
        model = Payments
        permission_classes = [permissions.AllowAny]
        fields = '__all__'
