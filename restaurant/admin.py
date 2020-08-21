from django.contrib import admin
from django.contrib.admin.decorators import register
from restaurant.models import Information


@register(Information)
class InformationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(InformationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
