from django.shortcuts import render
from django.views.generic import TemplateView

from dishes.models import Soup


class SoupsView(TemplateView):

    template_name = "dishes/dishes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["soups"] = Soup.objects.all()[:5]
        return context
