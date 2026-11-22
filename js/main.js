// SS & MS Fabrication Website JavaScript

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            const isHidden = mobileMenu.classList.toggle('hidden');
            mobileMenuBtn.setAttribute('aria-expanded', String(!isHidden));
        });
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
                // Close mobile menu if open
                if (mobileMenu) {
                    mobileMenu.classList.add('hidden');
                }
            }
        });
    });

    // Photo lightbox for .work-grid galleries (tap a photo to enlarge, swipe/arrow through)
    const gridLinks = Array.from(document.querySelectorAll('.work-grid a'));
    if (gridLinks.length) {
        const box = document.createElement('div');
        box.className = 'lightbox';
        box.hidden = true;
        box.setAttribute('role', 'dialog');
        box.setAttribute('aria-modal', 'true');
        box.innerHTML = '<figure><img alt=""><figcaption></figcaption></figure>' +
            '<button class="lb-close" aria-label="Close">&times;</button>' +
            '<button class="lb-prev" aria-label="Previous photo">&lsaquo;</button>' +
            '<button class="lb-next" aria-label="Next photo">&rsaquo;</button>';
        document.body.appendChild(box);
        const img = box.querySelector('img');
        const cap = box.querySelector('figcaption');
        let index = 0;
        let touchX = null;

        const show = function (i) {
            index = (i + gridLinks.length) % gridLinks.length;
            const link = gridLinks[index];
            img.src = link.getAttribute('href');
            img.alt = link.dataset.caption || '';
            cap.textContent = link.dataset.caption || '';
            box.hidden = false;
            document.body.style.overflow = 'hidden';
        };
        const close = function () {
            box.hidden = true;
            document.body.style.overflow = '';
        };

        gridLinks.forEach(function (link, i) {
            link.addEventListener('click', function (e) {
                // Home page tiles link to service pages; only enlarge direct image links
                if (!/\.(webp|jpe?g|png)$/i.test(link.getAttribute('href'))) return;
                e.preventDefault();
                show(i);
            });
        });
        box.querySelector('.lb-close').addEventListener('click', close);
        box.querySelector('.lb-prev').addEventListener('click', function () { show(index - 1); });
        box.querySelector('.lb-next').addEventListener('click', function () { show(index + 1); });
        box.addEventListener('click', function (e) { if (e.target === box) close(); });
        document.addEventListener('keydown', function (e) {
            if (box.hidden) return;
            if (e.key === 'Escape') close();
            if (e.key === 'ArrowLeft') show(index - 1);
            if (e.key === 'ArrowRight') show(index + 1);
        });
        box.addEventListener('touchstart', function (e) { touchX = e.touches[0].clientX; }, { passive: true });
        box.addEventListener('touchend', function (e) {
            if (touchX === null) return;
            const dx = e.changedTouches[0].clientX - touchX;
            if (Math.abs(dx) > 50) show(index + (dx < 0 ? 1 : -1));
            touchX = null;
        });
    }

    // Intersection Observer for loading animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('loaded');
            }
        });
    }, observerOptions);

    // Observe all elements with loading class
    document.querySelectorAll('.loading').forEach(el => {
        observer.observe(el);
    });

    // Form submission handling
    const contactForm = document.querySelector('form[name="contact"]');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Lets success.html know this visit came from a real form submission,
            // so the Google Ads conversion is counted once and only for genuine leads.
            try { sessionStorage.setItem('ssms_form_submitted', '1'); } catch (err) {}
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.textContent = 'Sending...';
                submitButton.disabled = true;
            }
        });
    }

    // Keep the footer year current
    const yearEl = document.getElementById('year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // Handle logo loading error
    const logoImg = document.querySelector('nav img');
    if (logoImg) {
        logoImg.addEventListener('error', function() {
            this.parentElement.classList.add('logo-error');
        });
    }

    // Handle image loading errors in gallery
    document.querySelectorAll('.work-grid img').forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.className = 'w-full h-96 bg-gray-300 rounded-lg flex items-center justify-center';
            placeholder.innerHTML = `<span class="text-gray-600 text-lg">${this.alt}</span>`;
            this.parentElement.appendChild(placeholder);
        });
    });

    // Handle workshop image error
    const workshopImg = document.querySelector('img[alt*="Workshop"]');
    if (workshopImg) {
        workshopImg.addEventListener('error', function() {
            const placeholder = document.createElement('div');
            placeholder.className = 'bg-gray-300 rounded-lg shadow-xl w-full h-80 flex items-center justify-center';
            placeholder.innerHTML = '<span class="text-gray-600 text-lg">Workshop Image</span>';
            this.parentElement.replaceChild(placeholder, this);
        });
    }

    // Add scroll effect to header
    let lastScrollTop = 0;
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Only hide the header on phones (they have the bottom call bar). On tablets and
        // desktops the header carries the phone number, so it stays visible.
        if (window.innerWidth >= 768) {
            header.style.transform = 'translateY(0)';
            lastScrollTop = scrollTop;
            return;
        }

        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            header.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            header.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });

    // Add transition to header
    if (header) {
        header.style.transition = 'transform 0.3s ease-in-out';
    }
});