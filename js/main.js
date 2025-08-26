// Main JavaScript for SS & MS Fabrication Website

// Mobile menu toggle
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Close mobile menu when a link is clicked
const mobileMenuLinks = mobileMenu.getElementsByTagName('a');
for (let link of mobileMenuLinks) {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
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
        }
    });
});

// Initialize Swiper
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        640: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    }
});

// Intersection Observer for animations
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
document.querySelector('form[name="contact"]').addEventListener('submit', function (e) {
    const submitButton = this.querySelector('button[type="submit"]');
    submitButton.textContent = 'Sending...';
    submitButton.disabled = true;
});

// Handle logo loading error
document.querySelector('nav img').addEventListener('error', function () {
    this.parentElement.classList.add('logo-error');
});

// Handle image loading errors in gallery
document.querySelectorAll('.swiper-slide img').forEach(img => {
    img.addEventListener('error', function () {
        this.style.display = 'none';
        const placeholder = document.createElement('div');
        placeholder.className = 'w-full h-96 bg-gray-300 rounded-lg flex items-center justify-center';
        placeholder.innerHTML = `<span class="text-gray-600 text-lg">${this.alt}</span>`;
        this.parentElement.appendChild(placeholder);
    });
});

// Handle workshop image error
const workshopImg = document.querySelector('img[alt="Our Fabrication Workshop"]');
if (workshopImg) {
    workshopImg.addEventListener('error', function () {
        const placeholder = document.createElement('div');
        placeholder.className = 'bg-gray-300 rounded-lg shadow-xl w-full h-80 flex items-center justify-center';
        placeholder.innerHTML = '<span class="text-gray-600 text-lg">Workshop Image</span>';
        this.parentElement.replaceChild(placeholder, this);
    });
}