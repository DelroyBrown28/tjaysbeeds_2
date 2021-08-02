from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from page_customisations.models import HomePageCustomisation


def index(request):
    """Returns the home page."""
    home_page_customisation = HomePageCustomisation.objects.all()
    context = {
        'home_page_customisation' : home_page_customisation,
    }
    return render(request, 'home/index.html', context)


