from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
]
