import os
from celery import shared_task
from django.core.mail import send_mail
from learning_hub.models import Lesson
from subscription.models import CourseSubscription


@shared_task
def send_course_update_notification(course_id: int):
    """
    subscribed_course: получение курса на который у пользователя оформлена подписка.
    new_course_lesson: получение информации о новом уроке
    """

    subscribed_course = CourseSubscription.objects.get(course=course_id, is_subscribed=True)
    new_course_lesson = Lesson.objects.filter(course_id=course_id).first()

    send_mail(
        subject=f'Курс "{subscribed_course.course.title}" обновился',
        message='У курса, на который вы подписаны, появились новые уроки или обновления.'
                f' Добавился новый урок "{new_course_lesson.title}".',
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=[subscribed_course.course.course_owner]
    )

    print(f'"{subscribed_course.course.title}" обновлен, сообщение отправлено')
