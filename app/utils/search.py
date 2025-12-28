"""
Search Utility Module
Provides full-text search across blog posts, pages, case studies, resources, and FAQ
"""

from typing import List, Dict, Optional
import re


class SearchIndex:
    """Simple in-memory search index"""

    def __init__(self):
        self.index: List[Dict] = []

    def add_document(
        self,
        title: str,
        content: str,
        url: str,
        doc_type: str,
        excerpt: Optional[str] = None,
    ):
        """Add a document to the search index"""
        self.index.append(
            {
                "title": title,
                "content": content.lower(),
                "url": url,
                "type": doc_type,
                "excerpt": (
                    excerpt or content[:200] + "..." if len(content) > 200 else content
                ),
            }
        )

    def search(self, query: str, doc_types: Optional[List[str]] = None) -> List[Dict]:
        """
        Search the index for documents matching the query

        Args:
            query: Search query string
            doc_types: Optional list of document types to filter by

        Returns:
            List of matching documents with relevance scores
        """
        if not query or not query.strip():
            return []

        query_lower = query.lower().strip()
        query_terms = re.split(r"\s+", query_lower)

        results = []

        for doc in self.index:
            # Filter by document type if specified
            if doc_types and doc["type"] not in doc_types:
                continue

            # Calculate relevance score
            score = 0
            title_matches = 0
            content_matches = 0

            # Check title matches (higher weight)
            title_lower = doc["title"].lower()
            for term in query_terms:
                if term in title_lower:
                    title_matches += 1
                    score += 10  # Title matches are worth more

            # Check content matches
            content = doc["content"]
            for term in query_terms:
                # Count occurrences in content
                count = content.count(term)
                content_matches += count
                score += count * 2  # Content matches worth less

            # Exact phrase match bonus
            if query_lower in title_lower:
                score += 20
            if query_lower in content:
                score += 10

            # Only include documents with matches
            if score > 0:
                # Generate snippet with highlighted terms
                snippet = self._generate_snippet(
                    doc["content"], query_terms, doc.get("excerpt", "")
                )

                results.append(
                    {
                        "title": doc["title"],
                        "url": doc["url"],
                        "type": doc["type"],
                        "excerpt": snippet,
                        "score": score,
                        "title_matches": title_matches,
                        "content_matches": content_matches,
                    }
                )

        # Sort by score (descending)
        results.sort(key=lambda x: x["score"], reverse=True)

        return results

    def _generate_snippet(
        self,
        content: str,
        query_terms: List[str],
        fallback_excerpt: str,
        max_length: int = 200,
    ) -> str:
        """Generate a snippet with highlighted search terms"""
        if not content:
            return fallback_excerpt

        # Find the first occurrence of any query term
        first_match_pos = len(content)
        for term in query_terms:
            pos = content.find(term)
            if pos != -1 and pos < first_match_pos:
                first_match_pos = pos

        # Extract snippet around the match
        start = max(0, first_match_pos - 50)
        end = min(len(content), first_match_pos + max_length)

        snippet = content[start:end]

        # Highlight query terms
        for term in query_terms:
            snippet = re.sub(
                re.escape(term),
                lambda m: f"<mark>{m.group()}</mark>",
                snippet,
                flags=re.IGNORECASE,
            )

        # Add ellipsis if needed
        if start > 0:
            snippet = "..." + snippet
        if end < len(content):
            snippet = snippet + "..."

        return snippet


# Global search index instance
_search_index: Optional[SearchIndex] = None


def get_search_index() -> SearchIndex:
    """Get or create the global search index"""
    global _search_index
    if _search_index is None:
        _search_index = SearchIndex()
        _build_index(_search_index)
    return _search_index


def _build_index(index: SearchIndex):
    """Build the search index with all site content"""
    # Import here to avoid circular imports
    from app.routes.pages import get_blog_posts

    # Add blog posts
    try:
        blog_posts = get_blog_posts()
        for post in blog_posts:
            content = f"{post.get('title', '')} {post.get('excerpt', '')}"
            index.add_document(
                title=post.get("title", ""),
                content=content,
                url=f"/blog/{post.get('slug', '')}",
                doc_type="blog",
                excerpt=post.get("excerpt", ""),
            )
    except Exception:
        pass  # Silently fail if blog posts can't be loaded

    # Add static pages
    pages = [
        {
            "title": "Services",
            "content": "AI services RAG copilots agent automation LLMOps evaluation security synthetic media compliance",
            "url": "/services",
            "type": "page",
        },
        {
            "title": "Regulated Enterprise Solutions",
            "content": "Regulated enterprise RAG copilots policy research agent automation operations workflows governance audit trails evaluation",
            "url": "/finance",
            "type": "page",
        },
        {
            "title": "Media & Advertising",
            "content": "Media advertising synthetic media compliance brand safety provenance disclosure workflows agentic content operations review approval",
            "url": "/media-ads",
            "type": "page",
        },
        {
            "title": "Pricing",
            "content": "Pricing GenAI Launch Sprint RAG Copilot Agent Automation LLMOps Security Hardening Platform Partner",
            "url": "/pricing",
            "type": "page",
        },
        {
            "title": "Contact",
            "content": "Contact consultation schedule Calendly message",
            "url": "/contact",
            "type": "page",
        },
        {
            "title": "FAQ",
            "content": "Frequently asked questions industries implementation timeline pricing support",
            "url": "/faq",
            "type": "page",
        },
    ]

    for page in pages:
        index.add_document(
            title=page["title"],
            content=page["content"],
            url=page["url"],
            doc_type=page["type"],
        )

    # Add FAQ entries (basic ones)
    faqs = [
        {
            "title": "What industries do you serve?",
            "content": "We specialize in regulated enterprises and media/advertising organizations",
            "url": "/faq#industries",
            "type": "faq",
        },
        {
            "title": "How long does a typical implementation take?",
            "content": "Implementation timelines vary based on project scope",
            "url": "/faq#timeline",
            "type": "faq",
        },
    ]

    for faq in faqs:
        index.add_document(
            title=faq["title"],
            content=faq["content"],
            url=faq["url"],
            doc_type=faq["type"],
        )

    # Add case studies
    try:
        from app.content.case_studies import get_case_studies

        case_studies = get_case_studies()
        for case_study in case_studies:
            content = f"{case_study.get('title', '')} {case_study.get('challenge', '')} {case_study.get('solution', '')} {case_study.get('results', '')}"
            index.add_document(
                title=case_study.get("title", ""),
                content=content,
                url=f"/case-studies/{case_study.get('slug', '')}",
                doc_type="case_study",
                excerpt=case_study.get("challenge", "")[:200],
            )
    except Exception:
        pass

    # Add resources
    try:
        from app.content.resources import get_resources

        resources = get_resources()
        for resource in resources:
            content = f"{resource.get('title', '')} {resource.get('description', '')}"
            index.add_document(
                title=resource.get("title", ""),
                content=content,
                url=f"/resources?category={resource.get('category', '')}",
                doc_type="resource",
                excerpt=resource.get("description", ""),
            )
    except Exception:
        pass


def search(
    query: str, doc_types: Optional[List[str]] = None, limit: int = 20
) -> List[Dict]:
    """
    Search across all indexed content

    Args:
        query: Search query string
        doc_types: Optional list of document types to filter by (blog, page, faq, resource, case_study)
        limit: Maximum number of results to return

    Returns:
        List of search results
    """
    index = get_search_index()
    results = index.search(query, doc_types)
    return results[:limit]
