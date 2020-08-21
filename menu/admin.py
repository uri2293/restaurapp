from django.contrib import admin
from django.contrib.admin.decorators import register
from menu.models import Plate, PlateType


@register(Plate)
class PlateAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(PlateAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__user=request.user)


@register(PlateType)
class PlateTypeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(PlateTypeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__user=request.user)
