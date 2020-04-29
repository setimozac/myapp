from .serializers import UserSerializer, TokenSerializer

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken


class CreateView(generics.CreateAPIView):

    serializer_class = UserSerializer


class TokenView(ObtainAuthToken):

    serializer_class = TokenSerializer
