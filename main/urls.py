from django.urls import path

from main.apps import MainConfig
from main.views import BaseView, CategoryListView, ProductListView, ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    # Главная страница
    path('', BaseView.as_view(), name='home'),
    # Категории и подкатегории товаров
    path('categories/', CategoryListView.as_view(), name='categories'),
    # Категории и подкатегории товаров
    path('categories/<slug:slug>/', ProductListView.as_view(), name='product'),
    # Описание товара
    path('categories/<slug:slug>/product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
