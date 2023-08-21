from django.urls import path
from .apps import CustomUserConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomUserListCreateView


app_name = CustomUserConfig.name

urlpatterns = [
    path('', CustomUserListCreateView.as_view(), name='custom_user'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
