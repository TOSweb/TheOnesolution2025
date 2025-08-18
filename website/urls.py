from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import (
    StaticViewSitemap, ServiceSitemap, BlogPostSitemap, 
    BlogCategorySitemap, PortfolioSitemap
)

# Complete sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
    'blog_posts': BlogPostSitemap,
    'blog_categories': BlogCategorySitemap,
    'portfolio': PortfolioSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.service_list, name='service_list'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('contact/submit/', views.contact_form_submit, name='contact_submit'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
