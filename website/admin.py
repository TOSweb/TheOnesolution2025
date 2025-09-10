from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import (
    Service, BlogCategory, BlogPost, BlogTag, PortfolioCategory, Portfolio,
    TeamMember, Testimonial, Contact, Newsletter, SiteSettings, SEOSettings, PortfolioMetric
)
from .widgets import TinyMCEWidget


class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'short_description': TinyMCEWidget(),
            'full_description': TinyMCEWidget(),
            'features': TinyMCEWidget(),
            'process_steps': TinyMCEWidget(),
            'benefits': TinyMCEWidget(),
            'meta_description': TinyMCEWidget(),
            'og_description': TinyMCEWidget(),
            'twitter_description': TinyMCEWidget(),
            'linkedin_description': TinyMCEWidget(),
            'whatsapp_description': TinyMCEWidget(),
            'pinterest_description': TinyMCEWidget(),
            'instagram_description': TinyMCEWidget(),
        }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ['title', 'is_featured', 'is_active', 'order', 'pricing', 'service_area', 'created_at']
    list_filter = ['is_featured', 'is_active', 'service_area', 'service_industry', 'created_at']
    list_editable = ['is_featured', 'is_active', 'order', 'pricing']
    search_fields = ['title', 'short_description', 'full_description', 'service_area', 'service_industry']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'full_description', 'icon', 'image')
        }),
        ('Service Details', {
            'fields': ('service_area', 'service_industry', 'service_duration', 'pricing', 'is_featured', 'is_active', 'order')
        }),
        ('Features & Process', {
            'fields': ('features', 'process_steps', 'benefits')
        }),
        ('Related Services', {
            'fields': ('related_services',)
        }),
        ('SEO & Social Media', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'canonical_url', 'schema_markup'),
            'classes': ('collapse',)
        }),
        ('Open Graph (Facebook, WhatsApp, LinkedIn)', {
            'fields': ('og_title', 'og_description', 'og_image', 'og_type', 'og_site_name', 'og_locale', 'og_url'),
            'classes': ('collapse',)
        }),
        ('Twitter Cards', {
            'fields': ('twitter_card', 'twitter_title', 'twitter_description', 'twitter_image', 'twitter_creator', 'twitter_site'),
            'classes': ('collapse',)
        }),
        ('Other Platforms', {
            'fields': ('linkedin_title', 'linkedin_description', 'linkedin_image', 'whatsapp_title', 'whatsapp_description', 'whatsapp_image', 'pinterest_title', 'pinterest_description', 'pinterest_image', 'instagram_title', 'instagram_description', 'instagram_image'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    filter_horizontal = ['related_services']

class BlogCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = '__all__'
        widgets = {
            'description': TinyMCEWidget(),
            'meta_description': TinyMCEWidget(),
        }


class BlogTagAdminForm(forms.ModelForm):
    class Meta:
        model = BlogTag
        fields = '__all__'
        widgets = {
            'meta_description': TinyMCEWidget(),
        }


class PortfolioCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = PortfolioCategory
        fields = '__all__'
        widgets = {
            'description': TinyMCEWidget(),
            'meta_description': TinyMCEWidget(),
        }


class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'excerpt': TinyMCEWidget(),
            'content': TinyMCEWidget(),
            'meta_description': TinyMCEWidget(),
            'og_description': TinyMCEWidget(),
            'twitter_description': TinyMCEWidget(),
            'linkedin_description': TinyMCEWidget(),
            'whatsapp_description': TinyMCEWidget(),
            'pinterest_description': TinyMCEWidget(),
            'instagram_description': TinyMCEWidget(),
            'internal_links': TinyMCEWidget(),
            'external_links': TinyMCEWidget(),
        }


class TeamMemberAdminForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        widgets = {
            'bio': TinyMCEWidget(),
            'expertise': TinyMCEWidget(),
            'meta_description': TinyMCEWidget(),
            'og_description': TinyMCEWidget(),
            'twitter_description': TinyMCEWidget(),
            'linkedin_description': TinyMCEWidget(),
            'whatsapp_description': TinyMCEWidget(),
            'pinterest_description': TinyMCEWidget(),
            'instagram_description': TinyMCEWidget(),
            'certifications': TinyMCEWidget(),
            'education': TinyMCEWidget(),
            'achievements': TinyMCEWidget(),
            'speaking_engagements': TinyMCEWidget(),
        }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ['title', 'category', 'author', 'status', 'is_featured', 'published_date', 'views_count', 'created_at']
    list_filter = ['status', 'category', 'author', 'published_date', 'created_at', 'is_featured']
    list_editable = ['status', 'is_featured']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views_count', 'created_at', 'updated_at']
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    filter_horizontal = ['tags']
    date_hierarchy = 'published_date'
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image', 'category', 'tags')
        }),
        ('Publishing', {
            'fields': ('author', 'status', 'is_featured', 'published_date')
        }),
        ('SEO & Social Media', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'canonical_url', 'schema_markup'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image', 'og_type', 'og_site_name', 'og_locale', 'og_url'),
            'classes': ('collapse',)
        }),
        ('Twitter Cards', {
            'fields': ('twitter_card', 'twitter_title', 'twitter_description', 'twitter_image', 'twitter_creator', 'twitter_site'),
            'classes': ('collapse',)
        }),
        ('Other Platforms', {
            'fields': ('linkedin_title', 'linkedin_description', 'linkedin_image', 'whatsapp_title', 'whatsapp_description', 'whatsapp_image', 'pinterest_title', 'pinterest_description', 'pinterest_image', 'instagram_title', 'instagram_description', 'instagram_image'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    form = BlogCategoryAdminForm
    list_display = ['name', 'slug', 'description', 'color', 'created_at']
    list_filter = ['created_at']
    list_editable = ['color']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    form = PortfolioCategoryAdminForm
    list_display = ['name', 'slug', 'description']
    list_filter = []
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

class PortfolioAdminForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        widgets = {
            'short_description': TinyMCEWidget(),
            'full_description': TinyMCEWidget(),
            'challenge': TinyMCEWidget(),
            'solution': TinyMCEWidget(),
            'implementation': TinyMCEWidget(),
            'results_summary': TinyMCEWidget(),
            'client_testimonial': TinyMCEWidget(),
            'meta_description': TinyMCEWidget(),
            'og_description': TinyMCEWidget(),
            'twitter_description': TinyMCEWidget(),
            'linkedin_description': TinyMCEWidget(),
            'whatsapp_description': TinyMCEWidget(),
            'pinterest_description': TinyMCEWidget(),
            'instagram_description': TinyMCEWidget(),
        }


class PortfolioMetricInline(admin.TabularInline):
    """Inline admin for portfolio metrics"""
    model = PortfolioMetric
    extra = 1
    fields = ('metric_value', 'metric_label', 'metric_type', 'order')
    ordering = ('order',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioAdminForm
    list_display = ['title', 'client_name', 'category', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    list_editable = ['is_featured']
    search_fields = ['title', 'client_name', 'short_description', 'full_description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PortfolioMetricInline]
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    filter_horizontal = ['related_services', 'related_portfolios']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'slug', 'client_name', 'category', 'short_description', 'full_description', 'featured_image')
        }),
        ('Project Details', {
            'fields': ('challenge', 'solution', 'implementation')
        }),
        ('Results & Metrics', {
            'fields': ('results_summary', 'before_image', 'after_image'),
            'description': 'Add metrics using the inline form below'
        }),
        ('Client Feedback', {
            'fields': ('client_testimonial', 'client_position', 'client_company', 'client_logo')
        }),
        ('Project Settings', {
            'fields': ('is_featured', 'order', 'project_location', 'project_industry', 'project_budget')
        }),
        ('Related Content', {
            'fields': ('related_services', 'related_portfolios'),
            'classes': ('collapse',)
        }),
        ('SEO & Social Media', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'canonical_url', 'schema_markup'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image', 'og_type', 'og_site_name', 'og_locale', 'og_url'),
            'classes': ('collapse',)
        }),
        ('Twitter Cards', {
            'fields': ('twitter_card', 'twitter_title', 'twitter_description', 'twitter_image', 'twitter_creator', 'twitter_site'),
            'classes': ('collapse',)
        }),
        ('Other Platforms', {
            'fields': ('linkedin_title', 'linkedin_description', 'linkedin_image', 'whatsapp_title', 'whatsapp_description', 'whatsapp_image', 'pinterest_title', 'pinterest_description', 'pinterest_image', 'instagram_title', 'instagram_description', 'instagram_image'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PortfolioMetric)
class PortfolioMetricAdmin(admin.ModelAdmin):
    """Admin for portfolio metrics (standalone view)"""
    list_display = ['portfolio', 'metric_value', 'metric_label', 'metric_type', 'order']
    list_filter = ['metric_type', 'portfolio__category']
    list_editable = ['order']
    search_fields = ['metric_value', 'metric_label', 'portfolio__title']
    ordering = ['portfolio', 'order']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberAdminForm
    list_display = ['name', 'position', 'is_active', 'order', 'experience_years', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['is_active', 'order', 'experience_years']
    search_fields = ['name', 'position', 'bio']
    readonly_fields = ['created_at', 'updated_at']
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    filter_horizontal = ['authored_posts', 'featured_projects']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'bio', 'photo', 'email')
        }),
        ('Professional Details', {
            'fields': ('expertise', 'experience_years', 'certifications', 'education', 'achievements')
        }),
        ('Social Media', {
            'fields': ('linkedin', 'twitter', 'github')
        }),
        ('Content & Projects', {
            'fields': ('authored_posts', 'featured_projects')
        }),
        ('SEO & Social Media', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'canonical_url', 'schema_markup'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image', 'og_type', 'og_site_name', 'og_locale', 'og_url'),
            'classes': ('collapse',)
        }),
        ('Twitter Cards', {
            'fields': ('twitter_card', 'twitter_title', 'twitter_description', 'twitter_image', 'twitter_creator', 'twitter_site'),
            'classes': ('collapse',)
        }),
        ('Other Platforms', {
            'fields': ('linkedin_title', 'linkedin_description', 'linkedin_image', 'whatsapp_title', 'whatsapp_description', 'whatsapp_image', 'pinterest_title', 'pinterest_description', 'pinterest_image', 'instagram_title', 'instagram_description', 'instagram_image'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    
    list_display = ['client_name', 'client_company', 'rating', 'is_featured', 'order', 'created_at']
    list_filter = ['is_featured', 'rating', 'created_at']
    list_editable = ['is_featured', 'order', 'rating']
    search_fields = ['client_name', 'client_company', 'content']
    readonly_fields = ['created_at']
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    filter_horizontal = ['related_services', 'related_portfolios']
    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_position', 'client_company', 'client_photo')
        }),
        ('Testimonial Content', {
            'fields': ('content', 'rating', 'project_reference', 'service_category', 'testimonial_date')
        }),
        ('Relationships', {
            'fields': ('related_services', 'related_portfolios')
        }),
        ('SEO & Social Media', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'canonical_url', 'schema_markup'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image', 'og_type', 'og_site_name', 'og_locale', 'og_url'),
            'classes': ('collapse',)
        }),
        ('Twitter Cards', {
            'fields': ('twitter_card', 'twitter_title', 'twitter_description', 'twitter_image', 'twitter_creator', 'twitter_site'),
            'classes': ('collapse',)
        }),
        ('Other Platforms', {
            'fields': ('linkedin_title', 'linkedin_description', 'linkedin_image', 'whatsapp_title', 'whatsapp_description', 'whatsapp_image', 'pinterest_title', 'pinterest_description', 'pinterest_image', 'instagram_title', 'instagram_description', 'instagram_image'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'service_interest', 'status', 'is_read', 'is_spam', 'created_at']
    list_filter = ['status', 'is_read', 'is_spam', 'created_at', 'service_interest']
    list_editable = ['status', 'is_read', 'is_spam']
    search_fields = ['name', 'email', 'company', 'message', 'service_interest']
    readonly_fields = ['created_at', 'updated_at', 'ip_address', 'user_agent', 'referrer']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company', 'service_interest', 'message')
        }),
        ('Status & Processing', {
            'fields': ('status', 'is_read', 'is_spam', 'admin_notes')
        }),
        ('Security & Tracking', {
            'fields': ('ip_address', 'user_agent', 'referrer'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_spam', 'mark_as_completed']
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True, status='in_progress')
        self.message_user(request, f'{updated} contact submissions marked as read.')
    mark_as_read.short_description = "Mark selected submissions as read"
    
    def mark_as_spam(self, request, queryset):
        updated = queryset.update(is_spam=True, status='spam')
        self.message_user(request, f'{updated} contact submissions marked as spam.')
    mark_as_spam.short_description = "Mark selected submissions as spam"
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} contact submissions marked as completed.')
    mark_as_completed.short_description = "Mark selected submissions as completed"

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at', 'unsubscribed_at']
    list_filter = ['is_active', 'subscribed_at', 'unsubscribed_at']
    list_editable = ['is_active']
    search_fields = ['email']
    readonly_fields = ['subscribed_at', 'unsubscribed_at']

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    
    list_display = ['site_name', 'site_description', 'contact_email']
    
    def has_add_permission(self, request):
        # Only allow one site settings instance
        return not SiteSettings.objects.exists()

@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'organization_schema', 'website_schema']
    readonly_fields = ['updated_at']
    
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    
    def has_add_permission(self, request):
        # Only allow one SEO settings instance
        return not SEOSettings.objects.exists()

# Customize admin site
admin.site.site_header = "DigitalPro CMS Admin"
admin.site.site_title = "DigitalPro Admin Portal"
admin.site.index_title = "Welcome to DigitalPro Content Management"
