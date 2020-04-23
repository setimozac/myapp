from .serializers import UserSerializer

from rest_framework import generics


class CreateView(generics.CreateAPIView):

    serializer_class = UserSerializer
