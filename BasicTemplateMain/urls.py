import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .admin import superadmin


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # Main Admin URL
    path('admin/', admin.site.urls),
    path('superadmin/', superadmin.urls),
    # Website URLs
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),  
    path('products/', include('products.urls')),  
    path('bag/', include('bag.urls')),  
    path('checkout/', include('checkout.urls')),  
    path('profile/', include('profiles.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
