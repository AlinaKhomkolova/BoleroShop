from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    path('api/', include([
        # Эндпоинт для регистрации пользователя
        path('register/', UserRegistrationView.as_view(), name='register'),
        # Эндпоинт для получения JWT-токена
        path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        # Эндпоинт для обновления JWT-токена
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]))
]
