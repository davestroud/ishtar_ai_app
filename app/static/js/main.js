// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function () {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            const isExpanded = navMenu.classList.toggle('active');
            navToggle.setAttribute('aria-expanded', isExpanded);
        });

        // Close menu when clicking outside
        document.addEventListener('click', function (event) {
            const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
            if (!isClickInsideNav && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Navbar scroll behavior
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', function () {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // Active page indicator
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath ||
            (currentPath === '/' && link.getAttribute('href') === '/')) {
            link.classList.add('active');
        }
    });

    // Ripple effect for buttons
    function createRipple(event) {
        const button = event.currentTarget;
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;

        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';

        button.appendChild(ripple);

        setTimeout(() => {
            ripple.remove();
        }, 600);
    }

    // Add ripple effect to all buttons
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', createRipple);
    });

    // Track CTA button clicks
    document.querySelectorAll('.btn-primary, .btn-secondary, .btn-link').forEach(button => {
        button.addEventListener('click', function () {
            const buttonText = this.textContent.trim() || this.querySelector('span')?.textContent.trim() || 'CTA Button';
            const href = this.getAttribute('href') || '';

            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    'event_category': 'CTA',
                    'event_label': buttonText,
                    'value': href
                });
            }

            if (typeof plausible !== 'undefined') {
                plausible('CTA Click', { props: { button: buttonText, href: href } });
            }
        });
    });

    // Intersection Observer for scroll-triggered animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all elements with slide-up class
    const animatedElements = document.querySelectorAll('.slide-up, .feature-card, .service-card, .solution-card, .use-case-item');
    animatedElements.forEach((el, index) => {
        el.classList.add('slide-up');
        el.style.transitionDelay = `${index * 0.1}s`;
        observer.observe(el);
    });

    // Back to Top Button
    const backToTopButton = document.getElementById('back-to-top');

    if (backToTopButton) {
        window.addEventListener('scroll', function () {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });

        backToTopButton.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Form Validation with Enhanced Feedback
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
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
            } else {
                // Track form submission event
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'form_submit', {
                        'event_category': 'Contact',
                        'event_label': 'Contact Form'
                    });
                }

                // Plausible Analytics
                if (typeof plausible !== 'undefined') {
                    plausible('Contact Form Submission');
                }

                // Add success animation
                contactForm.style.opacity = '0.7';
                setTimeout(() => {
                    contactForm.style.opacity = '1';
                }, 100);
            }
        });

        // Add floating label behavior
        const formInputs = contactForm.querySelectorAll('input, textarea');
        formInputs.forEach(input => {
            const formGroup = input.closest('.form-group');
            if (formGroup && !formGroup.classList.contains('floating-label')) {
                formGroup.classList.add('floating-label');

                // Move label after input for CSS sibling selector
                const label = formGroup.querySelector('label');
                if (label && input.id) {
                    const labelFor = label.getAttribute('for');
                    if (labelFor === input.id) {
                        input.insertAdjacentElement('afterend', label);
                    }
                }
            }

            // Handle focus and blur
            input.addEventListener('focus', function () {
                this.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', function () {
                if (!this.value) {
                    this.parentElement.classList.remove('focused');
                }
            });

            // Check if input has value on load
            if (input.value) {
                input.parentElement.classList.add('focused');
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
    errorDiv.style.animation = 'slideDown 0.3s ease-out';
    input.parentElement.appendChild(errorDiv);
}

// Cookie Consent
(function () {
    const cookieConsent = document.getElementById('cookie-consent');
    const acceptBtn = document.getElementById('accept-cookies');
    const declineBtn = document.getElementById('decline-cookies');

    if (!cookieConsent) return;

    // Check if user has already made a choice
    const consent = localStorage.getItem('cookie-consent');
    if (!consent) {
        cookieConsent.style.display = 'block';
    }

    if (acceptBtn) {
        acceptBtn.addEventListener('click', function () {
            localStorage.setItem('cookie-consent', 'accepted');
            cookieConsent.style.display = 'none';
            if (typeof gtag !== 'undefined') {
                gtag('event', 'cookie_consent', {
                    'event_category': 'Privacy',
                    'event_label': 'Accepted'
                });
            }
        });
    }

    if (declineBtn) {
        declineBtn.addEventListener('click', function () {
            localStorage.setItem('cookie-consent', 'declined');
            cookieConsent.style.display = 'none';
            if (typeof gtag !== 'undefined') {
                gtag('event', 'cookie_consent', {
                    'event_category': 'Privacy',
                    'event_label': 'Declined'
                });
            }
        });
    }
})();

// FAQ Accordion
(function () {
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', function () {
            const faqItem = this.closest('.faq-item');
            const isExpanded = this.getAttribute('aria-expanded') === 'true';

            // Close all other items
            document.querySelectorAll('.faq-item').forEach(item => {
                if (item !== faqItem) {
                    item.classList.remove('active');
                    item.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
                }
            });

            // Toggle current item
            if (isExpanded) {
                faqItem.classList.remove('active');
                this.setAttribute('aria-expanded', 'false');
            } else {
                faqItem.classList.add('active');
                this.setAttribute('aria-expanded', 'true');

                // Track FAQ view
                if (typeof gtag !== 'undefined') {
                    const questionText = this.querySelector('h3').textContent;
                    gtag('event', 'faq_view', {
                        'event_category': 'Engagement',
                        'event_label': questionText
                    });
                }
            }
        });
    });
})();

