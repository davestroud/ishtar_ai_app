"""
Case Studies Content Module
Contains case study data
"""

from typing import List, Dict


def get_case_studies() -> List[Dict]:
    """Get list of case studies"""
    return [
        {
            "title": "RAG Copilot Implementation for Financial Compliance",
            "slug": "rag-copilot-financial-compliance",
            "industry": "Finance",
            "client": "Major Financial Institution",
            "challenge": "The client needed to streamline compliance research and policy lookup across multiple regulatory frameworks. Manual processes were time-consuming and error-prone.",
            "solution": "We implemented a RAG copilot system that integrated with their existing knowledge base, providing instant access to compliance information with proper citations and evidence trails.",
            "results": "Reduced compliance research time by 75%, improved accuracy of policy interpretations, and enabled real-time compliance checks.",
            "metrics": {
                "time_saved": "75%",
                "accuracy_improvement": "40%",
                "adoption_rate": "90%",
            },
            "image": "/static/img/case-study-placeholder.jpg",
        },
        {
            "title": "Agent Automation for Media Content Operations",
            "slug": "agent-automation-media-content",
            "industry": "Media",
            "client": "Leading Media Company",
            "challenge": "Content review and approval workflows were manual and slow, creating bottlenecks in content production pipelines.",
            "solution": "We built an agentic automation system with human-in-the-loop checkpoints, automated content review, and intelligent routing for approval workflows.",
            "results": "Accelerated content production by 60%, reduced manual review time, and improved content quality through automated checks.",
            "metrics": {
                "production_speed": "60% faster",
                "review_time": "50% reduction",
                "content_quality": "25% improvement",
            },
            "image": "/static/img/case-study-placeholder.jpg",
        },
        {
            "title": "LLMOps Foundation for Enterprise AI Platform",
            "slug": "llmops-enterprise-platform",
            "industry": "Finance",
            "client": "Fortune 500 Financial Services",
            "challenge": "Multiple AI applications lacked centralized monitoring, evaluation, and governance, making it difficult to ensure reliability and compliance.",
            "solution": "We established a comprehensive LLMOps foundation with evaluation pipelines, monitoring, versioning, and CI/CD gating for all AI applications.",
            "results": "Achieved 99.9% uptime, reduced incidents by 80%, and enabled rapid iteration with confidence in production deployments.",
            "metrics": {
                "uptime": "99.9%",
                "incident_reduction": "80%",
                "deployment_speed": "3x faster",
            },
            "image": "/static/img/case-study-placeholder.jpg",
        },
    ]


def get_case_study_by_slug(slug: str) -> Dict:
    """Get a specific case study by slug"""
    case_studies = get_case_studies()
    for case_study in case_studies:
        if case_study.get("slug") == slug:
            return case_study
    return None
