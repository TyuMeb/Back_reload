from django.contrib import admin

from .models import CardModel, CategoryModel, ProductModel, KitModel, ProductImageModel


@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_account', 'product_description', 'product_price']

@admin.register(KitModel)
class KitModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_account', 'kit_name']

@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id']
