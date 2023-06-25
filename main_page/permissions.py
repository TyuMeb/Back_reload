from rest_framework import permissions

from main_page.models import SellerData


class IsSeller(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin or SellerData.objects.get(id=request.user.id)
