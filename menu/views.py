from django.views.generic import ListView
from menu.models import Plate


class MenuView(ListView):
    template_name = "menu.html"
    model = Plate

    def get_queryset(self):
        restaurant = self.kwargs['restaurant']
        queryset = Plate.objects.filter(restaurant__name=restaurant)
        return queryset
