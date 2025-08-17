from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    # path('services/', views.service_list, name='service_list'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
]
