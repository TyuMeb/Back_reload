from rest_framework import serializers

from orders.models import OrderModel
from products.models import (
    CardModel,
    CategoryModel,
    ProductModel,
    QuestionOptionsModel,
    QuestionsProductsModel,
    ResponseModel,
)


class CardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = ["id", "name"]


class CategoryModelSeializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "card", "name"]


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "order",
            "category",
            "product_size",
            "product_price",
            "product_description",
            "product_units",
            "is_ended",
        ]
        read_only_fields = [
            "id",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        new_order = OrderModel.objects.create(user_account=user, state="creating")
        return ProductModel.objects.create(**validated_data, user_account=user, order=new_order)


class QuestionModelSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = QuestionsProductsModel
        exclude = ["category"]

    @staticmethod
    def get_options(obj):
        return QuestionOptionsModel.objects.filter(question=obj).values_list("option", flat=True)


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        exclude = ["id", "user_account"]

    def create(self, validated_data):
        user = self.context["request"].user
        return ResponseModel.objects.create(**validated_data, user_account=user)
