from django.db import models
from django.db.models import CASCADE
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from pytils.translit import slugify

from config.settings import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=30,
                            unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=30,
                            unique=True, **NULLABLE)
    image = models.ImageField(upload_to='category/%Y/%m/%d', verbose_name='Изображение категории', **NULLABLE)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Автоматическая генерация уникального slug из имени"""
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    name = models.CharField(max_length=30,
                            unique=True, verbose_name='Название подкатегории')
    slug = models.SlugField(max_length=30,
                            unique=True, **NULLABLE)
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

    def save(self, *args, **kwargs):
        """Автоматическая генерация уникального slug из имени"""
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=CASCADE,
                                    verbose_name='Подкатегория')
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    slug = models.SlugField(max_length=100,
                            unique=True, **NULLABLE)
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

    @property
    def sell_price(self):
        """Расчет цены с учетом скидки"""
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def save(self, *args, **kwargs):
        """Автоматическая генерация уникального slug из имени"""
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
