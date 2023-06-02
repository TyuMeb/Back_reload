from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='chat_index'),
    path('<str:room_name>/', views.room_view, name='chat_room'),
    # path('add', views.add, name='add'),
    # path('delete/<int:id>', views.delete, name='delete'),
]
