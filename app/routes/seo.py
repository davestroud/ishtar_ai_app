from fastapi import APIRouter
from fastapi.responses import Response
from datetime import datetime

from app.utils.rss import generate_rss_feed

router = APIRouter()


def get_blog_posts_for_rss():
    """Get blog posts formatted for RSS feed"""
    # Import blog posts data
    from app.routes.pages import get_blog_posts

    posts_data = get_blog_posts()
    rss_posts = []

    for post in posts_data:
        rss_posts.append(
            {
                "title": post.get("title", ""),
                "slug": post.get("slug", ""),
                "description": post.get("excerpt", ""),
                "published_date": datetime.fromisoformat(
                    post.get("date", "2024-01-15")
                ),
                "author": post.get("author", "Ishtar AI Team"),
                "categories": ["AI", "Finance", "RAG", "LLM"],  # Default categories
            }
        )

    return rss_posts


@router.get("/sitemap.xml")
async def sitemap():
    """Generate sitemap.xml for search engines"""
    base_url = "https://ishtar-ai.com"
    current_date = datetime.now().strftime("%Y-%m-%d")

    pages = [
        {"loc": "/", "changefreq": "weekly", "priority": "1.0"},
        {"loc": "/services", "changefreq": "monthly", "priority": "0.9"},
        {"loc": "/pricing", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/case-studies", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/resources", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/demo", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/finance", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/media-ads", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/blog", "changefreq": "weekly", "priority": "0.8"},
        {"loc": "/faq", "changefreq": "monthly", "priority": "0.7"},
        {"loc": "/contact", "changefreq": "monthly", "priority": "0.7"},
        {"loc": "/privacy", "changefreq": "yearly", "priority": "0.3"},
        {"loc": "/terms", "changefreq": "yearly", "priority": "0.3"},
        {"loc": "/security", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/trust-center", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/about", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/implementation", "changefreq": "monthly", "priority": "0.7"},
        {"loc": "/responsible-ai", "changefreq": "monthly", "priority": "0.7"},
        {"loc": "/products/rag-copilots", "changefreq": "monthly", "priority": "0.8"},
        {
            "loc": "/products/agent-automation",
            "changefreq": "monthly",
            "priority": "0.8",
        },
        {
            "loc": "/products/llmops-foundation",
            "changefreq": "monthly",
            "priority": "0.8",
        },
        {"loc": "/products/genai-security", "changefreq": "monthly", "priority": "0.8"},
        {
            "loc": "/products/synthetic-media-compliance",
            "changefreq": "monthly",
            "priority": "0.8",
        },
    ]

    # Add individual case studies
    try:
        from app.content.case_studies import get_case_studies

        case_studies = get_case_studies()
        for case_study in case_studies:
            pages.append(
                {
                    "loc": f"/case-studies/{case_study.get('slug', '')}",
                    "changefreq": "monthly",
                    "priority": "0.7",
                }
            )
    except Exception:
        pass  # Silently fail if case studies can't be loaded

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for page in pages:
        sitemap_xml += f"  <url>\n"
        sitemap_xml += f'    <loc>{base_url}{page["loc"]}</loc>\n'
        sitemap_xml += f"    <lastmod>{current_date}</lastmod>\n"
        sitemap_xml += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        sitemap_xml += f'    <priority>{page["priority"]}</priority>\n'
        sitemap_xml += f"  </url>\n"

    sitemap_xml += "</urlset>"

    return Response(content=sitemap_xml, media_type="application/xml")


@router.get("/robots.txt")
async def robots():
    """Generate robots.txt for search engines"""
    robots_txt = """User-agent: *
Allow: /

Sitemap: https://ishtar-ai.com/sitemap.xml
"""
    return Response(content=robots_txt, media_type="text/plain")


@router.get("/feed")
@router.get("/rss.xml")
async def rss_feed():
    """Generate RSS feed for blog posts"""
    posts = get_blog_posts_for_rss()
    rss_xml = generate_rss_feed(posts)
    return Response(content=rss_xml, media_type="application/rss+xml")
