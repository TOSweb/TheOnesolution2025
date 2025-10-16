/**
 * TinyMCE Initialization for Django Admin
 * Handles dynamic inline formsets by initializing based on CSS class names
 */

(function() {
    'use strict';

    // Universal TinyMCE configuration - same size and features for all editors
    const UNIVERSAL_CONFIG = {
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
        // Auto-save for all editors
        setup: function(editor) {
            editor.on('change', function() {
                editor.save();
            });
        }
    };

    // TinyMCE configuration objects - all using universal config
    const TINYMCE_CONFIGS = {
        // Universal editor configuration - one config for all
        universal: {
            selector: '.tinymce-editor-universal',
            ...UNIVERSAL_CONFIG
        },

        // Full editor configuration
        full: {
            selector: '.tinymce-editor',
            ...UNIVERSAL_CONFIG
        },

        // Small editor configuration (same as full now)
        small: {
            selector: '.tinymce-editor-small',
            ...UNIVERSAL_CONFIG
        },

        // Inline editor configuration (same as full now)
        inline: {
            selector: '.tinymce-editor-inline',
            ...UNIVERSAL_CONFIG
        }
    };

    // Initialize TinyMCE for existing elements
    function initializeTinyMCE() {
        // Only initialize if TinyMCE is loaded
        if (typeof tinymce !== 'undefined') {
            // Initialize each configuration
            Object.values(TINYMCE_CONFIGS).forEach(config => {
                // Check if elements with this selector exist and aren't already initialized
                const elements = document.querySelectorAll(config.selector);
                const uninitializedElements = Array.from(elements).filter(el => 
                    !tinymce.get(el.id) && el.style.display !== 'none'
                );
                
                if (uninitializedElements.length > 0) {
                    tinymce.init(config);
                }
            });
        }
    }

    // Initialize TinyMCE for dynamically added elements (inline formsets)
    function initializeDynamicTinyMCE(container) {
        if (typeof tinymce === 'undefined') return;

        // Find all TinyMCE target elements in the container
        const selectors = ['.tinymce-editor-universal', '.tinymce-editor', '.tinymce-editor-small', '.tinymce-editor-inline'];
        
        selectors.forEach(selector => {
            const elements = container.querySelectorAll(selector);
            elements.forEach(element => {
                // Skip if already initialized or hidden
                if (tinymce.get(element.id) || element.style.display === 'none') {
                    return;
                }

                // Determine which config to use
                let config;
                if (element.classList.contains('tinymce-editor-universal')) {
                    config = Object.assign({}, TINYMCE_CONFIGS.universal);
                } else if (element.classList.contains('tinymce-editor-small')) {
                    config = Object.assign({}, TINYMCE_CONFIGS.small);
                } else if (element.classList.contains('tinymce-editor-inline')) {
                    config = Object.assign({}, TINYMCE_CONFIGS.inline);
                } else {
                    config = Object.assign({}, TINYMCE_CONFIGS.full);
                }

                // Set specific target for this element
                config.target = element;
                delete config.selector;

                // Initialize TinyMCE for this specific element
                tinymce.init(config);
            });
        });
    }

    // Clean up TinyMCE instances for removed elements
    function cleanupTinyMCE(container) {
        if (typeof tinymce === 'undefined') return;

        // Get all TinyMCE instances
        tinymce.editors.forEach(editor => {
            // If the editor's target element is not in the DOM anymore, remove it
            if (!document.contains(editor.getElement())) {
                editor.remove();
            }
        });
    }

    // Django admin inline formset event handlers
    function setupInlineFormsetHandlers() {
        // Handle when new inline forms are added
        document.addEventListener('formset:added', function(event) {
            const newForm = event.target;
            // Small delay to ensure DOM is ready
            setTimeout(() => {
                initializeDynamicTinyMCE(newForm);
            }, 100);
        });

        // Handle when inline forms are removed
        document.addEventListener('formset:removed', function(event) {
            setTimeout(() => {
                cleanupTinyMCE(document);
            }, 100);
        });

        // Fallback: Monitor for dynamically added rows using MutationObserver
        if (window.MutationObserver) {
            const observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.type === 'childList') {
                        mutation.addedNodes.forEach(function(node) {
                            if (node.nodeType === Node.ELEMENT_NODE) {
                                // Check if it's an inline form row
                                if (node.classList && (
                                    node.classList.contains('dynamic-form') ||
                                    node.querySelector('.dynamic-form') ||
                                    node.querySelector('.tinymce-editor-universal, .tinymce-editor, .tinymce-editor-small, .tinymce-editor-inline')
                                )) {
                                    setTimeout(() => {
                                        initializeDynamicTinyMCE(node);
                                    }, 100);
                                }
                            }
                        });

                        mutation.removedNodes.forEach(function(node) {
                            if (node.nodeType === Node.ELEMENT_NODE) {
                                setTimeout(() => {
                                    cleanupTinyMCE(document);
                                }, 100);
                            }
                        });
                    }
                });
            });

            // Start observing
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        }
    }

    // Initialize when DOM is ready
    function initialize() {
        // Set TinyMCE base URL to your static files
        if (typeof tinymce !== 'undefined') {
            tinymce.baseURL = '/static/tinymce';
        }

        // Initial TinyMCE setup
        initializeTinyMCE();
        
        // Setup handlers for dynamic forms
        setupInlineFormsetHandlers();

        // Re-initialize on Django admin events
        document.addEventListener('DOMContentLoaded', initializeTinyMCE);
        
        // Handle Django admin's dynamic form events
        if (typeof django !== 'undefined' && django.jQuery) {
            django.jQuery(document).on('formset:added', function(event, $row) {
                setTimeout(() => {
                    initializeDynamicTinyMCE($row[0]);
                }, 100);
            });

            django.jQuery(document).on('formset:removed', function() {
                setTimeout(() => {
                    cleanupTinyMCE(document);
                }, 100);
            });
        }
    }

    // Load TinyMCE if not already loaded
    function loadTinyMCE() {
        if (typeof tinymce === 'undefined') {
            const script = document.createElement('script');
            script.src = '/static/tinymce/tinymce.min.js';
            script.onload = initialize;
            document.head.appendChild(script);
        } else {
            initialize();
        }
    }

    // Start the initialization process
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadTinyMCE);
    } else {
        loadTinyMCE();
    }

})();
