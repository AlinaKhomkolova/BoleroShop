from rest_framework import serializers

from main.models import Category, Product, Subcategory


class CategoryRUDSerializer(serializers.ModelSerializer):
    """Сериализатор для удаления изменения и просмотра одной позиции"""

    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    """Просмотр всех категорий"""

    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreatedSerializer(serializers.ModelSerializer):
    """Создание категории"""

    class Meta:
        model = Category
        fields = ['name', 'image']

    def create(self, validated_data):
        category = Category.objects.create(
            name=validated_data['name'],
            image=validated_data['image']
        )
        return category


class SubcategorySerializer(serializers.ModelSerializer):
    """Просмотр всех подкатегорий"""

    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Просмотр всех продуктов"""
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
