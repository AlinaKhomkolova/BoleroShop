from django.urls import path

from cart.apps import CartConfig
from cart.views import CartAddView, CartClearView

app_name = CartConfig.name

urlpatterns = [
    # Для добавления/обновления
    path('api/cart/', CartAddView.as_view(), name='cart'),
    # Для удаления товара
    path('api/cart/<int:product_id>/', CartAddView.as_view(), name='cart-remove'),
    # Для отчистки корзины
    path('api/clear/', CartClearView.as_view(), name='cart-clear'),
]
