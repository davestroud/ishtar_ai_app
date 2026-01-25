# Build Scripts

This directory contains build and deployment scripts for the Ishtar AI website.

## minify_assets.py

Minifies CSS and JS files for production deployment.

### Installation

Install the required dependencies:

```bash
poetry install --with dev
```

### Usage

Run the minification script:

```bash
python scripts/minify_assets.py
```

This will create minified versions of all CSS and JS files in the static directory:
- `app/static/css/styles.css` → `app/static/css/styles.min.css`
- `app/static/js/main.js` → `app/static/js/main.min.js`

### Production Deployment

To use minified assets in production:

1. Run the minification script before deploying
2. Update your templates to reference the minified files
3. Or use environment-based template logic:

```jinja2
{% if config.environment == "production" %}
<link rel="stylesheet" href="/static/css/styles.min.css">
{% else %}
<link rel="stylesheet" href="/static/css/styles.css">
{% endif %}
```

### Automation

You can add this to your deployment pipeline:

```bash
# In your deployment script
poetry run python scripts/minify_assets.py
```
