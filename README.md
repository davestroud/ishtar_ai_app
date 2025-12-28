# Ishtar AI Website

A modern, professional website built with FastAPI and Jinja2 templates for Ishtar AI, showcasing AI solutions for finance and media industries.

## Architecture

```
Local Dev (Cursor) → GitHub → Replit Deploy
```

- **Local Development**: Code in Cursor on your machine
- **Version Control**: Push to GitHub
- **Deployment**: Replit pulls from GitHub and runs the app (auto-deploys on every commit)

## Tech Stack

- **FastAPI**: Modern Python web framework
- **Jinja2**: Template engine for server-side rendering
- **Poetry**: Dependency management
- **Uvicorn**: ASGI server
- **Pydantic Settings**: Configuration management

## Project Structure

```
ishtar-ai-app/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI entrypoint
│   ├── config.py                # Application settings
│   ├── middleware.py            # Security headers middleware
│   ├── content/                 # Blog articles and content
│   │   ├── __init__.py
│   │   └── blog_articles.py     # Blog article content
│   ├── routes/                  # Route handlers
│   │   ├── __init__.py
│   │   ├── pages.py             # Page routes
│   │   └── seo.py               # SEO routes (sitemap, robots.txt)
│   ├── templates/               # Jinja2 templates
│   │   ├── base.html            # Base template
│   │   ├── index.html           # Home page
│   │   ├── services.html        # Services page
│   │   ├── finance.html         # Finance solutions
│   │   ├── media_ads.html       # Media/Advertising solutions
│   │   ├── contact.html         # Contact form
│   │   ├── pricing.html         # Pricing page
│   │   ├── blog.html            # Blog listing
│   │   ├── blog_post.html       # Individual blog post
│   │   ├── faq.html             # FAQ page
│   │   ├── search.html          # Search page
│   │   ├── privacy.html         # Privacy Policy
│   │   ├── terms.html           # Terms of Service
│   │   ├── newsletter_success.html
│   │   ├── 404.html             # Custom 404 page
│   │   └── 500.html             # Custom 500 page
│   ├── static/                  # Static assets
│   │   ├── css/
│   │   │   └── styles.css       # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js          # JavaScript functionality
│   │   └── img/                 # Images and logos
│   └── utils/                    # Utility modules
│       ├── __init__.py
│       └── email.py             # Email sending utilities
├── tests/                       # Test directory
├── pyproject.toml               # Poetry configuration
├── README.md
├── .gitignore
├── .replit                      # Replit configuration
└── replit.nix                   # Nix configuration (optional)
```

## Setup

### Prerequisites

- Python 3.9+
- Poetry (recommended) or pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ishtar-ai-app
```

2. Install dependencies with Poetry:
```bash
poetry install
```

Or with pip:
```bash
pip install fastapi uvicorn jinja2 python-multipart pydantic-settings
```

3. Configure environment variables (optional):
Create a `.env` file in the root directory:
```env
# Email Configuration
EMAIL_ENABLED=false
EMAIL_PROVIDER=smtp
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your-email@example.com
SMTP_PASSWORD=your-password
SMTP_USE_TLS=true

# SendGrid (alternative)
# SENDGRID_API_KEY=your-api-key

# Analytics
GOOGLE_ANALYTICS_ID=G-KRTEM16GDJ

# Security
ENABLE_CSRF=true
CSRF_SECRET_KEY=your-secret-key
```

4. Run the development server:
```bash
poetry run uvicorn app.main:app --reload
```

Or with pip:
```bash
uvicorn app.main:app --reload
```

5. Open your browser and navigate to `http://localhost:8000`

## Pages

- **Home** (`/`): Landing page with hero section, features, testimonials, and newsletter signup
- **Services** (`/services`): Overview of AI services/products
- **Finance** (`/finance`): Finance-focused solutions and use cases
- **Media & Ads** (`/media-ads`): Media/Advertising-focused solutions
- **Pricing** (`/pricing`): Detailed pricing information and service packages
- **Blog** (`/blog`): Blog listing page
- **Blog Post** (`/blog/{slug}`): Individual blog articles with SEO and social sharing
- **FAQ** (`/faq`): Frequently asked questions
- **Search** (`/search`): Site search functionality
- **Contact** (`/contact`): Contact form and Calendly integration
- **Privacy Policy** (`/privacy`): Privacy policy page
- **Terms of Service** (`/terms`): Terms of service page

