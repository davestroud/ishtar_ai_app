from fastapi import APIRouter
from fastapi.responses import Response
from datetime import datetime

router = APIRouter()


@router.get("/sitemap.xml")
async def sitemap():
    """Generate sitemap.xml for search engines"""
    base_url = "https://ishtar-ai.com"
    current_date = datetime.now().strftime("%Y-%m-%d")

    pages = [
        {"loc": "/", "changefreq": "weekly", "priority": "1.0"},
        {"loc": "/services", "changefreq": "monthly", "priority": "0.9"},
        {"loc": "/finance", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/media-ads", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/contact", "changefreq": "monthly", "priority": "0.7"},
        {"loc": "/privacy", "changefreq": "yearly", "priority": "0.3"},
        {"loc": "/terms", "changefreq": "yearly", "priority": "0.3"},
    ]

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
