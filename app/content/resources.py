"""
Resources Content Module
Contains resource data for downloads section
"""

from typing import List, Dict


def get_resources() -> List[Dict]:
    """Get list of available resources"""
    return [
        {
            "title": "RAG Copilots: A Complete Guide for Financial Services",
            "type": "whitepaper",
            "description": "Comprehensive guide to implementing RAG copilots in financial services, covering architecture, compliance, and best practices.",
            "file_path": "/static/resources/rag-copilots-guide.pdf",
            "category": "Whitepapers",
            "gated": True,
            "download_count": 0,
        },
        {
            "title": "AI Governance Framework Template",
            "type": "template",
            "description": "Ready-to-use template for establishing AI governance frameworks in your organization.",
            "file_path": "/static/resources/ai-governance-template.docx",
            "category": "Templates",
            "gated": False,
            "download_count": 0,
        },
        {
            "title": "Synthetic Media Compliance Checklist",
            "type": "guide",
            "description": "Essential checklist for ensuring compliance when using AI-generated media content.",
            "file_path": "/static/resources/synthetic-media-checklist.pdf",
            "category": "Guides",
            "gated": True,
            "download_count": 0,
        },
        {
            "title": "LLMOps Best Practices Guide",
            "type": "guide",
            "description": "Best practices for implementing LLMOps pipelines, monitoring, and evaluation systems.",
            "file_path": "/static/resources/llmops-best-practices.pdf",
            "category": "Guides",
            "gated": True,
            "download_count": 0,
        },
        {
            "title": "Agent Automation ROI Calculator",
            "type": "tool",
            "description": "Interactive calculator to estimate ROI from agent automation implementations.",
            "file_path": "/static/resources/agent-automation-calculator.xlsx",
            "category": "Tools",
            "gated": False,
            "download_count": 0,
        },
    ]


def get_resource_categories() -> List[str]:
    """Get list of resource categories"""
    return ["All", "Whitepapers", "Guides", "Templates", "Tools"]
