from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser
from learning_hub.models import Course


class LessonCreateTestCase(APITestCase):

    def setUp(self) -> None:
        """Предварительное создание БД для дальнейших тестов"""

        self.user = CustomUser.objects.create(
            email='user@email.dot',
            phone='70000000000',
            city='user city',
        )
        #
        self.course = Course.objects.create(
            title='test title for course',
            description='test description for course',
            course_owner=self.user,
        )

        """Переопределение клиента для принудительной авторизации, т.к. все эндпоинты закрыты JWT"""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тестирование создания нового урока при POST запросе"""

        data = {
            "title": "test title for lesson",
            "description": "test description for lesson",
            "course": self.course.id,
            "lesson_owner": self.user.id
        }

        response = self.client.post(
            reverse('course:lesson_create'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'course_title': self.course.title,
                'lesson_owner': self.user.email,
                'video_link': None,
                'description': data.get('description'),
                'title': data.get('title'),
                'preview': None,
                'course': self.course.id
            }
        )

    def test_create_lesson_video_link_error(self):
        """Тестирование валидации поля 'video_link' на указание сторонних ресурсов (кроме 'https://youtube.com') """

        data = {
            "title": "test title for lesson",
            "description": "test description for lesson",
            "video_link": "https://test.com/",
            "course": self.course.id,
            "lesson_owner": self.user.id
        }

        response = self.client.post(
            reverse('course:lesson_create'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_create_lesson_description_error(self):
        """Тестирование валидации поля 'description' на указание сторонних ресурсов (кроме 'https://youtube.com') """

        data = {
            "title": "test title for lesson",
            "description": "https://test.com/",
            "course": self.course.id,
            "lesson_owner": self.user.id
        }

        response = self.client.post(
            reverse('course:lesson_create'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
