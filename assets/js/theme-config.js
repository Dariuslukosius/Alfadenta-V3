tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: {
                    light: '#F4B1A8',
                    DEFAULT: '#EE8E81',
                    dark: '#D97669',
                },
                secondary: '#0c4a6e',
            }
        }
    }
}

// Scroll to Top Button Logic
document.addEventListener('DOMContentLoaded', function () {
    // Create button element
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up text-xl"></i>';
    scrollBtn.className = 'fixed bottom-8 right-8 z-50 w-12 h-12 rounded-full bg-[#EE8E81] text-white shadow-lg flex items-center justify-center transition-all duration-300 transform translate-y-10 opacity-0 pointer-events-none hover:bg-[#D97669] hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-[#EE8E81] focus:ring-offset-2';
    scrollBtn.setAttribute('aria-label', 'Grįžti į viršų');

    // Add to body
    document.body.appendChild(scrollBtn);

    // Scroll event listener
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-10');
        } else {
            scrollBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-10');
        }
    });

    // Click event listener
    scrollBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
