from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils import timezone

class Service(models.Model):
    """Model for services offered by the company"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField(max_length=300)
    full_description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Icon class or SVG path")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    features = models.TextField(blank=True, help_text="List of service features (one per line)")
    process_steps = models.TextField(blank=True, help_text="List of process steps (one per line)")
    benefits = models.TextField(blank=True, help_text="List of benefits (one per line)")
    pricing = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    # Advanced SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="Custom SEO title (defaults to service title)")
    meta_description = models.TextField(max_length=160, blank=True, help_text="Custom SEO description (defaults to short description)")
    meta_keywords = models.CharField(max_length=200, blank=True, help_text="SEO keywords separated by commas")
    canonical_url = models.URLField(blank=True, help_text="Canonical URL if different from service URL")
    
    # Schema markup and structured data
    schema_markup = models.JSONField(default=dict, help_text="Custom JSON-LD schema markup")
    
    # Comprehensive Social Media Optimization
    # Open Graph (Facebook, WhatsApp, LinkedIn, etc.)
    og_title = models.CharField(max_length=100, blank=True, help_text="Open Graph title for social sharing")
    og_description = models.TextField(max_length=200, blank=True, help_text="Open Graph description for social sharing")
    og_image = models.ImageField(upload_to='services/og/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_type = models.CharField(max_length=50, default='website', choices=[
        ('website', 'Website'),
        ('article', 'Article'),
        ('product', 'Product'),
        ('service', 'Service'),
        ('business.business', 'Business'),
        ('place', 'Place'),
        ('profile', 'Profile'),
    ])
    og_site_name = models.CharField(max_length=100, blank=True, help_text="Site name for Open Graph")
    og_locale = models.CharField(max_length=10, default='en_US', help_text="Locale for Open Graph")
    og_url = models.URLField(blank=True, help_text="Canonical URL for Open Graph")
    
    # Twitter Card
    twitter_card = models.CharField(max_length=20, default='summary_large_image', choices=[
        ('summary', 'Summary'),
        ('summary_large_image', 'Summary Large Image'),
        ('app', 'App'),
        ('player', 'Player'),
    ])
    twitter_title = models.CharField(max_length=100, blank=True, help_text="Twitter title (defaults to og_title)")
    twitter_description = models.TextField(max_length=200, blank=True, help_text="Twitter description (defaults to og_description)")
    twitter_image = models.ImageField(upload_to='services/twitter/', blank=True, null=True, help_text="Twitter image (defaults to og_image)")
    twitter_creator = models.CharField(max_length=100, blank=True, help_text="Twitter creator handle (@username)")
    twitter_site = models.CharField(max_length=100, blank=True, help_text="Twitter site handle (@username)")
    
    # LinkedIn
    linkedin_title = models.CharField(max_length=100, blank=True, help_text="LinkedIn title (defaults to og_title)")
    linkedin_description = models.TextField(max_length=200, blank=True, help_text="LinkedIn description (defaults to og_description)")
    linkedin_image = models.ImageField(upload_to='services/linkedin/', blank=True, null=True, help_text="LinkedIn image (defaults to og_image)")
    
    # WhatsApp
    whatsapp_title = models.CharField(max_length=100, blank=True, help_text="WhatsApp title (defaults to og_title)")
    whatsapp_description = models.TextField(max_length=200, blank=True, help_text="WhatsApp description (defaults to og_description)")
    whatsapp_image = models.ImageField(upload_to='services/whatsapp/', blank=True, null=True, help_text="WhatsApp image (defaults to og_image)")
    
    # Pinterest
    pinterest_title = models.CharField(max_length=100, blank=True, help_text="Pinterest title (defaults to og_title)")
    pinterest_description = models.TextField(max_length=200, blank=True, help_text="Pinterest description (defaults to og_description)")
    pinterest_image = models.ImageField(upload_to='services/pinterest/', blank=True, null=True, help_text="Pinterest image (defaults to og_image)")
    
    # Instagram
    instagram_title = models.CharField(max_length=100, blank=True, help_text="Instagram title (defaults to og_title)")
    instagram_description = models.TextField(max_length=200, blank=True, help_text="Instagram description (defaults to og_description)")
    instagram_image = models.ImageField(upload_to='services/instagram/', blank=True, null=True, help_text="Instagram image (defaults to og_image)")
    
    # Service-specific SEO
    service_area = models.CharField(max_length=200, blank=True, help_text="Geographic area served")
    service_industry = models.CharField(max_length=200, blank=True, help_text="Target industries")
    service_duration = models.CharField(max_length=100, blank=True, help_text="Typical project duration")
    
    # Internal linking and SEO
    related_services = models.ManyToManyField('self', blank=True, symmetrical=False, help_text="Related services")
    
    # Service status
    is_active = models.BooleanField(default=True, help_text="Whether this service is active and visible")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

class BlogCategory(models.Model):
    """Model for blog post categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default="#3B82F6", help_text="Hex color code")
    
    # SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="SEO title for category pages")
    meta_description = models.TextField(max_length=160, blank=True, help_text="SEO description for category pages")
    meta_keywords = models.CharField(max_length=200, blank=True, help_text="SEO keywords for category pages")
    
    # Schema markup
    schema_markup = models.JSONField(default=dict, help_text="JSON-LD schema markup for category pages")
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blog categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogTag(models.Model):
    """Model for blog post tags"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    # SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="SEO title for tag pages")
    meta_description = models.TextField(max_length=160, blank=True, help_text="SEO description for tag pages")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogPost(models.Model):
    """Model for blog posts with advanced SEO support"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    # Basic content fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(max_length=500)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(BlogTag, blank=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    
    # Advanced SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="Custom SEO title (defaults to post title)")
    meta_description = models.TextField(max_length=160, blank=True, help_text="Custom SEO description (defaults to excerpt)")
    meta_keywords = models.CharField(max_length=200, blank=True, help_text="SEO keywords separated by commas")
    canonical_url = models.URLField(blank=True, help_text="Canonical URL if different from post URL")
    
    # Schema markup and structured data
    schema_markup = models.JSONField(default=dict, help_text="Custom JSON-LD schema markup", blank=True, null=True)
    
    # Comprehensive Social Media Optimization
    # Open Graph (Facebook, WhatsApp, LinkedIn, etc.)
    og_title = models.CharField(max_length=100, blank=True, help_text="Open Graph title for social sharing")
    og_description = models.TextField(max_length=200, blank=True, help_text="Open Graph description for social sharing")
    og_image = models.ImageField(upload_to='blog/og/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_type = models.CharField(max_length=50, default='article', choices=[
        ('website', 'Website'),
        ('article', 'Article'),
        ('blog', 'Blog Post'),
        ('news.article', 'News Article'),
        ('tech.article', 'Tech Article'),
        ('howto', 'How-To Guide'),
        ('review', 'Review'),
        ('creative.work', 'Creative Work'),
    ])
    og_site_name = models.CharField(max_length=100, blank=True, help_text="Site name for Open Graph")
    og_locale = models.CharField(max_length=10, default='en_US', help_text="Locale for Open Graph")
    og_url = models.URLField(blank=True, help_text="Canonical URL for Open Graph")
    og_author = models.CharField(max_length=100, blank=True, help_text="Author for Open Graph")
    og_published_time = models.DateTimeField(blank=True, null=True, help_text="Published time for Open Graph")
    og_modified_time = models.DateTimeField(blank=True, null=True, help_text="Modified time for Open Graph")
    og_section = models.CharField(max_length=100, blank=True, help_text="Section for Open Graph")
    og_tag = models.CharField(max_length=200, blank=True, help_text="Tags for Open Graph")
    
    # Twitter Card
    twitter_card = models.CharField(max_length=20, default='summary_large_image', choices=[
        ('summary', 'Summary'),
        ('summary_large_image', 'Summary Large Image'),
        ('app', 'App'),
        ('player', 'Player'),
    ])
    twitter_title = models.CharField(max_length=100, blank=True, help_text="Twitter title (defaults to og_title)")
    twitter_description = models.TextField(max_length=200, blank=True, help_text="Twitter description (defaults to og_description)")
    twitter_image = models.ImageField(upload_to='blog/twitter/', blank=True, null=True, help_text="Twitter image (defaults to og_image)")
    twitter_creator = models.CharField(max_length=100, blank=True, help_text="Twitter creator handle (@username)")
    twitter_site = models.CharField(max_length=100, blank=True, help_text="Twitter site handle (@username)")
    
    # LinkedIn
    linkedin_title = models.CharField(max_length=100, blank=True, help_text="LinkedIn title (defaults to og_title)")
    linkedin_description = models.TextField(max_length=200, blank=True, help_text="LinkedIn description (defaults to og_description)")
    linkedin_image = models.ImageField(upload_to='blog/linkedin/', blank=True, null=True, help_text="LinkedIn image (defaults to og_image)")
    
    # WhatsApp
    whatsapp_title = models.CharField(max_length=100, blank=True, help_text="WhatsApp title (defaults to og_title)")
    whatsapp_description = models.TextField(max_length=200, blank=True, help_text="WhatsApp description (defaults to og_description)")
    whatsapp_image = models.ImageField(upload_to='blog/whatsapp/', blank=True, null=True, help_text="WhatsApp image (defaults to og_image)")
    
    # Pinterest
    pinterest_title = models.CharField(max_length=100, blank=True, help_text="Pinterest title (defaults to og_title)")
    pinterest_description = models.TextField(max_length=200, blank=True, help_text="Pinterest description (defaults to og_description)")
    pinterest_image = models.ImageField(upload_to='blog/pinterest/', blank=True, null=True, help_text="Pinterest image (defaults to og_description)")
    
    # Instagram
    instagram_title = models.CharField(max_length=100, blank=True, help_text="Instagram title (defaults to og_title)")
    instagram_description = models.TextField(max_length=200, blank=True, help_text="Instagram description (defaults to og_description)")
    instagram_image = models.ImageField(upload_to='blog/instagram/', blank=True, null=True, help_text="Instagram image (defaults to og_image)")
    
    # Reading time and difficulty
    estimated_reading_time = models.PositiveIntegerField(blank=True, null=True, help_text="Estimated reading time in minutes")
    
    # Internal linking and SEO
    internal_links = models.TextField(blank=True, help_text="List of internal links to other blog posts (one per line)")
    external_links = models.TextField(blank=True, help_text="List of external links with descriptions (one per line)")
    related_posts = models.ManyToManyField('self', blank=True, symmetrical=False, help_text="Manually select related posts")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def increase_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])

