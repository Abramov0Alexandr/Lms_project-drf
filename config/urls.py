"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="LMS project API",
      default_version='v1',
      description="Description for LMS project. "
                  "Here you can find all the information about requests and check them",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(url="https://github.com/Abramov0Alexandr"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_hub.urls', namespace='course')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('custom-user/', include('custom_user.urls', namespace='custom_user')),
    path('course-subscription/', include('subscription.urls', namespace='subscription')),


    # Creating settings for drf-yasg
    # https://drf-yasg.readthedocs.io/en/stable/readme.html#quickstart

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
