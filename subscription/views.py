from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from learning_hub.models import Course
from subscription.models import CourseSubscription


class SubscribeToCourse(APIView):
    """
    Контроллер для осуществления подписки на курс
    """

    def post(self, request, course_id):
        """
        При вызове POST запроса с указанием id курса, создается экземпляр класса 'CourseSubscription',
        со следующей информацией:
        {'id': id экземпляра CourseSubscription, 'user': id пользователя, 'course': id курса, 'is_subscribed': True}

        :param course_id: id курса на который осуществляется подписка
        :return: Dictionary
        """

        course = Course.objects.get(pk=course_id)
        subscription, created = CourseSubscription.objects.get_or_create(user=request.user, course=course)
        subscription.is_subscribed = True
        subscription.save()
        return Response({'message': 'Вы успешно подписались на курс.'}, status=status.HTTP_200_OK)


class UnsubscribeFromCourse(APIView):
    """
    Контроллер для отмены подписки на курс
    """

    def post(self, request, course_id):
        """
        При вызове POST запроса с указанием id курса, происходит удаление экземпляр класса 'CourseSubscription',
        связанного с моделями CustomUser и Course

        :param course_id: id курса, для отмены подписки
        :return: Dictionary
        """

        course = Course.objects.get(pk=course_id)
        subscription = CourseSubscription.objects.get(user=request.user, course=course)
        subscription.delete()
        return Response({'message': 'Вы успешно отписались от курса.'}, status=status.HTTP_200_OK)
