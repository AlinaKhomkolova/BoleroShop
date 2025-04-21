from django.views.generic import ListView, DetailView

from main.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    context_object_name = 'products'
    queryset = Product.objects.all()
    list_filter = ('available',)
    template_name = 'main/index/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Главная'
        return data

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product/detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Описание'
        return data
