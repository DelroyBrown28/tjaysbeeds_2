from django.contrib import admin
from BasicTemplateMain.admin import superadmin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )
    search_fields = [
        'name',
        'sku',
        'price',
    ]
    list_filter = (
        'name',
        'category',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    list_display_links = ('name',)
    list_editable = (
        'friendly_name',
    )
    
        

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
