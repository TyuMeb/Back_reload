from rest_framework import serializers
from products.models import CategoryModel, ProductModel
from rest_framework.response import Response

class CardModelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    card_name = serializers.CharField()


class CategoryModelSeializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name']


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['id', 'category', 'product_size', 'product_price', 'product_description', 'product_units', 'is_ended']
        read_only_fields = ['id', ]

    def create(self, validated_data):
        user = self.context['request'].user
        obj = ProductModel.objects.create(**validated_data, user_account=user)
        return obj
