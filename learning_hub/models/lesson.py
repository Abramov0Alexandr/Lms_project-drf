from django.db import models
from learning_hub.services import lesson_upload_path


NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to=lesson_upload_path, verbose_name='Превью урока', **NULLABLE)
    video_link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс', related_name='course')

    def __str__(self):
        return f"{self.title} {self.course}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('pk',)
