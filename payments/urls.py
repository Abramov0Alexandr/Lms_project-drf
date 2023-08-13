from django.urls import path
from .apps import PaymentsConfig
from .views import PaymentsListApiView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payments', PaymentsListApiView.as_view(), name='payments'),
]