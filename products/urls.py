from django.urls import include, path
from .views import CardModelAPIView, CategoryModelListAPIView, CategoryModelListAPIView, ProductModelCreateAPIView, \
    ProductModelAPIView


urlpatterns = [
    path('products/all_CardModel/', CardModelAPIView.as_view()),
    path('products/card_categories/<int:card_id>', CategoryModelListAPIView.as_view()),
    path('products/product', ProductModelCreateAPIView.as_view()),

    path('products/<int:pk>', ProductModelAPIView.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update'})),
    path('products/', ProductModelAPIView.as_view({
        'get': 'list',
        'post': 'create'})),

    # path('products/image', ProductImageViewSet.as_view()),
]
