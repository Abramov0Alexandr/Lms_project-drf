from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from learning_hub.models import Course
from subscription.models import CourseSubscription


class SubscribeToCourse(APIView):
    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        subscription, created = CourseSubscription.objects.get_or_create(user=request.user, course=course)
        subscription.is_subscribed = True
        subscription.save()
        return Response({'message': 'Вы успешно подписались на курс.'}, status=status.HTTP_200_OK)


class UnsubscribeFromCourse(APIView):
    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        subscription = CourseSubscription.objects.get(user=request.user, course=course)
        subscription.delete()
        return Response({'message': 'Вы успешно отписались от курса.'}, status=status.HTTP_200_OK)
