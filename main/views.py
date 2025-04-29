from rest_framework import generics

from main.models import Product, Category, Subcategory
from main.paginators import Pagination
from main.serializers import ProductSerializer, SubcategorySerializer, CategoryListSerializer, \
    CategoryCreatedSerializer, CategoryRUDSerializer


class CategoryListAPIView(generics.ListAPIView):
    """Вывод списка категорий"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = Pagination


class CategoryCreatedAPIView(generics.CreateAPIView):
    """Создание категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryCreatedSerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Удаление, изменение, просмотри одной позиции"""
    queryset = Category.objects.all()
    serializer_class = CategoryRUDSerializer


class SubcategoryListAPIView(generics.ListAPIView):
    """Вывод списка подкатегорий"""
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = Pagination


class SubcategoryCreatedAPIView(generics.CreateAPIView):
    """Создание подкатегории"""
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Удаление, изменение, просмотр одной позиции товара"""
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductListAPIView(generics.ListAPIView):
    """Вывод списка товаров """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
