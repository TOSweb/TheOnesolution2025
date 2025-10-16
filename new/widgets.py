from django import forms
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django_json_widget.widgets import JSONEditorWidget


class UniversalTinyMCEWidget(Textarea):
    """
    Universal TinyMCE widget - one size fits all
    """
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'tinymce-editor-universal',
            'rows': 8,
            'cols': 80,
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class TinyMCEWidget(Textarea):
    """
    Universal TinyMCE widget with consistent sizing
    """
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'tinymce-editor',
            'rows': 8,
            'cols': 80,
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class TinyMCESmallWidget(Textarea):
    """
    Universal TinyMCE widget (same size as main widget)
    """
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'tinymce-editor-small',
            'rows': 8,
            'cols': 80,
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class TinyMCEInlineWidget(Textarea):
    """
    Universal TinyMCE widget for inline formsets (same size as main widget)
    """
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'tinymce-editor-inline',
            'rows': 8,
            'cols': 80,
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class CustomJSONWidget(JSONEditorWidget):
    """
    Custom JSON widget with better defaults for schema and structured data
    """
    def __init__(self, attrs=None, mode='code', options=None, width=None, height=None):
        default_options = {
            'modes': ['code', 'form', 'text', 'tree', 'view'],
            'mode': mode,
            'search': True,
            'history': True,
            'navigationBar': True,
            'statusBar': True,
            'mainMenuBar': True,
        }
        
        if options:
            default_options.update(options)
            
        super().__init__(
            attrs=attrs,
            mode=mode,
            options=default_options,
            width=width or '100%',
            height=height or '400px'
        )


class SchemaJSONWidget(CustomJSONWidget):
    """
    Specialized JSON widget for schema.org structured data
    """
    def __init__(self, attrs=None):
        schema_options = {
            'modes': ['code', 'tree', 'form'],
            'mode': 'tree',
            'search': True,
            'history': True,
            'navigationBar': True,
            'statusBar': True,
            'mainMenuBar': True,
        }
        
        super().__init__(
            attrs=attrs,
            mode='tree',
            options=schema_options,
            height='500px'
        )