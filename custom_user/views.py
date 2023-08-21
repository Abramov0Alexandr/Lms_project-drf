from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

