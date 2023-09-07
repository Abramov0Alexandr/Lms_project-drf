from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from custom_user.models import CustomUser


@shared_task()
def check_user_activity():

    user_group_exception = {'is_superuser': False, 'is_staff': False}

    # Определяем дату, которая находится за месяцем назад от текущей даты
    one_month_ago = timezone.now() - timedelta(days=30)

    # Получаем список пользователей, которые не заходили более месяца и ещё активны
    inactive_users = CustomUser.objects.filter(last_login__lte=one_month_ago, is_active=True, **user_group_exception)

    # Устанавливаем флаг is_active в False для найденных пользователей
    if inactive_users:

        for user in inactive_users:
            print(f'{user.email} был заблокирован', sep='\n')
            user.is_active = False
            user.save()


