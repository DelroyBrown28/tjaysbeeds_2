from django.contrib.admin import AdminSite
from django.contrib.auth.decorators import login_required



class SuperAdminSite(AdminSite):
    site_header = 'SuperUser Admin'

superadmin = SuperAdminSite(name='superadmin')

