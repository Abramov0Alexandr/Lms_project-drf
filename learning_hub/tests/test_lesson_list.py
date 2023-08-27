from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser
from learning_hub.models import Lesson, Course


class LessonListTestCase(APITestCase):

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

        self.lesson = Lesson.objects.create(
            title='test title for lesson',
            description='test description for lesson',
            course=self.course,
            lesson_owner=self.user
        )

        """Переопределение клиента для принудительной авторизации, т.к. все эндпоинты закрыты JWT"""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_lesson(self):
        """Тестирование вывода информации о списке уроков при GET запросе"""

        response = self.client.get(
            reverse('course:lesson_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {'id': self.lesson.id,
                         'course_title': self.course.title,
                         'lesson_owner': self.user.email,
                         'video_link': None,
                         'description': self.lesson.description,
                         'title': self.lesson.title,
                         'preview': None,
                         'course': self.course.id
                         }
                    ]
                }
        )
