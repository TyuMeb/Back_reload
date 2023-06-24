import datetime

from rest_framework import serializers
from .models import OrderModel, OrderImageModel, OrderOffer
from main_page.models import SellerData
from rest_framework.response import Response


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'user_account', 'card_id', 'order_description', 'order_time', 'state']
        read_only_fields = ['id', ]

    def create(self, validated_data):
        user = self.context['request'].user
        obj = OrderModel.objects.create(**validated_data, user_account=user)
        return obj


class OrderImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderImageModel
        fields = ('id', 'order_id', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6')

    def create(self, validated_data):
        obj = OrderImageModel.objects.create(**validated_data)
        return obj


class OrderOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOffer
        fields = ['id', 'user_account', 'order_id', 'offer_price', 'offer_execution_time', 'offer_description']

    def create(self, validated_data):
        user = self.context['request'].user
        try:
            seller_data = SellerData.objects.get(user_account_id=user)
        except:
            raise serializers.ValidationError("Вы не являетесь продавцом")
        '''проверяем если продавец активен, не заблокирован'''
        if not seller_data.seller_activity:
            raise serializers.ValidationError("Вы не можете сделать оффер")
        '''ставим заглушку на цену, тк ее можно указать только через 24 часа после офера'''
        validated_data['offer_price'] = ' '
        obj = OrderOffer.objects.create(**validated_data, user_account=user)
        return obj

    def update(self, instance, validated_data):
        check_time = datetime.datetime.now()
        time_offer = instance.offer_create_at
        '''проверяем прошло ли больше 24 часов с момента оффера для обновления цены'''
        check_total = check_time.day*24*60 + check_time.hour*60 + check_time.minute
        time_offer_total = time_offer.day*24*60 + time_offer.hour*60 + time_offer.minute

        result = check_total - time_offer_total
        print(result)

        ''' временно проверяем если прошло 5 минут'''
        if result < 5:
            raise serializers.ValidationError("Вы не можете установить цену, должно пройти 24 часа")

        return super().update(instance, validated_data)