class SEOSettings(models.Model):
    """Global SEO settings for the blog"""
    site_name = models.CharField(max_length=200, default="DigitalPro")
    site_description = models.TextField(blank=True)
    site_keywords = models.CharField(max_length=500, blank=True)
    
    # Default schema markup
    organization_schema = models.JSONField(default=dict, help_text="Organization schema markup")
    website_schema = models.JSONField(default=dict, help_text="Website schema markup")
    
    # Social media defaults
    default_og_image = models.ImageField(upload_to='seo/', blank=True, null=True)
    twitter_creator = models.CharField(max_length=100, blank=True)
    twitter_site = models.CharField(max_length=100, blank=True)
    
    # Analytics and tracking
    google_analytics_id = models.CharField(max_length=50, blank=True)
    google_tag_manager_id = models.CharField(max_length=50, blank=True)
    facebook_pixel_id = models.CharField(max_length=50, blank=True)
    
    # Search console
    google_search_console_verification = models.CharField(max_length=100, blank=True)
    bing_webmaster_verification = models.CharField(max_length=100, blank=True)
    
    # Performance and security
    enable_amp = models.BooleanField(default=False, help_text="Enable AMP support")
    enable_structured_data = models.BooleanField(default=True, help_text="Enable automatic structured data")
    enable_social_sharing = models.BooleanField(default=True, help_text="Enable social media optimization")
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "SEO Settings"

    def __str__(self):
        return "SEO Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SEOSettings.objects.exists():
            return
        super().save(*args, **kwargs)

