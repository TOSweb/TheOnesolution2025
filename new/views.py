from django.shortcuts import render, get_object_or_404
from .models import Home, AlternateHome, About, ServiceCategory, Service, ServiceVariant, ServiceContent, ServiceCategoryContent, ServiceVariantContent

# Create your views here.
def home(request):
    home = Home.objects.first()
    alternate_home = AlternateHome.objects.filter(home=home)
    # Get services to display on homepage (limit to 3 for grid layout)
    # Only query the fields we actually use in the template
    services = ServiceCategory.objects.only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug'
    )[:3]
    return render(request, 'index.html', {
        'home': home, 
        'alternate_home': alternate_home,
        'services': services
    })

def service_category_detail(request, slug):
    # Get the service category with optimized query
    service_category = get_object_or_404(
        ServiceCategory.objects.only(
            'heading', 'small_description', 'content', 'image_m', 'image_t', 'image_d', 'alt',
            'title', 'meta_description', 'meta_keywords', 'og_title', 
            'og_description', 'og_image', 'slug'
        ), 
        slug=slug
    )
    
    # Get services belonging to this category (ordered by order field)
    services = Service.objects.filter(
        service_category=service_category
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug', 'order'
    ).order_by('order', 'heading')
    
    # Get service variants belonging to services in this category (ordered by order field)
    service_variants = ServiceVariant.objects.filter(
        service_category__service_category=service_category
    ).select_related('service_category').only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug', 'order',
        'service_category__heading', 'service_category__slug'
    ).order_by('order', 'heading')
    
    # Get service category content (additional content blocks)
    service_category_contents = ServiceCategoryContent.objects.filter(
        service_category=service_category
    ).only(
        'image_m', 'image_t', 'image_d', 'content', 'youtube_video_embed'
    )
    
    # Get related service categories (excluding current one)
    related_categories = ServiceCategory.objects.exclude(
        id=service_category.id
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug'
    )[:3]
    
    context = {
        'service_category': service_category,
        'services': services,
        'service_variants': service_variants,
        'service_category_contents': service_category_contents,
        'related_categories': related_categories,
    }
    
    return render(request, 'service_category_detail.html', context)

def service_detail(request, slug):
    # Get the service with optimized query
    service = get_object_or_404(
        Service.objects.select_related('service_category').only(
            'heading', 'small_description', 'content', 'image_m', 'image_t', 'image_d', 'alt',
            'title', 'meta_description', 'meta_keywords', 'og_title', 
            'og_description', 'og_image', 'slug', 'schema',
            'service_category__heading', 'service_category__slug'
        ), 
        slug=slug
    )
    
    # Get service content (additional content blocks)
    service_contents = ServiceContent.objects.filter(
        service=service
    ).only(
        'image_m', 'image_t', 'image_d', 'content', 'youtube_video_embed'
    )
    
    # Get service variants related to this service (if ServiceVariant has FK to Service)
    service_variants = ServiceVariant.objects.filter(
        service_category=service
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug', 'order'
    ).order_by('order', 'heading')
    
    # Get related services from the same category (excluding current service)
    related_services = Service.objects.filter(
        service_category=service.service_category
    ).exclude(
        id=service.id
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug'
    ).order_by('order', 'heading')[:3]
    
    # Get other services from different categories
    other_services = Service.objects.exclude(
        service_category=service.service_category
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug',
        'service_category__heading'
    ).select_related('service_category')[:3]
    
    context = {
        'service': service,
        'service_contents': service_contents,
        'service_variants': service_variants,
        'related_services': related_services,
        'other_services': other_services,
    }
    
    return render(request, 'service_detail.html', context)

def service_variant_detail(request, slug):
    # Get the service variant with optimized query
    service_variant = get_object_or_404(
        ServiceVariant.objects.select_related('service_category__service_category').only(
            'heading', 'small_description', 'content', 'image_m', 'image_t', 'image_d', 'alt',
            'title', 'meta_description', 'meta_keywords', 'og_title', 
            'og_description', 'og_image', 'slug', 'schema', 'canonical_url',
            'service_category__heading', 'service_category__slug',
            'service_category__service_category__heading', 'service_category__service_category__slug'
        ), 
        slug=slug
    )
    
    # Get service variant content (additional content blocks)
    service_variant_contents = ServiceVariantContent.objects.filter(
        service_variant=service_variant
    ).only(
        'image_m', 'image_t', 'image_d', 'content', 'youtube_video_embed'
    )
    
    # Get related service variants from the same service (excluding current variant)
    related_variants = ServiceVariant.objects.filter(
        service_category=service_variant.service_category
    ).exclude(
        id=service_variant.id
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug'
    ).order_by('order', 'heading')[:3]
    
    # Get other service variants from different services
    other_variants = ServiceVariant.objects.exclude(
        service_category=service_variant.service_category
    ).only(
        'heading', 'small_description', 'image_m', 'image_t', 'image_d', 'alt', 'slug',
        'service_category__heading'
    ).select_related('service_category')[:3]
    
    context = {
        'service_variant': service_variant,
        'service_variant_contents': service_variant_contents,
        'related_variants': related_variants,
        'other_variants': other_variants,
    }
    
    return render(request, 'service_variant_detail.html', context)

def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})