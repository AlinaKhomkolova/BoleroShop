from django.urls import path, include

from cart.apps import CartConfig
from cart.views import CartAddView, CartClearView

app_name = CartConfig.name

urlpatterns = [
    path('api/cart/', include([
        # Получение/добавление/обновление корзины
        # GET - просмотр, POST - добавление
        path('', CartAddView.as_view(), name='cart'),

        # Удаление конкретного товара (отдельный метод DELETE)
        # DELETE для удаления по product_id
        path('<int:product_id>/', CartAddView.as_view(), name='cart-remove-item'),

        # Для отчистки корзины
        path('clear/', CartClearView.as_view(), name='cart-clear'),
    ]))
]
