from django.contrib.auth.models import AbstractUser
from django.db import models

from custom_user.manager import CustomUserManager
from custom_user.services import upload_path


NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    fullname = models.CharField(max_length=50, verbose_name='Фамилия и имя пользователя', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    city = models.CharField(max_length=30, verbose_name='Город')
    avatar = models.ImageField(upload_to=upload_path, verbose_name='Аватар', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Статус активации')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
