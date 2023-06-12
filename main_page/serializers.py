from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CooperationOffer, UserAccount
from rest_framework.response import Response

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'person_telephone', 'surname')

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'name', 'person_telephone', 'surname')


class CooperationOfferSerializer(serializers.ModelSerializer):
    user_account_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CooperationOffer
        fields = '__all__'

