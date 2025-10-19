(function() {
    'use strict';

    function initTinyMCEForAll() {
        if (typeof tinymce === 'undefined') {
            setTimeout(initTinyMCEForAll, 200);
            return;
        }

        // Remove previous editors before reinitializing
        tinymce.remove('textarea[name$="content"], textarea[class*="tinymce"]');

        document.querySelectorAll('textarea[name$="content"], textarea[class*="tinymce"]').forEach((textarea) => {
            // Skip hidden template (__prefix__)
            if (textarea.name.includes('__prefix__')) return;

            // Skip if already initialized
            if (tinymce.get(textarea.id)) return;

            tinymce.init({
                target: textarea,
                height: 350,
                menubar: true,
                plugins: [
                    'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
                    'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
                    'insertdatetime', 'media', 'table', 'help', 'wordcount'
                ],
                toolbar: 'undo redo | blocks | bold italic backcolor | ' +
                         'alignleft aligncenter alignright alignjustify | ' +
                         'bullist numlist outdent indent | removeformat | help',
                content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',
                relative_urls: false,
                remove_script_host: false,
                convert_urls: true,
                branding: false,
                promotion: false,
                license_key: 'gpl',
                setup: function(editor) {
                    editor.on('init', function() {
                        editor.getBody().setAttribute('contenteditable', 'true');
                    });
                    editor.on('change keyup', function() {
                        editor.save();
                    });
                }
            });
        });
    }

    // Run once on page load
    document.addEventListener('DOMContentLoaded', initTinyMCEForAll);

    // Re-run whenever a new inline form is added
    document.addEventListener('formset:added', function() {
        setTimeout(initTinyMCEForAll, 100);
    });
})();
