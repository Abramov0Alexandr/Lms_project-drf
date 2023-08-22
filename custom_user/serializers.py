from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    """

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        """
        :param validated_data: Данные, переданные при создании нового пользователя
        Метод переопределен для корректного создания нового пользователя.
        Пароль указанный при создании пользователя хэшируется, появляется возможность авторизации по JWT.
        :return: Создается новый экземпляр класса CustomUser
        """

        new_custom_user = CustomUser.objects.create_user(**validated_data)
        return new_custom_user