class PortfolioCategory(models.Model):
    """Model for portfolio categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    
    # SEO fields
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Portfolio Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class PortfolioMetric(models.Model):
    """Model for portfolio metrics and results"""
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='metrics_items')
    metric_value = models.CharField(max_length=100, help_text="The metric value (e.g., 300%, $2.1M, 2.5x)")
    metric_label = models.CharField(max_length=200, help_text="Description of the metric (e.g., Traffic Increase, Revenue Generated)")
    metric_type = models.CharField(max_length=50, choices=[
        ('percentage', 'Percentage'),
        ('currency', 'Currency'),
        ('multiplier', 'Multiplier'),
        ('number', 'Number'),
        ('text', 'Text'),
    ], default='text', help_text="Type of metric for proper formatting")
    order = models.PositiveIntegerField(default=0, help_text="Order of display")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Portfolio Metric"
        verbose_name_plural = "Portfolio Metrics"

    def __str__(self):
        return f"{self.metric_value} - {self.metric_label}"

    def get_formatted_value(self):
        """Return formatted metric value based on type"""
        if self.metric_type == 'percentage':
            return f"{self.metric_value}%"
        elif self.metric_type == 'currency':
            return f"${self.metric_value}"
        elif self.metric_type == 'multiplier':
            return f"{self.metric_value}x"
        else:
            return self.metric_value

class Portfolio(models.Model):
    """Model for portfolio items and case studies"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    client_name = models.CharField(max_length=200)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='portfolios')
    featured_image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    short_description = models.TextField(max_length=300)
    full_description = models.TextField()
    
    # Project details
    challenge = models.TextField(help_text="What was the client's challenge?")
    solution = models.TextField(help_text="How did we solve it?")
    implementation = models.TextField(help_text="What was our approach?")
    
    # Results
    results_summary = models.TextField(help_text="Summary of results achieved")
    
    # Before & After
    before_image = models.ImageField(upload_to='portfolio/before/', blank=True, null=True)
    after_image = models.ImageField(upload_to='portfolio/after/', blank=True, null=True)
    
    
    
    # Client testimonial
    client_testimonial = models.TextField(blank=True)
    client_position = models.CharField(max_length=100, blank=True)
    client_company = models.CharField(max_length=200, blank=True)
    
    # Advanced SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="Custom SEO title (defaults to portfolio title)")
    meta_description = models.TextField(max_length=160, blank=True, help_text="Custom SEO description (defaults to short description)")
    meta_keywords = models.CharField(max_length=200, blank=True, help_text="SEO keywords separated by commas")
    canonical_url = models.URLField(blank=True, help_text="Canonical URL if different from portfolio URL")
    
    # Schema markup and structured data
    schema_markup = models.JSONField(default=dict, help_text="Custom JSON-LD schema markup", blank=True, null=True)
    project_type = models.CharField(max_length=50, default='CreativeWork', choices=[
        ('CreativeWork', 'Creative Work'),
        ('WebSite', 'Website'),
        ('MobileApplication', 'Mobile App'),
        ('DigitalMarketing', 'Digital Marketing Campaign'),
        ('Branding', 'Branding Project'),
        ('ContentCreation', 'Content Creation'),
    ])
    
    # Comprehensive Social Media Optimization
    # Open Graph (Facebook, WhatsApp, LinkedIn, etc.)
    og_title = models.CharField(max_length=100, blank=True, help_text="Open Graph title for social sharing")
    og_description = models.TextField(max_length=200, blank=True, help_text="Open Graph description for social sharing")
    og_image = models.ImageField(upload_to='portfolio/og/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_type = models.CharField(max_length=50, default='website', choices=[
        ('website', 'Website'),
        ('article', 'Article'),
        ('product', 'Product'),
        ('creative.work', 'Creative Work'),
        ('business.business', 'Business'),
        ('place', 'Place'),
        ('profile', 'Profile'),
    ])
    og_site_name = models.CharField(max_length=100, blank=True, help_text="Site name for Open Graph")
    og_locale = models.CharField(max_length=10, default='en_US', help_text="Locale for Open Graph")
    og_url = models.URLField(blank=True, help_text="Canonical URL for Open Graph")
    
    # Twitter Card
    twitter_card = models.CharField(max_length=20, default='summary_large_image', choices=[
        ('summary', 'Summary'),
        ('summary_large_image', 'Summary Large Image'),
        ('app', 'App'),
        ('player', 'Player'),
    ])
    twitter_title = models.CharField(max_length=100, blank=True, help_text="Twitter title (defaults to og_title)")
    twitter_description = models.TextField(max_length=200, blank=True, help_text="Twitter description (defaults to og_description)")
    twitter_image = models.ImageField(upload_to='portfolio/twitter/', blank=True, null=True, help_text="Twitter image (defaults to og_image)")
    twitter_creator = models.CharField(max_length=100, blank=True, help_text="Twitter creator handle (@username)")
    twitter_site = models.CharField(max_length=100, blank=True, help_text="Twitter site handle (@username)")
    
    # LinkedIn
    linkedin_title = models.CharField(max_length=100, blank=True, help_text="LinkedIn title (defaults to og_title)")
    linkedin_description = models.TextField(max_length=200, blank=True, help_text="LinkedIn description (defaults to og_description)")
    linkedin_image = models.ImageField(upload_to='portfolio/linkedin/', blank=True, null=True, help_text="LinkedIn image (defaults to og_image)")
    
    # WhatsApp
    whatsapp_title = models.CharField(max_length=100, blank=True, help_text="WhatsApp title (defaults to og_title)")
    whatsapp_description = models.TextField(max_length=200, blank=True, help_text="WhatsApp description (defaults to og_description)")
    whatsapp_image = models.ImageField(upload_to='portfolio/whatsapp/', blank=True, null=True, help_text="WhatsApp image (defaults to og_image)")
    
    # Pinterest
    pinterest_title = models.CharField(max_length=100, blank=True, help_text="Pinterest title (defaults to og_title)")
    pinterest_description = models.TextField(max_length=200, blank=True, help_text="Pinterest description (defaults to og_description)")
    pinterest_image = models.ImageField(upload_to='portfolio/pinterest/', blank=True, null=True, help_text="Pinterest image (defaults to og_image)")
    
    # Instagram
    instagram_title = models.CharField(max_length=100, blank=True, help_text="Instagram title (defaults to og_title)")
    instagram_description = models.TextField(max_length=200, blank=True, help_text="Instagram description (defaults to og_description)")
    instagram_image = models.ImageField(upload_to='portfolio/instagram/', blank=True, null=True, help_text="Instagram image (defaults to og_image)")
    
    # Portfolio-specific SEO
    project_location = models.CharField(max_length=200, blank=True, help_text="Project location or target market")
    project_industry = models.CharField(max_length=200, blank=True, help_text="Client industry")
    project_budget = models.CharField(max_length=100, blank=True, help_text="Project budget range")
    
    # Internal linking and SEO
    related_portfolios = models.ManyToManyField('self', blank=True, symmetrical=False, help_text="Related portfolio items")
    related_services = models.ManyToManyField(Service, blank=True, related_name='case_studies', help_text="Services used in this project")
    client_logo = models.ImageField(upload_to='portfolio/clients/', blank=True, null=True, help_text="Client company logo")
    
    # SEO and display
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return f"{self.title} - {self.client_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.slug})

