from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    # Эндпоинт для регистрации пользователя
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    # Эндпоинт для получения JWT-токена
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Эндпоинт для обновления JWT-токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
