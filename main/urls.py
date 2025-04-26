from django.urls import path

from main.apps import MainConfig
from main.views import SubcategoryListAPIView, SubcategoryRetrieveUpdateDestroyAPIView, SubcategoryCreatedAPIView, \
    CategoryListAPIView, CategoryCreatedAPIView, CategoryRetrieveUpdateDestroyAPIView, ProductListAPIView

app_name = MainConfig.name

urlpatterns = [
    # Список категорий
    path('api/category/', CategoryListAPIView.as_view(), name='category-list'),
    # Создание категории
    path('api/category/created/', CategoryCreatedAPIView.as_view(), name='category-created'),
    # Удаление, изменение, просмотр одной позиции
    path('api/category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-rud'),

    # Список подкатегорий
    path('api/subcategory/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
    # Создание подкатегории
    path('api/subcategory/created/', SubcategoryCreatedAPIView.as_view(), name='subcategory-created'),
    # Удаление, изменение, просмотр одной позиции товара
    path('api/subcategory/<int:pk>/', SubcategoryRetrieveUpdateDestroyAPIView.as_view(), name='subcategory-rud'),

    # Просмотр всех продуктов
    path('api/product/', ProductListAPIView.as_view(), name='product-list'),
]
