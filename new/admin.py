from django.contrib import admin
from django import forms
from django_json_widget.widgets import JSONEditorWidget
from .models import (
    Home, AlternateHome, About, ServiceCategory, ServiceCategoryContent, 
    Service, ServiceContent, ServiceVariant, ServiceVariantContent
)
from .widgets import (
    UniversalTinyMCEWidget, TinyMCEWidget, TinyMCESmallWidget, TinyMCEInlineWidget,
    CustomJSONWidget, SchemaJSONWidget
)


# Custom Forms with TinyMCE widgets
# Note: All widgets now have universal sizing (350px height, same features)
# You can use UniversalTinyMCEWidget for all fields, or keep the existing ones
# Example: 'content': UniversalTinyMCEWidget(),

class HomeAdminForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'
        widgets = {
            'small_description': TinyMCEWidget(),
            'meta_description': TinyMCESmallWidget(),
            'og_description': TinyMCESmallWidget(),
            'schema': SchemaJSONWidget(),
        }


class AboutAdminForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'small_description': TinyMCEWidget(),
            'content': TinyMCEWidget(),
            'vision': TinyMCEWidget(),
            'mission': TinyMCEWidget(),
            'meta_description': TinyMCESmallWidget(),
            'og_description': TinyMCESmallWidget(),
            'schema': SchemaJSONWidget(),
        }


class ServiceCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = '__all__'
        widgets = {
            'small_description': TinyMCEWidget(),
            'content': TinyMCEWidget(),
            'meta_description': TinyMCESmallWidget(),
            'og_description': TinyMCESmallWidget(),
            'schema': SchemaJSONWidget(),
        }


class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'small_description': TinyMCEWidget(),
            'content': TinyMCEWidget(),
            'meta_description': TinyMCESmallWidget(),
            'og_description': TinyMCESmallWidget(),
            'schema': SchemaJSONWidget(),
        }


class ServiceVariantAdminForm(forms.ModelForm):
    class Meta:
        model = ServiceVariant
        fields = '__all__'
        widgets = {
            'small_description': TinyMCEWidget(),
            'content': TinyMCEWidget(),
            'meta_description': TinyMCESmallWidget(),
            'og_description': TinyMCESmallWidget(),
            'schema': SchemaJSONWidget(),
        }


# Inline Forms for dynamic formsets
class ServiceCategoryContentInlineForm(forms.ModelForm):
    class Meta:
        model = ServiceCategoryContent
        fields = '__all__'
        widgets = {
            'content': TinyMCEInlineWidget(),
        }


class ServiceContentInlineForm(forms.ModelForm):
    class Meta:
        model = ServiceContent
        fields = '__all__'
        widgets = {
            'content': TinyMCEInlineWidget(),
        }


class ServiceVariantContentInlineForm(forms.ModelForm):
    class Meta:
        model = ServiceVariantContent
        fields = '__all__'
        widgets = {
            'content': TinyMCEInlineWidget(),
        }


# Inline Admin Classes
class AlternateHomeInline(admin.TabularInline):
    model = AlternateHome
    extra = 1


class ServiceCategoryContentInline(admin.TabularInline):
    model = ServiceCategoryContent
    form = ServiceCategoryContentInlineForm
    extra = 1


class ServiceContentInline(admin.TabularInline):
    model = ServiceContent
    form = ServiceContentInlineForm
    extra = 1


class ServiceVariantContentInline(admin.TabularInline):
    model = ServiceVariantContent
    form = ServiceVariantContentInlineForm
    extra = 1


# Main Admin Classes
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    form = HomeAdminForm
    inlines = [AlternateHomeInline]
    list_display = ['title', 'heading', 'project_completed', 'client_retention']
    search_fields = ['title', 'heading']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'heading', 'small_description')
        }),
        ('Statistics', {
            'fields': ('project_completed', 'client_retention', 'no_of_clients', 'years_of_experience')
        }),
        ('SEO Meta', {
            'fields': ('meta_description', 'meta_keywords', 'canonical_url'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_type', 'og_url', 'og_image', 'og_description', 'og_site_name'),
            'classes': ('collapse',)
        }),
        ('Schema', {
            'fields': ('schema',),
            'classes': ('collapse',)
        }),
    )

    class Media:
        js = ('admin/js/tinymce_init.js',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm
    list_display = ['heading', 'slug']
    search_fields = ['heading', 'slug']
    prepopulated_fields = {'slug': ('heading',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('heading', 'slug', 'small_description', 'content')
        }),
        ('Images', {
            'fields': ('image_m', 'image_t', 'image_d', 'alt')
        }),
        ('Vision & Mission', {
            'fields': ('vision', 'mission')
        }),
        ('SEO Meta', {
            'fields': ('title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_type', 'og_url', 'og_image', 'og_description', 'og_site_name'),
            'classes': ('collapse',)
        }),
        ('Schema', {
            'fields': ('schema',),
            'classes': ('collapse',)
        }),
    )

    class Media:
        js = ('admin/js/tinymce_init.js',)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    form = ServiceCategoryAdminForm
    inlines = [ServiceCategoryContentInline]
    list_display = ['heading', 'slug']
    search_fields = ['heading', 'slug']
    prepopulated_fields = {'slug': ('heading',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('heading', 'slug', 'small_description', 'content')
        }),
        ('Images', {
            'fields': ('image_m', 'image_t', 'image_d', 'alt')
        }),
        ('SEO Meta', {
            'fields': ('title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_type', 'og_url', 'og_image', 'og_description', 'og_site_name'),
            'classes': ('collapse',)
        }),
        ('Schema', {
            'fields': ('schema',),
            'classes': ('collapse',)
        }),
    )

    class Media:
        js = ('admin/js/tinymce_init.js',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    inlines = [ServiceContentInline]
    list_display = ['heading', 'service_category', 'slug']
    list_filter = ['service_category']
    search_fields = ['heading', 'slug']
    prepopulated_fields = {'slug': ('heading',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('service_category', 'heading', 'slug', 'small_description', 'content')
        }),
        ('Images', {
            'fields': ('image_m', 'image_t', 'image_d', 'alt')
        }),
        ('SEO Meta', {
            'fields': ('title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_type', 'og_url', 'og_image', 'og_description', 'og_site_name'),
            'classes': ('collapse',)
        }),
        ('Schema', {
            'fields': ('schema',),
            'classes': ('collapse',)
        }),
    )

    class Media:
        js = ('admin/js/tinymce_init.js',)


@admin.register(ServiceVariant)
class ServiceVariantAdmin(admin.ModelAdmin):
    form = ServiceVariantAdminForm
    inlines = [ServiceVariantContentInline]
    list_display = ['heading', 'service_category', 'slug']
    list_filter = ['service_category']
    search_fields = ['heading', 'slug']
    prepopulated_fields = {'slug': ('heading',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('service_category', 'heading', 'slug', 'small_description', 'content')
        }),
        ('Images', {
            'fields': ('image_m', 'image_t', 'image_d', 'alt')
        }),
        ('SEO Meta', {
            'fields': ('title', 'meta_description', 'meta_keywords', 'canonical_url'),
            'classes': ('collapse',)
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_type', 'og_url', 'og_image', 'og_description', 'og_site_name'),
            'classes': ('collapse',)
        }),
        ('Schema', {
            'fields': ('schema',),
            'classes': ('collapse',)
        }),
    )

    class Media:
        js = ('admin/js/tinymce_init.js',)