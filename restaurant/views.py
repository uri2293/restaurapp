from django.views.generic import ListView
from restaurant.models import Information


class IndexView(ListView):
    template_name = "index.html"
    model = Information