## Features

### SEO & Analytics
- ✅ Comprehensive SEO meta tags (Open Graph, Twitter Cards)
- ✅ JSON-LD structured data (Organization, WebSite, BlogPosting schemas)
- ✅ Dynamic sitemap.xml and robots.txt
- ✅ Google Analytics 4 integration with event tracking
- ✅ Canonical URLs for all pages

### Security
- ✅ Security headers middleware (CSP, X-Frame-Options, etc.)
- ✅ CSRF protection (honeypot fields)
- ✅ Input validation and sanitization

### Performance
- ✅ Lazy loading for images
- ✅ Cache control headers
- ✅ Resource hints (preconnect, dns-prefetch)
- ✅ Optimized CSS/JS delivery

### Accessibility
- ✅ Skip-to-content link
- ✅ ARIA labels and roles
- ✅ Keyboard navigation support
- ✅ WCAG compliance considerations
- ✅ Reduced motion support for animations

### User Experience
- ✅ Responsive design (mobile & desktop)
- ✅ Modern animations and micro-interactions
- ✅ Cookie consent banner
- ✅ Newsletter signup
- ✅ Social sharing buttons
- ✅ Custom error pages (404, 500)
- ✅ Search functionality

### Content Management
- ✅ Blog system with article content management
- ✅ FAQ accordion interface
- ✅ Testimonials section
- ✅ Newsletter subscription handling

## Development

### Running Locally

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag enables auto-reload on code changes.

### Adding New Pages

1. Create a new template in `app/templates/`
2. Add a route handler in `app/routes/pages.py`
3. Update navigation in `app/templates/base.html`
4. Add the route to `app/routes/seo.py` for sitemap inclusion

### Adding Blog Articles

1. Add article content function to `app/content/blog_articles.py`
2. Add article metadata to the `articles` dictionary in `app/routes/pages.py` (blog_post route)
3. Add blog post entry to the `posts` list in the blog route

### Code Organization

- **Routes**: Page handlers in `app/routes/pages.py`, SEO routes in `app/routes/seo.py`
- **Content**: Blog articles and static content in `app/content/`
- **Utilities**: Helper functions in `app/utils/`
- **Configuration**: Settings in `app/config.py`
- **Middleware**: Security and caching middleware in `app/middleware.py`

## Deployment to Replit

1. Push your code to GitHub
2. In Replit, import from GitHub
3. Replit will automatically detect the `.replit` configuration
4. The app will run on `uvicorn app.main:app --host 0.0.0.0 --port 8080`
5. Replit will auto-deploy on every commit

### Replit Configuration

The `.replit` file configures:
- Run command: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
- Python 3.11 module
- Entry point: `app/main.py`

## Configuration

### Email Integration

The contact form supports email sending via SMTP or SendGrid:

1. Set `EMAIL_ENABLED=true` in your `.env` file
2. Configure SMTP settings or SendGrid API key
3. Email will be sent when contact form is submitted

### Analytics

- **Google Analytics**: Set `GOOGLE_ANALYTICS_ID` in config (default: G-KRTEM16GDJ)
- **Plausible Analytics**: Set `PLAUSIBLE_DOMAIN` in config (optional)

### Customization

#### Updating Calendly Link

Edit `app/templates/contact.html` and update the Calendly URL:
```html
<a href="https://calendly.com/david-ishtar-ai" ...>
```

#### Styling

Modify `app/static/css/styles.css` to customize colors, fonts, and layout. The site uses CSS custom properties (variables) for easy theming.

#### Social Media Links

Update social media links in:
- `app/templates/base.html` (navbar and footer)
- JSON-LD structured data in `base.html`

## Dependencies

- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `jinja2`: Template engine
- `python-multipart`: Form data handling
- `pydantic-settings`: Configuration management

Optional (for email):
- `sendgrid`: SendGrid API client (install with `poetry add sendgrid`)

## License

Copyright © 2024 Ishtar AI. All rights reserved.
