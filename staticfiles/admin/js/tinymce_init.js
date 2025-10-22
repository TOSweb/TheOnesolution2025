/**
 * Minimal TinyMCE initialization for Django admin inline forms
 */
(function() {
    'use strict';

    const CONFIG = {
        height: 350,
        menubar: true,
        plugins: [
            'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
            'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
            'insertdatetime', 'media', 'table', 'help', 'wordcount'
        ],
        toolbar: 'undo redo | blocks | ' +
            'bold italic backcolor | alignleft aligncenter ' +
            'alignright alignjustify | bullist numlist outdent indent | ' +
            'removeformat | help',
        content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',
        relative_urls: false,
        remove_script_host: false,
        convert_urls: true,
        branding: false,
        promotion: false,
        license_key: 'gpl'
    };

    function initTinyMCE(container = document) {
        if (typeof tinymce === 'undefined') return;
        
        const textareas = container.querySelectorAll('.tinymce-editor, .tinymce-editor-universal, .tinymce-editor-small, .tinymce-editor-inline');
        textareas.forEach(textarea => {
            if (!textarea.id.includes('__prefix__') && !tinymce.get(textarea.id)) {
                tinymce.init({ target: textarea, ...CONFIG });
            }
        });
    }

    function handleInlineAdd() {
        // Wait for Django to update IDs from __prefix__ to real numbers
        setTimeout(() => initTinyMCE(), 100);
    }

    function setup() {
        initTinyMCE();
        
        // Handle Django inline form events
        if (typeof django !== 'undefined' && django.jQuery) {
            django.jQuery(document).on('formset:added', handleInlineAdd);
        }
    }

    // Load TinyMCE if needed, then setup
    if (typeof tinymce === 'undefined') {
        const script = document.createElement('script');
        script.src = '/static/tinymce/tinymce.min.js';
        script.onload = setup;
        document.head.appendChild(script);
    } else {
        document.addEventListener('DOMContentLoaded', setup);
    }
})();