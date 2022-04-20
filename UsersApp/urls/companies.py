from django.urls import re_path
from UsersApp import views

urlpatterns = [
    
    re_path(r'^companies$', views.companyApi),
    re_path(r'^companies/([A-Za-z0-9]+)$', views.companyApi)
    
]