from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home, name='home'),
    
    path('about/', about, name='about'),
    path('services/<slug:slug>/', service_category_detail, name='service_category_detail'),
    path('service/<slug:slug>/', service_detail, name='service_detail'),
    path('service-variant/<slug:slug>/', service_variant_detail, name='service_variant_detail'),
]