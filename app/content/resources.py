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
            "estimated_time": "45 minutes",
            "target_audience": "Compliance Officers, Research Analysts, AI Platform Teams",
            "table_of_contents": [
                "Introduction to RAG Copilots",
                "Architecture and Design Patterns",
                "Compliance and Security Considerations",
                "Implementation Best Practices",
                "Evaluation and Monitoring",
                "Case Studies"
            ],
            "key_takeaways": [
                "How to design RAG systems for financial services",
                "Compliance requirements and how to meet them",
                "Best practices for evaluation and monitoring"
            ]
        },
        {
            "title": "AI Governance Framework Template",
            "type": "template",
            "description": "Ready-to-use template for establishing AI governance frameworks in your organization.",
            "file_path": "/static/resources/ai-governance-template.docx",
            "category": "Templates",
            "gated": False,
            "download_count": 0,
            "estimated_time": "30 minutes",
            "target_audience": "AI Governance Teams, Risk Management, Executive Leadership",
            "table_of_contents": [
                "Governance Structure",
                "Policy Templates",
                "Risk Assessment Framework",
                "Evaluation Criteria",
                "Compliance Checklist"
            ],
            "key_takeaways": [
                "Ready-to-use governance framework",
                "Policy templates for AI systems",
                "Risk assessment methodology"
            ]
        },
        {
            "title": "Synthetic Media Compliance Checklist",
            "type": "guide",
            "description": "Essential checklist for ensuring compliance when using AI-generated media content.",
            "file_path": "/static/resources/synthetic-media-checklist.pdf",
            "category": "Guides",
            "gated": True,
            "download_count": 0,
            "estimated_time": "20 minutes",
            "target_audience": "Media Companies, Advertising Agencies, Content Operations",
            "table_of_contents": [
                "Disclosure Requirements",
                "Provenance Tracking",
                "Brand Safety Checks",
                "Compliance Checklist",
                "Best Practices"
            ],
            "key_takeaways": [
                "Complete compliance checklist",
                "Disclosure workflow guidance",
                "Brand safety considerations"
            ]
        },
        {
            "title": "LLMOps Best Practices Guide",
            "type": "guide",
            "description": "Best practices for implementing LLMOps pipelines, monitoring, and evaluation systems.",
            "file_path": "/static/resources/llmops-best-practices.pdf",
            "category": "Guides",
            "gated": True,
            "download_count": 0,
            "estimated_time": "35 minutes",
            "target_audience": "ML Engineers, DevOps Teams, AI Platform Teams",
            "table_of_contents": [
                "LLMOps Fundamentals",
                "Evaluation Pipelines",
                "Monitoring and Alerting",
                "Version Control",
                "CI/CD Integration",
                "Best Practices"
            ],
            "key_takeaways": [
                "How to build evaluation pipelines",
                "Monitoring and alerting strategies",
                "CI/CD integration patterns"
            ]
        },
        {
            "title": "Agent Automation ROI Calculator",
            "type": "tool",
            "description": "Interactive calculator to estimate ROI from agent automation implementations.",
            "file_path": "/static/resources/agent-automation-calculator.xlsx",
            "category": "Tools",
            "gated": False,
            "download_count": 0,
            "estimated_time": "15 minutes",
            "target_audience": "Operations Teams, Finance Teams, Process Owners",
            "table_of_contents": [
                "Input Parameters",
                "Cost Calculations",
                "Time Savings Analysis",
                "ROI Projections"
            ],
            "key_takeaways": [
                "Estimate automation ROI",
                "Calculate time and cost savings",
                "Build business case for automation"
            ]
        },
    ]


def get_resource_categories() -> List[str]:
    """Get list of resource categories"""
    return ["All", "Whitepapers", "Guides", "Templates", "Tools"]
