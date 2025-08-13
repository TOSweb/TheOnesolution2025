from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Service, BlogPost, Portfolio, TeamMember, Testimonial, BlogCategory, PortfolioCategory

def index(request):
    """Homepage view with featured content"""
    # Get featured services for the homepage
    featured_services = Service.objects.filter(is_featured=True, is_active=True).order_by('order')[:6]
    
    # If not enough featured services, get all active services
    if featured_services.count() < 6:
        remaining_services = Service.objects.filter(is_active=True).exclude(id__in=[s.id for s in featured_services]).order_by('order')
        featured_services = list(featured_services) + list(remaining_services[:6 - featured_services.count()])
    
    # Get featured portfolio items
    featured_portfolios = Portfolio.objects.filter(is_featured=True).order_by('order')[:6]
    
    # Get featured blog posts
    featured_blog_posts = BlogPost.objects.filter(status='published', is_featured=True).order_by('-published_date')[:6]
    
    # Get featured testimonials
    featured_testimonials = Testimonial.objects.filter(is_featured=True).order_by('order')[:3]
    
    # Get team members
    team_members = TeamMember.objects.filter(is_active=True).order_by('order')[:3]
    
    context = {
        'featured_services': featured_services,
        'featured_portfolios': featured_portfolios,
        'featured_blog_posts': featured_blog_posts,
        'featured_testimonials': featured_testimonials,
        'team_members': team_members,
    }
    
    return render(request, 'index.html', context)

class ServiceListView(ListView):
    """View for listing all services"""
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'
    paginate_by = 12
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('order', 'title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_services'] = Service.objects.filter(is_featured=True, is_active=True).order_by('order')[:3]
        return context

class ServiceDetailView(DetailView):
    """View for individual service details"""
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related services
        service = self.get_object()
        related_services = Service.objects.filter(is_active=True).exclude(id=service.id).order_by('order')[:3]
        
        # Get case studies for this service
        case_studies = service.case_studies.all()[:3]
        
        # Get testimonials for this service
        testimonials = service.testimonials.all()[:3]
        
        context.update({
            'related_services': related_services,
            'case_studies': case_studies,
            'testimonials': testimonials,
        })
        return context

def service_detail(request, slug):
    """Alternative function-based view for service details"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    
    # Get related services
    related_services = Service.objects.filter(is_active=True).exclude(id=service.id).order_by('order')[:3]
    
    # Get case studies for this service
    case_studies = service.case_studies.all()[:3]
    
    # Get testimonials for this service
    testimonials = service.testimonials.all()[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
        'case_studies': case_studies,
        'testimonials': testimonials,
    }
    
    return render(request, 'service_detail.html', context)