// Social Sharing
(function () {
    const socialShare = document.getElementById('social-share');
    const shareButtons = document.querySelectorAll('.social-share-btn');

    // Show share buttons on blog posts
    if (window.location.pathname.includes('/blog/')) {
        if (socialShare) {
            socialShare.style.display = 'flex';
        }
    }

    shareButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            const platform = this.getAttribute('data-platform');
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent(document.title);
            let shareUrl = '';

            switch (platform) {
                case 'twitter':
                    shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
                    break;
                case 'linkedin':
                    shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${url}`;
                    break;
                case 'email':
                    shareUrl = `mailto:?subject=${title}&body=${url}`;
                    break;
            }

            if (shareUrl) {
                window.open(shareUrl, '_blank', 'width=600,height=400');

                // Track social share
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'share', {
                        'method': platform,
                        'content_type': 'blog_post',
                        'item_id': window.location.pathname
                    });
                }
            }
        });
    });
})();

// Newsletter Form Tracking
(function () {
    const newsletterForms = document.querySelectorAll('.newsletter-form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function (e) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'newsletter_signup', {
                    'event_category': 'Lead Generation',
                    'event_label': 'Newsletter Subscription'
                });
            }
        });
    });
})();

// Enhanced GA4 Tracking - Page View with Scroll Depth
(function () {
    let maxScroll = 0;
    const scrollThresholds = [25, 50, 75, 90, 100];

    window.addEventListener('scroll', function () {
        const scrollPercent = Math.round(
            (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100
        );

        if (scrollPercent > maxScroll) {
            scrollThresholds.forEach(threshold => {
                if (scrollPercent >= threshold && maxScroll < threshold) {
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'scroll_depth', {
                            'event_category': 'Engagement',
                            'event_label': `${threshold}%`,
                            'value': threshold
                        });
                    }
                }
            });
            maxScroll = scrollPercent;
        }
    });
})();

// Track Time on Page
(function () {
    let startTime = Date.now();
    const trackInterval = 30000; // 30 seconds

    setInterval(function () {
        const timeOnPage = Math.round((Date.now() - startTime) / 1000);
        if (typeof gtag !== 'undefined' && timeOnPage % 30 === 0) {
            gtag('event', 'time_on_page', {
                'event_category': 'Engagement',
                'event_label': '30 seconds',
                'value': timeOnPage
            });
        }
    }, trackInterval);
})();

// Pricing Page Analytics
(function () {
    if (window.location.pathname === '/pricing') {
        // Track pricing page view
        if (typeof gtag !== 'undefined') {
            gtag('event', 'page_view', {
                'event_category': 'Pricing',
                'event_label': 'Pricing Page'
            });
        }

        // Track pricing card interactions
        const pricingCards = document.querySelectorAll('.pricing-card');
        pricingCards.forEach((card, index) => {
            const cardTitle = card.querySelector('h3')?.textContent || `Pricing Tier ${index + 1}`;

            // Track card views (when scrolled into view)
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        if (typeof gtag !== 'undefined') {
                            gtag('event', 'pricing_card_view', {
                                'event_category': 'Pricing',
                                'event_label': cardTitle
                            });
                        }
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });

            observer.observe(card);

            // Track CTA clicks
            const ctaButton = card.querySelector('.pricing-cta');
            if (ctaButton) {
                ctaButton.addEventListener('click', function () {
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'pricing_cta_click', {
                            'event_category': 'Pricing',
                            'event_label': cardTitle,
                            'value': index + 1
                        });
                    }
                });
            }
        });
    }
})();
