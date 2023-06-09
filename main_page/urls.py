from django.urls import include, path
from rest_framework import routers

from .views import ActivateUser, CooperationViewSet, reset_password


router = routers.SimpleRouter()

router.register(r"cooperation", CooperationViewSet)

urlpatterns = [
    path("users/", include(router.urls)),
    path(
        "activate/<uid>/<token>",
        ActivateUser.as_view({"get": "activation"}),
        name="activation",
    ),
    path(
        "password/reset/confirm/<str:uid>/<str:token>",
        reset_password,
        name="reset_password",
    ),
]
