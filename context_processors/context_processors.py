from page_customisations.models import ProductsPageCustomisation
from page_customisations.views import (HeaderCustomisation,
                                       ProductsPageCustomisation,
                                       GlobalSiteStyling)


def global_styles_processor(request):
    return {
       'global_styles': GlobalSiteStyling.objects.all(),

    }
    
def header_customisation_processor(request):
    return {
       'header_customisation': HeaderCustomisation.objects.all(),

    }
    
def products_page_customisation_processor(request):
    return {
       'products_page_customisation': ProductsPageCustomisation.objects.all(),
    }
    
