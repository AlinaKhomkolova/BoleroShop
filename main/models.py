from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=30,
                            unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=30,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    slug = models.SlugField(max_length=100,
                            unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение продукта', blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
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
                       args=[self.slug])

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
