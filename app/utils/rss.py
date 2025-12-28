"""
RSS Feed Generator Utility
Generates RSS 2.0 compliant feeds for blog posts
"""

from datetime import datetime
from typing import List, Dict
from xml.etree import ElementTree as ET
from xml.dom import minidom


def generate_rss_feed(
    posts: List[Dict], site_url: str = "https://ishtar-ai.com"
) -> str:
    """
    Generate RSS 2.0 compliant XML feed from blog posts

    Args:
        posts: List of dictionaries containing post data:
            - title: Post title
            - slug: Post slug/URL
            - description: Post description/excerpt
            - published_date: datetime object or ISO string
            - author: Author name (optional)
            - categories: List of categories/tags (optional)
        site_url: Base URL of the site

    Returns:
        RSS XML string
    """
    # Create root element
    rss = ET.Element("rss", version="2.0")
    rss.set("xmlns:atom", "http://www.w3.org/2005/Atom")
    rss.set("xmlns:content", "http://purl.org/rss/1.0/modules/content/")

    channel = ET.SubElement(rss, "channel")

    # Channel metadata
    ET.SubElement(channel, "title").text = "Ishtar AI Blog"
    ET.SubElement(channel, "link").text = f"{site_url}/blog"
    ET.SubElement(channel, "description").text = (
        "AI solutions for finance and media industries. Latest insights on RAG copilots, agent automation, LLMOps, and AI security."
    )
    ET.SubElement(channel, "language").text = "en-US"
    ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    ET.SubElement(channel, "generator").text = "Ishtar AI FastAPI"

    # Atom self-link
    atom_link = ET.SubElement(channel, "atom:link")
    atom_link.set("href", f"{site_url}/feed")
    atom_link.set("rel", "self")
    atom_link.set("type", "application/rss+xml")

    # Add items for each post
    for post in posts:
        item = ET.SubElement(channel, "item")

        ET.SubElement(item, "title").text = post.get("title", "")
        ET.SubElement(item, "link").text = f"{site_url}/blog/{post.get('slug', '')}"
        ET.SubElement(item, "guid", isPermaLink="true").text = (
            f"{site_url}/blog/{post.get('slug', '')}"
        )

        # Description
        description = ET.SubElement(item, "description")
        description.text = post.get("description", "")

        # Published date
        pub_date = post.get("published_date")
        if pub_date:
            if isinstance(pub_date, str):
                # Try to parse ISO string
                try:
                    pub_date = datetime.fromisoformat(pub_date.replace("Z", "+00:00"))
                except:
                    pub_date = datetime.utcnow()
            elif isinstance(pub_date, datetime):
                pass
            else:
                pub_date = datetime.utcnow()

            ET.SubElement(item, "pubDate").text = pub_date.strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            )
        else:
            ET.SubElement(item, "pubDate").text = datetime.utcnow().strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            )

        # Author
        author = post.get("author")
        if author:
            ET.SubElement(item, "author").text = f"{author} ({site_url})"

        # Categories
        categories = post.get("categories", [])
        if isinstance(categories, str):
            categories = [categories]
        for category in categories:
            ET.SubElement(item, "category").text = category

    # Convert to string with pretty formatting
    rough_string = ET.tostring(rss, encoding="unicode")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
