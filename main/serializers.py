from rest_framework import serializers

from main.models import Category, Product, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # Категория продукта
    category = serializers.CharField(
        source='subcategory.category.name',
        read_only=True
    )
    # Подкатегория продукта
    subcategory = SubcategorySerializer(read_only=True)

    # Цена со скидкой
    sell_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )
    # Список уров трех картинок
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'discount',
            'sell_price',
            'images',
        ]

    def get_images(self, obj):
        return {
            'small': obj.image_small.url if obj.image_small else None,
            'medium': obj.image_medium.url if obj.image_medium else None,
            'large': obj.image_large.url if obj.image_large else None,
        }
