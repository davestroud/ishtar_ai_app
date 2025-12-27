// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
            if (!isClickInsideNav && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
            }
        });
    }

    // Form Validation
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const message = document.getElementById('message');

            let isValid = true;

            // Clear previous errors
            document.querySelectorAll('.error-message').forEach(el => el.remove());
            document.querySelectorAll('.form-group input, .form-group textarea').forEach(el => {
                el.classList.remove('error');
            });

            // Validate name
            if (!name.value.trim()) {
                showError(name, 'Name is required');
                isValid = false;
            }

            // Validate email
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email.value.trim()) {
                showError(email, 'Email is required');
                isValid = false;
            } else if (!emailRegex.test(email.value)) {
                showError(email, 'Please enter a valid email address');
                isValid = false;
            }

            // Validate message
            if (!message.value.trim()) {
                showError(message, 'Message is required');
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();
            }
        });
    }
});

function showError(input, message) {
    input.classList.add('error');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    errorDiv.style.color = 'var(--error-color)';
    errorDiv.style.fontSize = '0.875rem';
    errorDiv.style.marginTop = '0.25rem';
    input.parentElement.appendChild(errorDiv);
}

