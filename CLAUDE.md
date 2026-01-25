# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
poetry install

# Run development server (auto-reload enabled)
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run without poetry (if dependencies installed globally)
uvicorn app.main:app --reload
```

## Architecture

This is a FastAPI website with Jinja2 server-side rendering for Ishtar AI.

**Deployment flow:** Local Dev → GitHub → Replit (auto-deploys on commit)

### Key Entry Points

- `app/main.py` - FastAPI app initialization, middleware setup, error handlers
- `app/config.py` - Pydantic settings loaded from `.env` (email, analytics, security)
- `app/routes/pages.py` - All page route handlers
- `app/routes/seo.py` - Sitemap.xml and robots.txt generation

### Content Management

Blog articles are defined in `app/content/blog_articles.py`. To add a new article:
1. Add article content function to `app/content/blog_articles.py`
2. Add article metadata to the `articles` dict in `app/routes/pages.py`
3. Add entry to the `posts` list in the blog route

### Adding New Pages

1. Create template in `app/templates/`
2. Add route handler in `app/routes/pages.py`
3. Update navigation in `app/templates/base.html`
4. Add route to `app/routes/seo.py` for sitemap

### Static Assets

- CSS: `app/static/css/styles.css` (uses CSS custom properties for theming)
- JS: `app/static/js/main.js`
- Images: `app/static/img/`

### Middleware

`app/middleware.py` adds security headers (CSP, X-Frame-Options, etc.)
