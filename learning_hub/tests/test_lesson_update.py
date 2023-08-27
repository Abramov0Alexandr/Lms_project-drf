from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser
from learning_hub.models import Course, Lesson


class LessonUpdateTestCase(APITestCase):

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

    def test_patch_lesson(self):
        """
        Тестирование обновления полей экземпляра класса 'Lesson' при вызове PATCH запроса
        """

        data = {
            "title": "new test title",
            "description": "new test description",
        }

        response = self.client.patch(
            '/lesson/update/1/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.id,
                'course_title': self.course.title,
                'lesson_owner': self.user.email,
                'video_link': None,
                'description': 'new test description',
                'title': 'new test title',
                'preview': None,
                'course': self.lesson.id
            }
        )

    def test_update_lesson(self):
        """
        Тестирование обновления полей экземпляра класса 'Lesson' при вызове PUT запроса
        """

        data = {
            "title": "another one new test title",
            "description": "another one new test description",
            "course": self.course.id
        }

        response = self.client.put(
            '/lesson/update/2/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.course.id,
                'course_title': self.course.title,
                'lesson_owner': self.user.email,
                'video_link': None,
                'description': 'another one new test description',
                'title': 'another one new test title',
                'preview': None,
                'course': self.course.id
            }
        )