class TeamMember(models.Model):
    """Model for team members"""
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    expertise = models.TextField(blank=True, help_text="List of areas of expertise (one per line)")
    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    # Advanced SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="Custom SEO title (defaults to team member name)")
    meta_description = models.TextField(max_length=160, blank=True, help_text="Custom SEO description (defaults to bio)")
    meta_keywords = models.CharField(max_length=200, blank=True, help_text="SEO keywords separated by commas")
    
    # Schema markup and structured data
    schema_markup = models.JSONField(default=dict, help_text="Custom JSON-LD schema markup")
    
    # Comprehensive Social Media Optimization
    # Open Graph (Facebook, WhatsApp, LinkedIn, etc.)
    og_title = models.CharField(max_length=100, blank=True, help_text="Open Graph title for social sharing")
    og_description = models.TextField(max_length=200, blank=True, help_text="Open Graph description for social sharing")
    og_image = models.ImageField(upload_to='team/og/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_type = models.CharField(max_length=50, default='profile', choices=[
        ('website', 'Website'),
        ('article', 'Article'),
        ('profile', 'Profile'),
        ('person', 'Person'),
        ('business.business', 'Business'),
    ])
    og_site_name = models.CharField(max_length=100, blank=True, help_text="Site name for Open Graph")
    og_locale = models.CharField(max_length=10, default='en_US', help_text="Locale for Open Graph")
    og_url = models.URLField(blank=True, help_text="Canonical URL for Open Graph")
    
    # Twitter Card
    twitter_card = models.CharField(max_length=20, default='summary', choices=[
        ('summary', 'Summary'),
        ('summary_large_image', 'Summary Large Image'),
        ('app', 'App'),
        ('player', 'Player'),
    ])
    twitter_title = models.CharField(max_length=100, blank=True, help_text="Twitter title (defaults to og_title)")
    twitter_description = models.TextField(max_length=200, blank=True, help_text="Twitter description (defaults to og_description)")
    twitter_image = models.ImageField(upload_to='team/twitter/', blank=True, null=True, help_text="Twitter image (defaults to og_image)")
    twitter_creator = models.CharField(max_length=100, blank=True, help_text="Twitter creator handle (@username)")
    twitter_site = models.CharField(max_length=100, blank=True, help_text="Twitter site handle (@username)")
    
    # LinkedIn
    linkedin_title = models.CharField(max_length=100, blank=True, help_text="LinkedIn title (defaults to og_title)")
    linkedin_description = models.TextField(max_length=200, blank=True, help_text="LinkedIn description (defaults to og_description)")
    linkedin_image = models.ImageField(upload_to='team/linkedin/', blank=True, null=True, help_text="LinkedIn image (defaults to og_image)")
    
    # WhatsApp
    whatsapp_title = models.CharField(max_length=100, blank=True, help_text="WhatsApp title (defaults to og_title)")
    whatsapp_description = models.TextField(max_length=200, blank=True, help_text="WhatsApp description (defaults to og_description)")
    whatsapp_image = models.ImageField(upload_to='team/whatsapp/', blank=True, null=True, help_text="WhatsApp image (defaults to og_image)")
    
    # Pinterest
    pinterest_title = models.CharField(max_length=100, blank=True, help_text="Pinterest title (defaults to og_title)")
    pinterest_description = models.TextField(max_length=200, blank=True, help_text="Pinterest description (defaults to og_description)")
    pinterest_image = models.ImageField(upload_to='team/pinterest/', blank=True, null=True, help_text="Pinterest image (defaults to og_image)")
    
    # Instagram
    instagram_title = models.CharField(max_length=100, blank=True, help_text="Instagram title (defaults to og_title)")
    instagram_description = models.TextField(max_length=200, blank=True, help_text="Instagram description (defaults to og_description)")
    instagram_image = models.ImageField(upload_to='team/instagram/', blank=True, null=True, help_text="Instagram image (defaults to og_image)")
    
    # Team member specific SEO
    certifications = models.TextField(blank=True, help_text="List of professional certifications (one per line)")
    education = models.TextField(blank=True, help_text="Educational background (one per line)")
    achievements = models.TextField(blank=True, help_text="Professional achievements and awards (one per line)")
    speaking_engagements = models.TextField(blank=True, help_text="Speaking engagements and presentations (one per line)")
    
    # Internal linking and SEO
    related_team_members = models.ManyToManyField('self', blank=True, symmetrical=False, help_text="Related team members")
    authored_posts = models.ManyToManyField(BlogPost, blank=True, related_name='team_authors', help_text="Blog posts authored by this team member")
    featured_projects = models.ManyToManyField(Portfolio, blank=True, related_name='team_members', help_text="Portfolio projects this team member worked on")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"

