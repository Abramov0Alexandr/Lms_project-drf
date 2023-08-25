import re
from rest_framework.serializers import ValidationError


ALLOWED_HOST = ["https://www.youtube.com"]


def video_link_validator(video_link: str):
    if not video_link.startswith(" ".join(ALLOWED_HOST)):
        raise ValidationError(f"Недопустимая ссылка для видео: {video_link}")


def description_validator(description: str):
    links = re.findall(r"https?://\S+", description)
    for host in links:
        if not host.startswith("https://www.youtube.com/"):
            raise ValidationError(f"Запрещено указывать ссылки на сторонние ресурысы: {host}")
