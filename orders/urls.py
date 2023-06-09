from django.urls import path

from .views import OrderImageViewSet, OrderOfferViewSet


urlpatterns = [
    path(
        "products/image", OrderImageViewSet.as_view({"get": "list", "post": "create"})
    ),
    path("offer/", OrderOfferViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "offer/<int:pk>",
        OrderOfferViewSet.as_view(
            {"get": "retrieve", "delete": "destroy", "put": "update"}
        ),
    ),
]
