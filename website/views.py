from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q
from django.conf import settings
import json
import re
from .models import Service, BlogPost, Portfolio, Testimonial, BlogCategory, BlogTag, PortfolioCategory, Contact
import random

def index(request):
    """Homepage view with featured content"""
    featured_services = Service.objects.filter(is_featured=True, is_active=True).order_by('order')[:6]
    
    # Get latest 3 portfolio items
    latest_portfolios = Portfolio.objects.all().order_by('-id')[:3]
    
    # Get latest 3 blog posts
    latest_posts = BlogPost.objects.filter(status='published').order_by('-published_date')[:3]
    
    context = {
        'featured_services': featured_services,
        'latest_portfolios': latest_portfolios,
        'latest_posts': latest_posts,
    }
    return render(request, 'index.html', context)

class ServiceListView(ListView):
    """View for listing all services"""
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'
    ordering = ['order', 'title']
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True)

def service_list(request):
    """Function-based view for listing all services"""
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    
    context = {
        'services': services,
    }
    
    return render(request, 'service_list.html', context)

def service_detail(request, slug):
    """View for individual service detail page"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    
    # Get related services from the model's related_services field
    related_services = service.related_services.filter(is_active=True)[:3]
    
    # If no related services are set, get some fallback services
    if not related_services:
        related_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:3]
    
    # Get related case studies/portfolios
    related_case_studies = Portfolio.objects.filter(related_services=service)[:3]
    
    # Get testimonials related to this service
    related_testimonials = Testimonial.objects.filter(related_services=service)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
        'related_case_studies': related_case_studies,
        'related_testimonials': related_testimonials,
    }
    
    return render(request, 'service_detail.html', context)

# class ServiceDetailView(DetailView):
#     """Alternative class-based view for service detail"""
#     model = Service
#     template_name = 'service_detail.html'
#     context_object_name = 'service'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         service = self.get_object()
        
#         # Get related services (excluding current service)
#         context['related_services'] = Service.objects.filter(is_active=True).exclude(id=service.id)[:3]
        
#         # Get related case studies/portfolios
#         context['related_case_studies'] = Portfolio.objects.filter(related_services=service, is_active=True)[:3]
        
#         # Get testimonials related to this service
#         context['related_testimonials'] = Testimonial.objects.filter(related_services=service, is_active=True)[:3]
        
#         return context

def blog_list(request):
    """View for listing all published blog posts"""
    # Get featured posts (up to 5 featured published posts)
    featured_posts = BlogPost.objects.filter(
        status='published', 
        is_featured=True
    ).order_by('-published_date')[:5]
    
    # Get all categories and shuffle them, then take first 5
    all_categories = list(BlogCategory.objects.all().order_by('name'))
    random.shuffle(all_categories)
    categories = all_categories[:5]
    
    # Get 6 posts from each category (including featured posts to avoid empty sections)
    category_posts = {}
    for category in categories:
        posts = BlogPost.objects.filter(
            status='published',
            category=category
        ).order_by('-published_date')[:6]
        
        if posts.exists():  # Only include categories that have posts
            category_posts[category] = posts
    
    # Get all tags for potential filtering
    tags = BlogTag.objects.all().order_by('name')
    
    context = {
        'featured_posts': featured_posts,
        'categories': categories,
        'category_posts': category_posts,
        'tags': tags,
    }
    
    return render(request, 'blog_list.html', context)

def blog_detail(request, slug):
    """View for displaying a single blog post"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.increase_views()
    
    # Get related posts from the same category
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id).order_by('-published_date')[:3]
    
    # Get related posts from other categories
    other_categories_posts = BlogPost.objects.filter(
        status='published'
    ).exclude(
        category=post.category
    ).exclude(id=post.id).order_by('-published_date')[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'other_categories_posts': other_categories_posts,
    }
    
    return render(request, 'blog_detail.html', context)

def category_detail(request, slug):
    """View for displaying all posts from a specific category with pagination"""
    category = get_object_or_404(BlogCategory, slug=slug)
    
    # Get all published posts from this category
    posts_list = BlogPost.objects.filter(
        category=category,
        status='published'
    ).order_by('-published_date')
    
    # Pagination - 10 posts per page
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    # Get other categories for navigation
    other_categories = BlogCategory.objects.exclude(id=category.id).order_by('name')[:5]
    
    context = {
        'category': category,
        'posts': posts,
        'other_categories': other_categories,
        'paginator': paginator,
    }
    
    return render(request, 'category_detail.html', context)

