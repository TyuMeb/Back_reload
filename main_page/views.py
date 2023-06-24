import requests

from django.shortcuts import render
from django.http.response import JsonResponse
from djoser.views import UserViewSet
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers import UserFedbackSerializer
from .models import UserFeedback


class FeedbackViewSet(viewsets.ModelViewSet):
    '''
    Сохранение обращения клиента на главной странице
    '''
    queryset = UserFeedback.objects.all()
    serializer_class = UserFedbackSerializer
    http_method_names = ['get', 'post', 'delete']


class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response({'активация': 'активация аккаунта прошла успешно'})


def reset_password(request, uid, token):

    if request.method == 'POST':
        # проверки на стороне фронта на корректность пароля - не пустое поле и тд
        new_pass = request.POST['new_pass']
        uid_new = request.POST['uid_data']
        token_new = request.POST['token_data']

        # надо поменять url когда на сервере будет
        url = "http://127.0.0.1:8000/auth/users/reset_password_confirm/"
        data = {'uid': uid_new, 'token': token_new, 'new_password': new_pass}
        headers = {'Accept': 'application/json'}

        # отправляем POST запрос и меняем пароль
        requests.post(url, headers=headers, data=data)

        return JsonResponse({'обновление пароля': '22 прошло успешно'})

    return render(request, 'main_page/reset_password.html', {'uid': uid, 'token_uid': token})