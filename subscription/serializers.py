from rest_framework import serializers
from subscription.models import CourseSubscription


class CourseSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        class Meta:
            model = CourseSubscription
            fields = '__all__'
