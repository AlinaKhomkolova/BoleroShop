from django.urls import path, include

from main.apps import MainConfig
from main.views import SubcategoryListAPIView, SubcategoryRetrieveUpdateDestroyAPIView, SubcategoryCreatedAPIView, \
    CategoryListAPIView, CategoryCreatedAPIView, CategoryRetrieveUpdateDestroyAPIView, ProductListAPIView

app_name = MainConfig.name

urlpatterns = [
    path('api/', include([
        # Список категорий
        path('category/', CategoryListAPIView.as_view(), name='category-list'),
        # Создание категории
        path('category/created/', CategoryCreatedAPIView.as_view(), name='category-created'),
        # Удаление, изменение, просмотр одной позиции
        path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-rud'),

        # Список подкатегорий
        path('subcategory/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
        # Создание подкатегории
        path('subcategory/created/', SubcategoryCreatedAPIView.as_view(), name='subcategory-created'),
        # Удаление, изменение, просмотр одной позиции товара
        path('subcategory/<int:pk>/', SubcategoryRetrieveUpdateDestroyAPIView.as_view(), name='subcategory-rud'),

        # Просмотр всех продуктов
        path('product/', ProductListAPIView.as_view(), name='product-list'),
    ]))
]
