from django import forms
from django.utils.safestring import mark_safe


class JSONEditorWidget(forms.Textarea):
    """
    JSON Editor Widget for editing JSON fields like schema markup
    Provides syntax highlighting and validation
    """
    
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/9.9.2/jsoneditor.min.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/9.9.2/jsoneditor.min.js',
        )
    
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update({
            'class': 'json-editor-widget',
            'style': 'font-family: monospace; font-size: 12px;'
        })
        super().__init__(attrs)
    
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        
        # Generate unique ID for this instance
        element_id = attrs.get('id', f'id_{name}')
        
        # Render the textarea
        textarea_html = super().render(name, value, attrs, renderer)
        
        # JavaScript to initialize JSON Editor
        init_script = f"""
        <script type="text/javascript">
        document.addEventListener('DOMContentLoaded', function() {{
            if (typeof JSONEditor !== 'undefined') {{
                const container = document.getElementById('{element_id}');
                if (container) {{
                    // Create JSON Editor container
                    const editorContainer = document.createElement('div');
                    editorContainer.id = 'json-editor-{element_id}';
                    editorContainer.style.height = '400px';
                    editorContainer.style.marginTop = '10px';
                    container.parentNode.insertBefore(editorContainer, container.nextSibling);
                    
                    // Hide the original textarea
                    container.style.display = 'none';
                    
                    // Initialize JSON Editor
                    const editor = new JSONEditor(editorContainer, {{
                        mode: 'tree',
                        modes: ['tree', 'code', 'text'],
                        onChangeText: function(jsonString) {{
                            try {{
                                const json = JSON.parse(jsonString);
                                container.value = JSON.stringify(json, null, 2);
                            }} catch (e) {{
                                // If invalid JSON, just store the text
                                container.value = jsonString;
                            }}
                        }},
                        onChangeJSON: function(json) {{
                            container.value = JSON.stringify(json, null, 2);
                        }}
                    }});
                    
                    // Set initial value
                    try {{
                        const initialValue = container.value;
                        if (initialValue) {{
                            const json = JSON.parse(initialValue);
                            editor.set(json);
                        }}
                    }} catch (e) {{
                        // If invalid JSON, set empty object
                        editor.set({{}});
                    }}
                    
                    // Add a button to show/hide the original textarea for debugging
                    const toggleButton = document.createElement('button');
                    toggleButton.type = 'button';
                    toggleButton.textContent = 'Toggle Raw JSON';
                    toggleButton.style.marginTop = '10px';
                    toggleButton.onclick = function() {{
                        container.style.display = container.style.display === 'none' ? 'block' : 'none';
                    }};
                    editorContainer.parentNode.insertBefore(toggleButton, editorContainer.nextSibling);
                }}
            }}
        }});
        </script>
        """
        
        return mark_safe(textarea_html + init_script)


class TinyMCEWidget(forms.Textarea):
    class Media:
        js = ('tinymce/tinymce.min.js',)

    def render(self, name, value, attrs=None, renderer=None):
        textarea = super().render(name, value, attrs, renderer)
        script = f'''
        <script type="text/javascript">
            tinymce.init({{
                selector: 'textarea[name="{name}"]',
                plugins: 'advlist autolink lists link image charmap preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste help wordcount',
                toolbar: 'undo redo | formatselect | bold italic underline | alignleft aligncenter alignright | bullist numlist outdent indent | link image media | code fullscreen',
                height: 400,
                license_key: 'gpl'
            }});
        </script>
        '''
        return mark_safe(textarea + script)


class TinyMCEMiniWidget(forms.Textarea):
    class Media:
        js = ('tinymce/tinymce.min.js',)

    def render(self, name, value, attrs=None, renderer=None):
        textarea = super().render(name, value, attrs, renderer)
        script = f'''
        <script type="text/javascript">
            tinymce.init({{
                selector: 'textarea[name="{name}"]',
                plugins: 'lists paste',
                toolbar: 'bullist numlist',
                width: '100%',
                height: 150,
                menubar: false,
                statusbar: false,
                resize: false,
                license_key: 'gpl'
            }});
        </script>
        '''
        return mark_safe(textarea + script)
