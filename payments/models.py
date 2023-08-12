from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from learning_hub.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class Payments(models.Model):

    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('account_transfer', 'Банковский перевод'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_day = models.DateTimeField(default=timezone.now, verbose_name='День оплаты')

    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')

    payment_amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма оплаты')
    payment_type = models.CharField(max_length=17, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return f"Оплата {self.paid_course if self.paid_course else self.paid_lesson}"

    class Meta:
        verbose_name = 'Платежи'
        verbose_name_plural = 'Платежи'
        ordering = ('-payment_day',)
