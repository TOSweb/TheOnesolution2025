from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service, BlogPost, Portfolio, BlogCategory

class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 1.0
    changefreq = 'monthly'
    
    def items(self):
        return ['index', 'service_list', 'blog_list', 'portfolio', 'about', 'contact']
    
    def location(self, item):
        return reverse(item)

class ServiceSitemap(Sitemap):
    """Sitemap for services"""
    changefreq = 'monthly'
    priority = 0.8
    
    def items(self):
        return Service.objects.filter(is_active=True)
    
    def lastmod(self, obj):
        return obj.updated_at

class BlogPostSitemap(Sitemap):
    """Sitemap for blog posts"""
    changefreq = 'weekly'
    priority = 0.7
    
    def items(self):
        return BlogPost.objects.filter(status='published')
    
    def lastmod(self, obj):
        return obj.updated_at

class BlogCategorySitemap(Sitemap):
    """Sitemap for blog categories"""
    changefreq = 'monthly'
    priority = 0.6
    
    def items(self):
        return BlogCategory.objects.all()
    
    def location(self, obj):
        return reverse('category_detail', kwargs={'slug': obj.slug})
    
    def lastmod(self, obj):
        return obj.updated_at

class PortfolioSitemap(Sitemap):
    """Sitemap for portfolio items"""
    changefreq = 'monthly'
    priority = 0.8
    
    def items(self):
        return Portfolio.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at 