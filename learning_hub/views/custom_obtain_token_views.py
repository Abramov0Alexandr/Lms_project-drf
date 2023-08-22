from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from learning_hub.serializers import MyTokenObtainPairSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    """
    Контроллер для получения JWT токена.
    Так как контроллеры для модели Курса написаны на основе ViewSet,
    то получение токена стандартным 'TokenObtainPairView' перестало быть возможным
    """

    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer
