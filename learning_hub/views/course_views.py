from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from learning_hub.models import Course
from learning_hub.serializers import CourseSerializer


# ToDo: Закрыть эндпоинт для данного контроллера не авторизованным пользователям
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @action(detail=False, methods=['post'])
    def get_token(self, request):
        return TokenObtainPairView.as_view()(request=request._request)
