from django.contrib import admin
from django.contrib.auth.models import User
from page_customisations.models import (HomePageCustomisation,
                                        HeaderCustomisation,
                                        ProductsPageCustomisation,
                                        GlobalSiteStyling)
from BasicTemplateMain.admin import superadmin


# Superuser admin models
class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'home_page_styling',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',
       
    )
    
class GlobalSiteStylingAdmin(admin.ModelAdmin):
    list_display = (
        'global_site_styles',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',
       
    )

    
class HeaderCustomisationAdmin(admin.ModelAdmin):
   list_display = (
        'header_styling',
        'do_not_display',
    )
   list_editable = (
        'do_not_display',
       
   )


class ProductsPageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'products_page_styling',
        'do_not_display',
    )
    list_editable = (
            'do_not_display',
        
    )
    
"""
superadmin.register() to register for superuser admin
"""

superadmin.register(GlobalSiteStyling, GlobalSiteStylingAdmin)
superadmin.register(HomePageCustomisation, HomePageCustomisationAdmin)
superadmin.register(HeaderCustomisation, HeaderCustomisationAdmin)
superadmin.register(ProductsPageCustomisation, ProductsPageCustomisationAdmin)
superadmin.register(User)
