from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserFeedback
from rest_framework.response import Response

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'person_telephone', 'surname')


class UserFedbackSerializer(serializers.ModelSerializer):
    user_account_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFeedback
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname',)