from rest_framework import generics, status
from rest_framework.response import Response

from users.serializers import UserRegistrationSerializer, UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """Вью для регистрации пользователя"""
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """Обработка POST-запроса для создания пользователя"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Создание пользователя через сериалайзер
        tokens = serializer.get_tokens(user)  # Получение JWT-токенов
        return Response({
            "user": UserSerializer(user).data,  # Возвращаем данные пользователя
            "tokens": tokens  # Возвращаем токены для авторизации
        }, status=status.HTTP_201_CREATED)
