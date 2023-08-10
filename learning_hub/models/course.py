from django.db import models
from learning_hub.services import course_upload_path


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to=course_upload_path, verbose_name='Превью курса', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('pk',)
