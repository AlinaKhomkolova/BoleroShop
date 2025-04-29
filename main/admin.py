from django.contrib import admin

from .models import Category, Product, Subcategory


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class AdminSubcategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'discount', 'sell_price',
                    'created', 'updated', 'available']
    list_filter = ['available', 'created', 'updated']
    search_fields = ['name', 'slug']  # Поиск по названию и слагу
    ordering = ['-created']  # Сортировка по дате создания
    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}
