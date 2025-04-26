from django.contrib import admin

from .models import Category, Product, Subcategory, Basket, BasketItems


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
    list_display = ['name', 'slug', 'price',
                    'created', 'updated', 'discount', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Basket)
class AdminBasket(admin.ModelAdmin):
    list_display = ['id','user']
    list_filter = ['user']


@admin.register(BasketItems)
class AdminBasketItems(admin.ModelAdmin):
    list_display = ['basket', 'product', 'quantity']
    list_filter = ['basket']
