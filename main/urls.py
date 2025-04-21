from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),  # Главная страница
]
