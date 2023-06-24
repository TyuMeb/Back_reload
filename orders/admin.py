from django.contrib import admin
from .models import OrderModel, OrderImageModel, OrderOffer
from products.models import ProductModel

class ProductModelInline(admin.TabularInline):
    model = ProductModel
    extra = 3

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['order_time', 'id', 'state', 'user_account']
    inlines = [ProductModelInline, ]

@admin.register(OrderImageModel)
class OrderImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id']


@admin.register(OrderOffer)
class OrderOfferAdmin(admin.ModelAdmin):
    list_display = ['offer_create_at', 'id', 'order_id']