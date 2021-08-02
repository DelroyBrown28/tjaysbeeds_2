from django.shortcuts import render
from .models import (HomePageCustomisation,
                     HeaderCustomisation,
                     ProductsPageCustomisation,
                     GlobalSiteStyling)


def header_customisation(request):
    """Customisation for header contents"""
    header_customisation = HeaderCustomisation.objects.all()
    context = {
        'header_customisation' : header_customisation,
    }
    return render(request, 'includes/header.html', context)


def products_page_customisation(request):
    """Customisation for products page"""
    products_page_customisation = ProductsPageCustomisation.objects.all()
    context = {
        'products_page_customisation' : products_page_customisation,
    }
    return render(request, 'products/products.html', context)


def global_site_styles(request):
    """Customisation for all pages"""
    global_site_styles = GlobalSiteStyling.objects.all()
    context = {
        'global_site_styles' : global_site_styles,
    }
    return render(request, 'products/products.html', context)


