import re
from rest_framework.serializers import ValidationError


ALLOWED_HOST = ["https://www.youtube.com"]


def video_link_validator(video_link: str):
    """
    Метод валидации поля 'video_link' класса Lesson
    :param video_link: ссылка на поле, в котором указывается URL ссылка для видео материала
    :return: в случае, если ссылка не входит в допустимый хост, то возбуждается ошибка 'ValidationError'
    """

    if not video_link.startswith(" ".join(ALLOWED_HOST)):
        raise ValidationError(f"Недопустимая ссылка для видео: {video_link}")


def description_validator(description: str):
    """
    Метод валидации поля 'description'
    :param: ссылка на поле, содержащее информацию об описании сущности
    :return: в случае, если в описании содержится ссылка, которая не входит в допустимый хост,
    то возбуждается ошибка 'ValidationError'
    """

    links = re.findall(r"https?://\S+", description)
    for host in links:
        if not host.startswith("https://www.youtube.com/"):
            raise ValidationError(f"Запрещено указывать ссылки на сторонние ресурсы: {host}")
