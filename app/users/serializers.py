from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': {
                'write_only': True,
                "min_length": 8,
                "style": {"input_type": "password"}
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class TokenSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        style={'input_type': "password"},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password
            )

        if not user:
            msg = "Unable to log in with provided credentials."
            raise serializers.ValidationError(_(msg), code="authorization")

        data['user'] = user
        return data
