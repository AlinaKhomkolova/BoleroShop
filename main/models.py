from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from config.settings import NULLABLE
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=30,
                            unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=30,
                            unique=True)
    image = models.ImageField(upload_to='category/%y/%m/%d', verbose_name='Изображение категории', **NULLABLE)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])


class Subcategory(models.Model):
    name = models.CharField(max_length=30,
                            unique=True, verbose_name='Название подкатегории')
    slug = models.SlugField(max_length=30,
                            unique=True)
    image = models.ImageField(upload_to='category/%y/%m/%d', verbose_name='Изображение подкатегории', **NULLABLE)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=CASCADE,
                                 verbose_name='Категория')

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('main:categories',
    #                    args=[self.subcategories.slug])


class Product(models.Model):
    subcategories = models.ForeignKey(Subcategory, related_name='products', on_delete=CASCADE,
                                      verbose_name='Подкатегория')
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    slug = models.SlugField(max_length=100,
                            unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение продукта', **NULLABLE)
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 70}
    )
    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 80}
    )
    image_large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(800, 600)],
        format='JPEG',
        options={'quality': 90}
    )

    description = models.TextField(verbose_name='Описание продукта', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Доступность товара')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания продукта')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения продукта')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail',
                       args=[self.subcategories.slug])

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


class Basket(models.Model):
    user = models.OneToOneField(User, related_name='baskets', verbose_name='Владелец корзины',
                                on_delete=CASCADE)

    class Meta:
        ordering = ['user']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя {self.user.username}'


class BasketItems(models.Model):
    basket = models.ForeignKey(Basket, related_name='items', verbose_name='Корзина', on_delete=CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество продуктов в корзине', default=1)

    class Meta:
        ordering = ['basket']
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'

    def __str__(self):
        return f'{self.product.name} × {self.quantity}'
