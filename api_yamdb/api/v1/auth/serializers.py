from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.validators import EmailValidator
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework_simplejwt.tokens import RefreshToken

from ..validators import validate_username

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[validate_username,
                    ]
    )
    email = serializers.EmailField(
        max_length=150,
        required=True,
        validators=[EmailValidator(),
                    ]
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def validate(self, attrs):
        if User.objects.filter(
            (Q(username=attrs['username']) & ~Q(email=attrs['email']))
            | (~Q(username=attrs['username']) & Q(email=attrs['email']))
        ).exists():
            raise ValidationError(
                {'username': 'Поле должно быть уникальным.',
                 'email': 'Поле должно быть уникальным.',
                 }
            )
        return attrs


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    confirmation_code = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = attrs['username']
        confirmation_code = attrs['confirmation_code']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound('Такого пользователя не существует.')

        if not default_token_generator.check_token(user, confirmation_code):
            raise ValidationError(
                {'confirmation_code': 'Неверный код подтверждения.'}
            )

        jwt_token = RefreshToken.for_user(user)

        return {
            'access_token': str(jwt_token.access_token),
            'refresh_token': str(jwt_token),
        }
