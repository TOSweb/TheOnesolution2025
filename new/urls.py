from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('services/<slug:slug>/', service_category_detail, name='service_category_detail'),
    path('service/<slug:slug>/', service_detail, name='service_detail'),
]