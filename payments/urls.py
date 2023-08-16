from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apps import PaymentsConfig
from .views import PaymentsListApiView

app_name = PaymentsConfig.name

urlpatterns = [
    path('', PaymentsListApiView.as_view(), name='payments'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
