from django.core.management.base import BaseCommand
from new.models import Home, About, ServiceCategory, ServiceCategoryContent


class Command(BaseCommand):
    help = 'Create test data to verify TinyMCE setup'

    def handle(self, *args, **options):
        # Create test Home instance
        home, created = Home.objects.get_or_create(
            title="Test Home Page",
            defaults={
                'meta_description': 'Test meta description for home page',
                'meta_keywords': 'test, home, page',
                'heading': 'Welcome to The One Solution',
                'small_description': '<p>This is a <strong>test description</strong> with HTML content.</p>',
                'schema': {},
                'project_completed': 100,
                'client_retention': 95,
                'no_of_clients': 50,
                'years_of_experience': 10,
                'og_title': 'Test OG Title',
                'og_type': 'website',
                'og_url': 'https://example.com',
                'og_image': 'https://example.com/image.jpg',
                'og_description': 'Test OG description',
                'og_site_name': 'The One Solution',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created Home instance'))
        else:
            self.stdout.write(self.style.WARNING('Home instance already exists'))

        # Create test About instance
        about, created = About.objects.get_or_create(
            slug="test-about",
            defaults={
                'heading': 'About The One Solution',
                'small_description': '<p>This is our <em>company story</em>.</p>',
                'content': '<h2>Our Story</h2><p>We are a leading digital marketing agency...</p>',
                'vision': '<p>Our vision is to <strong>transform businesses</strong> through digital innovation.</p>',
                'mission': '<p>Our mission is to deliver <em>exceptional results</em> for our clients.</p>',
                'title': 'About Us - The One Solution',
                'meta_description': 'Learn about The One Solution digital marketing agency',
                'meta_keywords': 'about, company, digital marketing',
                'schema': {},
                'og_title': 'About The One Solution',
                'og_type': 'website',
                'og_url': 'https://example.com/about',
                'og_image': 'https://example.com/about-image.jpg',
                'og_description': 'Learn about our company',
                'og_site_name': 'The One Solution',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created About instance'))
        else:
            self.stdout.write(self.style.WARNING('About instance already exists'))

        # Create test Service Category with inline content
        service_category, created = ServiceCategory.objects.get_or_create(
            slug="test-service-category",
            defaults={
                'heading': 'Digital Marketing Services',
                'small_description': '<p>Comprehensive <strong>digital marketing solutions</strong> for your business.</p>',
                'content': '<h2>Our Services</h2><p>We offer a wide range of digital marketing services...</p>',
                'title': 'Digital Marketing Services',
                'meta_description': 'Professional digital marketing services',
                'meta_keywords': 'digital marketing, services, SEO, PPC',
                'schema': {},
                'og_title': 'Digital Marketing Services',
                'og_type': 'website',
                'og_url': 'https://example.com/services',
                'og_image': 'https://example.com/services-image.jpg',
                'og_description': 'Professional digital marketing services',
                'og_site_name': 'The One Solution',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created ServiceCategory instance'))
            
            # Create inline content for testing tabular inline formsets
            ServiceCategoryContent.objects.create(
                service_category=service_category,
                content='<h3>SEO Services</h3><p>Improve your search engine rankings with our <strong>expert SEO services</strong>.</p>'
            )
            
            ServiceCategoryContent.objects.create(
                service_category=service_category,
                content='<h3>PPC Advertising</h3><p>Drive targeted traffic with our <em>professional PPC campaigns</em>.</p>'
            )
            
            self.stdout.write(self.style.SUCCESS('Created ServiceCategoryContent instances'))
        else:
            self.stdout.write(self.style.WARNING('ServiceCategory instance already exists'))

        self.stdout.write(
            self.style.SUCCESS(
                'Test data created successfully! '
                'You can now test TinyMCE in the Django admin at /admin/'
            )
        )
