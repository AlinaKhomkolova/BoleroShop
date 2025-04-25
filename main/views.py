from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Product, Category, Subcategory


class BaseView(ListView):
    model = Category
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Главная'
        return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['subcategory'] = self.object.subcategories
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'main/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Категории товаров'
        return data


class ProductListView(ListView):
    model = Product
    template_name = 'main/product.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.subcategory = get_object_or_404(Subcategory, slug=self.kwargs['slug'])
        return Product.objects.filter(subcategories=self.subcategory)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = self.subcategory
        context['title'] = self.subcategory.name
        return context
