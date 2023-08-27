from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser
from learning_hub.models import Course


class CourseSubscribtionTestCase(APITestCase):

    def setUp(self) -> None:
        """Предварительное создание БД для дальнейших тестов"""

        self.user = CustomUser.objects.create(
            email='user@email.dot',
            phone='70000000000',
            city='user city',
        )

        self.course = Course.objects.create(
            title='test title for course',
            description='test description for course',
            course_owner=self.user,
        )

        """Переопределение клиента для принудительной авторизации, т.к. все эндпоинты закрыты JWT"""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscribing_for_course(self):
        """Тестирование подписки на курс"""

        course_subscribe_response = self.client.post(
            '/course-subscription/subscribe/1/'
        )

        self.assertEqual(
            course_subscribe_response.status_code,
            status.HTTP_200_OK
        )

        """Проверка наличия подписки у пользователя"""
        course_data_response = self.client.get('/course/1/').json()

        self.assertTrue(
            course_data_response.get('is_subscribed')
        )
