document.addEventListener('DOMContentLoaded', () => {
    const bgContainer = document.getElementById('background-container');
    if (!bgContainer) return;

    const layers = bgContainer.querySelectorAll('.bg-layer');
    const sections = document.querySelectorAll('section, header, footer');

    // Config: Map sections to background images (index 0, 1, 2)
    // We can use a simple modulo or specific mapping.
    // Let's try to map sections to images based on their order in the DOM.
    // Or simpler: change background every X sections.

    let currentBgIndex = 0;

    const observerOptions = {
        root: null,
        rootMargin: '-40% 0px -40% 0px', // Trigger when section is in middle 20% of viewport
        threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Determine which background to show based on the section
                const section = entry.target;

                // Example logic: 
                // Hero (first section) -> bg 0
                // Services -> bg 1
                // Why Choose Us -> bg 2
                // Testimonials -> bg 0
                // CTA -> bg 1
                // Footer -> bg 2

                let targetIndex = 0;

                // Simple heuristic based on check specific IDs or classes
                if (section.id === 'services') {
                    targetIndex = 1;
                } else if (section.classList.contains('bg-white') && !section.id) {
                    // "Why Choose Us" usually matches this after services
                    targetIndex = 2;
                } else if (section.classList.contains('bg-gray-50') && !section.id) {
                    targetIndex = 0; // Testimonials
                } else if (section.tagName === 'FOOTER') {
                    targetIndex = 2;
                }

                // Or cyclically based on node index?
                // Let's stick to a cycle based on explicit data attributes if present, otherwise cycle.

                // Let's try to set data-bg-index in HTML for explicit control.
                if (section.dataset.bgIndex !== undefined) {
                    targetIndex = parseInt(section.dataset.bgIndex);
                } else {
                    // Fallback or ignore
                    // Don't change if not specified? 
                    // Let's rely on HTML attributes for precision.
                    return;
                }

                if (targetIndex !== currentBgIndex) {
                    activateLayer(targetIndex);
                    currentBgIndex = targetIndex;
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    function activateLayer(index) {
        layers.forEach((layer, i) => {
            if (i === index) {
                layer.classList.add('active');
            } else {
                layer.classList.remove('active');
            }
        });
    }

    // Initial activation
    activateLayer(0);
});
