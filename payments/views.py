from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .models import Payments
from .serializers import PaymentsSerializer


class PaymentsListApiView(generics.ListAPIView):
    """
    Контроллер для вывода информации об объектах класса Payments
    filterset_fields: возможность фильтрации по оплаченным курсам, урокам и типу оплаты
    ordering_fields: возможность изменить упорядочивание по дате оплаты
    """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_type')
    ordering_fields = ('payment_day', )