class Testimonial(models.Model):
    """Model for client testimonials"""
    client_name = models.CharField(max_length=200)
    client_position = models.CharField(max_length=200)
    client_company = models.CharField(max_length=200)
    client_photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    # Advanced SEO fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="Custom SEO title for testimonial pages")
    meta_description = models.TextField(max_length=160, blank=True, help_text="Custom SEO description for testimonial pages")
    
    # Schema markup and structured data
    schema_markup = models.JSONField(default=dict, help_text="Custom JSON-LD schema markup")
    
    # Comprehensive Social Media Optimization
    # Open Graph (Facebook, WhatsApp, LinkedIn, etc.)
    og_title = models.CharField(max_length=100, blank=True, help_text="Open Graph title for social sharing")
    og_description = models.TextField(max_length=200, blank=True, help_text="Open Graph description for social sharing")
    og_image = models.ImageField(upload_to='testimonials/og/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_type = models.CharField(max_length=50, default='website', choices=[
        ('website', 'Website'),
        ('article', 'Article'),
        ('review', 'Review'),
        ('business.business', 'Business'),
        ('place', 'Place'),
    ])
    og_site_name = models.CharField(max_length=100, blank=True, help_text="Site name for Open Graph")
    og_locale = models.CharField(max_length=10, default='en_US', help_text="Locale for Open Graph")
    og_url = models.URLField(blank=True, help_text="Canonical URL for Open Graph")
    
    # Twitter Card
    twitter_card = models.CharField(max_length=20, default='summary', choices=[
        ('summary', 'Summary'),
        ('summary_large_image', 'Summary Large Image'),
        ('app', 'App'),
        ('player', 'Player'),
    ])
    twitter_title = models.CharField(max_length=100, blank=True, help_text="Twitter title (defaults to og_title)")
    twitter_description = models.TextField(max_length=200, blank=True, help_text="Twitter description (defaults to og_description)")
    twitter_image = models.ImageField(upload_to='testimonials/twitter/', blank=True, null=True, help_text="Twitter image (defaults to og_image)")
    twitter_creator = models.CharField(max_length=100, blank=True, help_text="Twitter creator handle (@username)")
    twitter_site = models.CharField(max_length=100, blank=True, help_text="Twitter site handle (@username)")
    
    # LinkedIn
    linkedin_title = models.CharField(max_length=100, blank=True, help_text="LinkedIn title (defaults to og_title)")
    linkedin_description = models.TextField(max_length=200, blank=True, help_text="LinkedIn description (defaults to og_description)")
    linkedin_image = models.ImageField(upload_to='testimonials/linkedin/', blank=True, null=True, help_text="LinkedIn image (defaults to og_image)")
    
    # WhatsApp
    whatsapp_title = models.CharField(max_length=100, blank=True, help_text="WhatsApp title (defaults to og_title)")
    whatsapp_description = models.TextField(max_length=200, blank=True, help_text="WhatsApp description (defaults to og_description)")
    whatsapp_image = models.ImageField(upload_to='testimonials/whatsapp/', blank=True, null=True, help_text="WhatsApp image (defaults to og_image)")
    
    # Pinterest
    pinterest_title = models.CharField(max_length=100, blank=True, help_text="Pinterest title (defaults to og_title)")
    pinterest_description = models.TextField(max_length=200, blank=True, help_text="Pinterest description (defaults to og_description)")
    pinterest_image = models.ImageField(upload_to='testimonials/pinterest/', blank=True, null=True, help_text="Pinterest image (defaults to og_description)")
    
    # Instagram
    instagram_title = models.CharField(max_length=100, blank=True, help_text="Instagram title (defaults to og_title)")
    instagram_description = models.TextField(max_length=200, blank=True, help_text="Instagram description (defaults to og_description)")
    instagram_image = models.ImageField(upload_to='testimonials/instagram/', blank=True, null=True, help_text="Instagram image (defaults to og_image)")
    
    # Testimonial specific SEO
    project_reference = models.CharField(max_length=200, blank=True, help_text="Reference to specific project")
    service_category = models.CharField(max_length=200, blank=True, help_text="Service category this testimonial relates to")
    testimonial_date = models.DateField(blank=True, null=True, help_text="Date when testimonial was given")
    
    # Internal linking and SEO - Connected to models
    related_services = models.ManyToManyField(Service, blank=True, related_name='testimonials', help_text="Services this testimonial relates to")
    related_portfolios = models.ManyToManyField(Portfolio, blank=True, related_name='testimonials', help_text="Portfolio items this testimonial relates to")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.client_company}"

class Contact(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200, blank=True)
    service_interest = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    
    # Security and spam prevention fields
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    referrer = models.URLField(blank=True)
    
    # Status tracking
    is_read = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('spam', 'Spam'),
        ],
        default='new'
    )
    
    # Admin notes
    admin_notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    def get_absolute_url(self):
        return reverse('admin:website_contact_change', args=[str(self.id)])
    
    @property
    def is_recent(self):
        """Check if submission is within last 24 hours"""
        from django.utils import timezone
        from datetime import timedelta
        return self.created_at > timezone.now() - timedelta(hours=24)

class Newsletter(models.Model):
    """Model for newsletter subscriptions"""
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email

class SiteSettings(models.Model):
    """Model for site-wide settings"""
    site_name = models.CharField(max_length=200, default="DigitalPro")
    site_description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Contact information
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_address = models.TextField(blank=True)
    
    # Social media
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    
    # Analytics
    google_analytics_code = models.TextField(blank=True)
    facebook_pixel_code = models.TextField(blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            return
        super().save(*args, **kwargs)
