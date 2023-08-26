from django.db import models
from django.contrib.auth import get_user_model
from learning_hub.models import Course


class CourseSubscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subscribed_user', verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscribed_course', verbose_name='Курс в подписке')
    is_subscribed = models.BooleanField(default=False, verbose_name='Подписка осуществлена')

    class Meta:
        verbose_name = 'Подписка на курсы'
        verbose_name_plural = 'Подписки на курсы'
        ordering = ('course', 'is_subscribed')
