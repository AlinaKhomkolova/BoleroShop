from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from cart.serializers import CartItemSerializer
from main.models import Product


class CartAddView(APIView):
    """Вью для управления товарами в корзине"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Добавление/обновление товара в корзине"""

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            update_quantity = serializer.validated_data.get('update_quantity', False)

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "Товар не найден"}, status=status.HTTP_404_NOT_FOUND)

            cart = Cart(request)
            cart.add(product, quantity, update_quantity=update_quantity)  # Обновление количества

            # Возвращаем обновленные данные корзины для удобства
            return Response({"success": "Товар добавлен/обновлен"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        """Удаление товара из корзины по product_id"""
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Товар не найден"}, status=status.HTTP_404_NOT_FOUND)

        cart = Cart(request)
        cart.remove(product) # Удаляем товар из корзины

        return Response({"success": "Товар удален"}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request):
        """Просмотр товаров в корзине"""
        cart = Cart(request)
        cart_data = [
            {
                'product_id': item['product'].id,
                'name': item['product'].name,
                'quantity': item['quantity'],
                'price': item['price'],
                'total_price': item['total_price']
            }
            for item in cart
        ]
        total = cart.get_total_price()

        return Response({
            'items': cart_data,
            'total_price': total
        }, status=status.HTTP_200_OK)


class CartClearView(APIView):
    """Очистка корзины"""
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """Полная очистка корзины"""
        cart = Cart(request)
        cart.clear()
        return Response({"success": "Корзина очищена"}, status=status.HTTP_204_NO_CONTENT)
