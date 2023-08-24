from rest_framework.serializers import ValidationError


PERMISSIBLE_VALUE = "https://www.youtube.com"


def video_link_validator(video_link: str):
    if not video_link.startswith(PERMISSIBLE_VALUE):
        raise ValidationError('Недопустимая ссылка для видео')
