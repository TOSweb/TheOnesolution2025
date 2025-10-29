/**
 * TinyMCE initialization for Django admin with production fixes
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
        license_key: 'gpl',
        // Production fixes
        base_url: '/static/tinymce/',
        suffix: '.min',
        cache_suffix: '?v=' + Date.now()
    };

    let isInitialized = false;

    function initTinyMCE(container = document) {
        if (typeof tinymce === 'undefined') {
            console.warn('TinyMCE not loaded');
            return;
        }
        
        const selectors = [
            '.tinymce-editor', 
            '.tinymce-editor-universal', 
            '.tinymce-editor-small', 
            '.tinymce-editor-inline'
        ];
        
        selectors.forEach(selector => {
            const textareas = container.querySelectorAll(selector);
            textareas.forEach(textarea => {
                // Skip if already initialized or has __prefix__
                if (textarea.id.includes('__prefix__') || tinymce.get(textarea.id)) {
                    return;
                }
                
                try {
                    tinymce.init({
                        target: textarea,
                        ...CONFIG,
                        setup: function(editor) {
                            editor.on('init', function() {
                                console.log('TinyMCE initialized for:', textarea.id);
                            });
                        }
                    });
                } catch (error) {
                    console.error('TinyMCE init error for', textarea.id, error);
                }
            });
        });
    }

    function handleInlineAdd(event) {
        console.log('Inline form added, initializing TinyMCE...');
        // Wait for Django to update IDs from __prefix__ to real numbers
        setTimeout(() => {
            initTinyMCE();
        }, 200);
    }

    function setup() {
        if (isInitialized) return;
        isInitialized = true;
        
        console.log('Setting up TinyMCE...');
        
        // Initialize existing textareas
        initTinyMCE();
        
        // Handle Django inline form events
        if (typeof django !== 'undefined' && django.jQuery) {
            django.jQuery(document).on('formset:added', handleInlineAdd);
            console.log('Django formset events bound');
        } else {
            console.warn('Django jQuery not available');
        }
    }

    function loadTinyMCE() {
        if (typeof tinymce !== 'undefined') {
            setup();
            return;
        }

        const script = document.createElement('script');
        script.src = '/static/tinymce/tinymce.min.js';
        script.async = true;
        
        script.onload = function() {
            console.log('TinyMCE script loaded');
            // Wait a bit for TinyMCE to fully initialize
            setTimeout(setup, 100);
        };
        
        script.onerror = function() {
            console.error('Failed to load TinyMCE script');
        };
        
        document.head.appendChild(script);
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadTinyMCE);
    } else {
        loadTinyMCE();
    }

    // Fallback for late initialization
    window.addEventListener('load', function() {
        if (!isInitialized) {
            console.log('Fallback TinyMCE initialization');
            loadTinyMCE();
        }
    });

})();
