# Ishtar AI Website

A modern website built with FastAPI and Jinja2 templates for Ishtar AI, showcasing AI solutions for finance and media industries.

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

## Project Structure

```
ishtar-ai-site/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entrypoint
│   ├── routes/
│   │   └── pages.py         # Route handlers
│   ├── templates/
│   │   ├── base.html        # Base template
│   │   ├── index.html       # Home page
│   │   ├── services.html    # Services page
│   │   ├── finance.html     # Finance solutions
│   │   ├── media_ads.html   # Media/Advertising solutions
│   │   └── contact.html     # Contact form
│   └── static/
│       ├── css/
│       │   └── styles.css   # Stylesheet
│       ├── js/
│       │   └── main.js     # JavaScript
│       └── img/             # Images
├── tests/                   # Test directory
├── pyproject.toml           # Poetry configuration
├── README.md
├── .gitignore
├── .replit                  # Replit configuration
└── replit.nix              # Nix configuration (optional)
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

3. Run the development server:
```bash
poetry run uvicorn app.main:app --reload
```

Or with pip:
```bash
uvicorn app.main:app --reload
```

4. Open your browser and navigate to `http://localhost:8000`

## Pages

- **Home** (`/`): Landing page with hero section and overview
- **Services** (`/services`): List of 6 AI services/products
- **Finance** (`/finance`): Finance-focused solutions
- **Media & Ads** (`/media-ads`): Media/Advertising-focused solutions
- **Contact** (`/contact`): Contact form and Calendly integration

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

## Features

- ✅ SEO-friendly server-side rendering
- ✅ Responsive design (mobile & desktop)
- ✅ Contact form with validation
- ✅ Calendly integration (placeholder link)
- ✅ Clean navigation structure
- ✅ Modern, professional styling

## Customization

### Updating Calendly Link

Edit `app/templates/contact.html` and replace the placeholder URL:
```html
<a href="https://calendly.com/ishtar-ai/consultation" ...>
```

### Styling

Modify `app/static/css/styles.css` to customize colors, fonts, and layout.

### Adding Email Integration

The contact form currently returns a success message. To add email functionality:

1. Add an email service (e.g., SendGrid, AWS SES)
2. Update the POST handler in `app/routes/pages.py`
3. Configure environment variables for API keys

## Dependencies

- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `jinja2`: Template engine
- `python-multipart`: Form data handling
- `pydantic-settings`: Configuration management

## License

Copyright © 2024 Ishtar AI. All rights reserved.
