from rest_framework import serializers
from products.models import CategoryModel, ProductModel, CardModel
from rest_framework.response import Response
from orders.models import OrderModel


class CardModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardModel
        fields = ['id', 'name']


class CategoryModelSeializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'card', 'name']


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'order', 'category', 'product_size', 'product_price', 'product_description', 'product_units',
                  'is_ended']
        read_only_fields = ['id', ]

    def create(self, validated_data):
        user = self.context['request'].user
        new_order = OrderModel.objects.create(user_account=user, state='creating')
        obj = ProductModel.objects.create(**validated_data, user_account=user, order=new_order)
        return obj


