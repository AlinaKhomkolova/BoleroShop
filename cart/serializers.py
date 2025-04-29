from rest_framework import serializers


class CartItemSerializer(serializers.Serializer):
    """Валидация данных для операций с корзиной"""
    # ID товара
    product_id = serializers.IntegerField()
    # Количество товара
    quantity = serializers.IntegerField(min_value=1)
    # True — заменить текущее количество, False — добавить к текущему (опционально)
    update_quantity = serializers.BooleanField(required=False)
