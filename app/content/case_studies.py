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
            "client": "Top-10 US Bank (Asset Management Division)",
            "challenge": "The client needed to streamline compliance research and policy lookup across multiple regulatory frameworks. Manual processes were time-consuming and error-prone, with compliance officers spending 60% of their time on research tasks.",
            "solution": "We implemented a RAG copilot system that integrated with their existing knowledge base, providing instant access to compliance information with proper citations and evidence trails. The system included permission-aware retrieval, audit logging, and evaluation baselines.",
            "results": "Reduced compliance research time by 75%, improved accuracy of policy interpretations, and enabled real-time compliance checks.",
            "metrics": {
                "time_saved": "75%",
                "accuracy_improvement": "40%",
                "adoption_rate": "90%",
                "measurement_period": "12 weeks post-deployment",
                "methodology": "Before/after time tracking and accuracy audits",
            },
            "timeline": {
                "kickoff": "Week 1",
                "architecture_review": "Week 2",
                "build_complete": "Week 6",
                "pilot_deployment": "Week 7",
                "production_rollout": "Week 8",
                "total_duration": "8 weeks",
            },
            "architecture": {
                "components": [
                    "Vector database (Pinecone)",
                    "LLM API (OpenAI)",
                    "Permission engine",
                    "Audit logging system",
                    "Evaluation pipeline",
                ],
                "integrations": [
                    "SharePoint knowledge base",
                    "Active Directory",
                    "Compliance management system",
                ],
                "diagram": "/static/img/case-study-placeholder.jpg",
            },
            "risk_controls": {
                "audit_trails": "Complete audit logging of all queries and responses",
                "permissions": "RBAC with source-level entitlements",
                "evaluation": "Automated groundedness and citation accuracy testing",
                "compliance": "FINRA and SEC record-keeping compliance",
            },
            "artifacts": {
                "screenshots": ["/static/img/case-study-placeholder.jpg"],
                "sample_outputs": "Example compliance memo with citations",
                "documents": [],
            },
            "image": "/static/img/case-study-placeholder.jpg",
        },
        {
            "title": "Agent Automation for Media Content Operations",
            "slug": "agent-automation-media-content",
            "industry": "Media",
            "client": "Global Media Network",
            "challenge": "Content review and approval workflows were manual and slow, creating bottlenecks in content production pipelines. Content teams spent 40% of their time on review and approval tasks.",
            "solution": "We built an agentic automation system with human-in-the-loop checkpoints, automated content review, and intelligent routing for approval workflows. The system included brand safety checks, provenance tracking, and disclosure workflows.",
            "results": "Accelerated content production by 60%, reduced manual review time, and improved content quality through automated checks.",
            "metrics": {
                "production_speed": "60% faster",
                "review_time": "50% reduction",
                "content_quality": "25% improvement",
                "measurement_period": "16 weeks post-deployment",
                "methodology": "Production metrics tracking and quality audits",
            },
            "timeline": {
                "kickoff": "Week 1",
                "architecture_review": "Week 2",
                "build_complete": "Week 9",
                "pilot_deployment": "Week 10",
                "production_rollout": "Week 12",
                "total_duration": "12 weeks",
            },
            "architecture": {
                "components": [
                    "Agent orchestration engine",
                    "Content review API",
                    "Approval workflow system",
                    "Brand safety checker",
                    "Provenance tracker",
                ],
                "integrations": [
                    "Content management system",
                    "Slack notifications",
                    "Approval queue dashboard",
                ],
                "diagram": "/static/img/case-study-placeholder.jpg",
            },
            "risk_controls": {
                "audit_trails": "Complete audit logging of all content decisions",
                "permissions": "Role-based approval workflows",
                "evaluation": "Automated brand safety and quality scoring",
                "compliance": "Synthetic media disclosure compliance",
            },
            "artifacts": {
                "screenshots": ["/static/img/case-study-placeholder.jpg"],
                "sample_outputs": "Example approval workflow dashboard",
                "documents": [],
            },
            "image": "/static/img/case-study-placeholder.jpg",
        },
        {
            "title": "LLMOps Foundation for Enterprise AI Platform",
            "slug": "llmops-enterprise-platform",
            "industry": "Finance",
            "client": "Fortune 500 Financial Services",
            "challenge": "Multiple AI applications lacked centralized monitoring, evaluation, and governance, making it difficult to ensure reliability and compliance. Incidents were frequent and deployments were slow due to manual processes.",
            "solution": "We established a comprehensive LLMOps foundation with evaluation pipelines, monitoring, versioning, and CI/CD gating for all AI applications. The platform included automated regression testing, prompt/model versioning, and rollback capabilities.",
            "results": "Achieved 99.9% uptime, reduced incidents by 80%, and enabled rapid iteration with confidence in production deployments.",
            "metrics": {
                "uptime": "99.9%",
                "incident_reduction": "80%",
                "deployment_speed": "3x faster",
                "measurement_period": "6 months post-deployment",
                "methodology": "Platform monitoring and incident tracking",
            },
            "timeline": {
                "kickoff": "Week 1",
                "architecture_review": "Week 2",
                "build_complete": "Week 6",
                "pilot_deployment": "Week 7",
                "production_rollout": "Week 8",
                "total_duration": "8 weeks",
            },
            "architecture": {
                "components": [
                    "Evaluation pipeline",
                    "Monitoring dashboard",
                    "Version control system",
                    "CI/CD gates",
                    "Rollback system",
                ],
                "integrations": [
                    "GitHub Actions",
                    "Datadog",
                    "Slack alerts",
                    "All AI applications",
                ],
                "diagram": "/static/img/case-study-placeholder.jpg",
            },
            "risk_controls": {
                "audit_trails": "Complete audit logging of all deployments and changes",
                "permissions": "RBAC for deployment approvals",
                "evaluation": "Automated regression testing before deployments",
                "compliance": "SOC 2-aligned controls and auditability",
            },
            "artifacts": {
                "screenshots": ["/static/img/case-study-placeholder.jpg"],
                "sample_outputs": "Example evaluation report and monitoring dashboard",
                "documents": [],
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