def portfolio_list(request):
    """View for listing all portfolio items"""
    portfolios = Portfolio.objects.all().order_by('-id')
    categories = PortfolioCategory.objects.all().order_by('name')
    
    context = {
        'portfolios': portfolios,
        'categories': categories,
    }
    
    return render(request, 'portfolio.html', context)

def portfolio_detail(request, slug):
    """View for displaying a single portfolio item"""
    portfolio = get_object_or_404(Portfolio, slug=slug)
    
    # Get related portfolios from the same category
    related_portfolios = Portfolio.objects.filter(
        category=portfolio.category
    ).exclude(id=portfolio.id).order_by('-id')[:3]
    
    # Get related portfolios from other categories
    other_categories_portfolios = Portfolio.objects.exclude(
        category=portfolio.category
    ).exclude(id=portfolio.id).order_by('-id')[:3]
    
    context = {
        'portfolio': portfolio,
        'related_portfolios': related_portfolios,
        'other_categories_portfolios': other_categories_portfolios,
    }
    
    return render(request, 'portfolio_detail.html', context)

def about(request):
    """View for the about page"""
    return render(request, 'about.html')

# Security and spam prevention functions
def is_spam_submission(request, data):
    """Check if submission is likely spam"""
    # Check for rapid submissions (same IP within 1 hour)
    ip_address = get_client_ip(request)
    recent_submissions = Contact.objects.filter(
        ip_address=ip_address,
        created_at__gte=timezone.now() - timezone.timedelta(hours=1)
    ).count()
    
    if recent_submissions >= 3:
        return True, "Too many submissions from this IP address"
    
    # Check for suspicious content patterns
    message = data.get('message', '').lower()
    name = data.get('name', '').lower()
    
    # Common spam patterns
    spam_patterns = [
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'\b(viagra|cialis|casino|poker|loan|credit|debt|weight loss|diet)\b',
        r'[A-Z]{5,}',  # Too many consecutive capitals
        r'\b(free|money|cash|earn|income|profit|rich|wealth)\b',
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message) or re.search(pattern, name):
            return True, "Suspicious content detected"
    
    # Check for very short messages (likely spam)
    if len(message.strip()) < 10:
        return True, "Message too short"
    
    # Check for very long messages (potential spam)
    if len(message.strip()) > 2000:
        return True, "Message too long"
    
    return False, None

def get_client_ip(request):
    """Get client IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_protect
@require_http_methods(["POST"])
def contact_form_submit(request):
    """Secure contact form submission endpoint"""
    if request.method == 'POST':
        try:
            # Get form data
            data = {
                'name': request.POST.get('name', '').strip(),
                'email': request.POST.get('email', '').strip(),
                'phone': request.POST.get('phone', '').strip(),
                'company': request.POST.get('company', '').strip(),
                'service_interest': request.POST.get('service_interest', '').strip(),
                'message': request.POST.get('message', '').strip(),
            }
            
            # Basic validation
            if not all([data['name'], data['email'], data['message']]):
                return JsonResponse({
                    'success': False,
                    'message': 'Please fill in all required fields.'
                }, status=400)
            
            # Email validation
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
                return JsonResponse({
                    'success': False,
                    'message': 'Please enter a valid email address.'
                }, status=400)
            
            # Check for spam
            is_spam, spam_reason = is_spam_submission(request, data)
            if is_spam:
                return JsonResponse({
                    'success': False,
                    'message': 'Submission blocked for security reasons.'
                }, status=429)
            
            # Create contact submission
            contact = Contact.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                company=data['company'],
                service_interest=data['service_interest'],
                message=data['message'],
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                referrer=request.META.get('HTTP_REFERER', ''),
                status='new' if not is_spam else 'spam',
                is_spam=is_spam
            )
            
            # Log successful submission
            print(f"Contact form submitted by {data['name']} ({data['email']}) from IP {get_client_ip(request)}")
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! We will get back to you soon.',
                'submission_id': contact.id
            })
            
        except Exception as e:
            # Log error for debugging
            print(f"Contact form error: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'An error occurred. Please try again later.'
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    }, status=405)

def contact_page(request):
    """Contact page view"""
    # Get services for the service interest dropdown
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    
    context = {
        'services': services,
    }
    return render(request, 'contact.html', context)
