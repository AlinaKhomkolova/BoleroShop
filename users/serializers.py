from django.contrib.auth.password_validation import validate_password
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Основной сериализатор для модели пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'date_of_birth']

    def create(self, validated_data):
        """Создание пользователя с генерацией slug из username"""
        slug = slugify(validated_data['username'])

        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            slug=slug,
            date_of_birth=validated_data.get('date_of_birth')
        )
        return user

    def get_tokens(self, user):
        """Генерация JWT-токенов при успешной регистрации"""
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
