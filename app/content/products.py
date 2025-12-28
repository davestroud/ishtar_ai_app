"""
Products Content Module
Contains product information and details
"""

from typing import Dict, Optional


def get_product_by_slug(slug: str) -> Optional[Dict]:
    """Get a specific product by slug"""
    products = {
        "rag-copilots": {
            "title": "RAG Copilots",
            "slug": "rag-copilots",
            "subtitle": "Enterprise Knowledge Products",
            "description": "Production-ready RAG copilots that provide instant access to your knowledge base with proper citations, evidence trails, and permission-aware retrieval.",
            "outcomes": [
                "Instant access to compliance policies, research documents, and knowledge bases with citations",
                "60-75% reduction in research time for compliance officers and researchers",
                "Evidence-native workflows that provide audit trails for every claim",
            ],
            "target_users": [
                "Compliance Officers",
                "Research Analysts",
                "Operations Teams",
                "Legal Teams",
            ],
            "evidence_approach": {
                "title": "Evidence & Citations Approach",
                "description": "Every response includes source citations with claim→evidence mapping. Users can verify every claim against source documents, ensuring accuracy and compliance.",
                "features": [
                    "Automatic citation generation for all claims",
                    "Source document links and excerpts",
                    "Confidence scores for each citation",
                    "Claim-to-evidence mapping visualization",
                ],
            },
            "permissioning": {
                "title": "Permissioning Model",
                "description": "Multi-layered access control ensures users only see information they're authorized to access.",
                "features": [
                    "Role-Based Access Control (RBAC) with custom roles",
                    "Source-level entitlements (document-level permissions)",
                    "Attribute-Based Access Control (ABAC) support",
                    "Integration with enterprise identity systems (SSO, Active Directory)",
                ],
            },
            "evaluation": {
                "title": "Evaluation Framework",
                "description": "Comprehensive evaluation ensures responses are accurate, grounded, and appropriate.",
                "metrics": [
                    "Groundedness: Response accuracy against source documents",
                    "Citation Accuracy: Citations match the claims made",
                    "Refusal Behavior: Appropriate refusal of out-of-scope requests",
                    "Response Quality: Relevance and completeness",
                ],
            },
            "deployment": {
                "patterns": [
                    "SaaS: Fully managed cloud deployment with tenant isolation",
                    "VPC: Dedicated infrastructure in your cloud environment",
                    "On-Premise: Containerized deployment in your data center",
                ],
                "integrations": [
                    "SharePoint, Confluence, and other knowledge bases",
                    "Active Directory and SSO providers",
                    "Existing compliance and document management systems",
                ],
            },
            "deliverables": {
                "title": "What You Get in 6-7 Weeks",
                "items": [
                    "Ingestion pipeline for your knowledge base",
                    "Vector database with metadata strategy",
                    "Permission-aware retrieval system",
                    "Citation generation and evidence mapping",
                    "Evaluation baseline and testing framework",
                    "Deployment-ready system with monitoring",
                    "Documentation and runbooks",
                    "Executive demo and handoff",
                ],
            },
            "pricing": {
                "range": "$85k–$135k",
                "duration": "6–7 weeks",
                "link": "/pricing",
            },
            "cta": {
                "primary": "Request Demo",
                "primary_link": "/demo",
                "secondary": "View Pricing",
                "secondary_link": "/pricing",
            },
        },
        "agent-automation": {
            "title": "Agent Automation",
            "slug": "agent-automation",
            "subtitle": "Operational AI Systems",
            "description": "End-to-end workflow automation with human-in-the-loop checkpoints, auditability, and intelligent decision-making.",
            "outcomes": [
                "Automate complex workflows end-to-end with AI agents",
                "60-80% reduction in manual processing time",
                "Complete audit trails for compliance and governance",
            ],
            "target_users": [
                "Operations Teams",
                "Content Operations",
                "Compliance Officers",
                "Process Owners",
            ],
            "evidence_approach": {
                "title": "Tool Calling & Decision Making",
                "description": "Agents make decisions using tool calling with full transparency and auditability.",
                "features": [
                    "Tool calling with function definitions",
                    "Decision reasoning logs",
                    "Approval workflows for critical decisions",
                    "Rollback capabilities",
                ],
            },
            "permissioning": {
                "title": "Access Controls",
                "description": "Granular permissions control what agents can do and what data they can access.",
                "features": [
                    "Role-based agent permissions",
                    "Tool-level access control",
                    "Data access restrictions",
                    "Approval workflow permissions",
                ],
            },
            "evaluation": {
                "title": "Evaluation Framework",
                "description": "Comprehensive evaluation ensures agents operate correctly and safely.",
                "metrics": [
                    "Task Completion Rate: Percentage of tasks completed successfully",
                    "Error Rate: Frequency of errors and failures",
                    "Human Intervention Rate: Frequency of HITL checkpoints",
                    "Audit Compliance: Completeness of audit trails",
                ],
            },
            "deployment": {
                "patterns": [
                    "SaaS: Managed agent orchestration platform",
                    "VPC: Dedicated infrastructure with your tools",
                    "Hybrid: Agents in cloud, tools on-premise",
                ],
                "integrations": [
                    "Slack, Microsoft Teams for notifications",
                    "Approval queue dashboards",
                    "Existing workflow and process systems",
                    "Content management systems",
                ],
            },
            "deliverables": {
                "title": "What You Get in 7-9 Weeks",
                "items": [
                    "Agent orchestration engine",
                    "Tool calling framework",
                    "Human-in-the-loop checkpoints",
                    "Retry and recovery mechanisms",
                    "Audit logging system",
                    "Deployment playbook",
                    "Monitoring and alerting",
                    "Documentation and training",
                ],
            },
            "pricing": {
                "range": "$120k–$200k",
                "duration": "7–9 weeks",
                "link": "/pricing",
            },
            "cta": {
                "primary": "Request Demo",
                "primary_link": "/demo",
                "secondary": "View Pricing",
                "secondary_link": "/pricing",
            },
        },
        "llmops-foundation": {
            "title": "LLMOps Foundation",
            "slug": "llmops-foundation",
            "subtitle": "AI Platform Backbone",
            "description": "Evaluation, monitoring, release gates, and governance—so your GenAI system stays reliable.",
            "outcomes": [
                "99.9% uptime with automated monitoring and alerting",
                "80% reduction in incidents through evaluation gates",
                "3x faster deployments with confidence",
            ],
            "target_users": [
                "AI Platform Teams",
                "ML Engineers",
                "DevOps Teams",
                "AI Governance Teams",
            ],
            "evidence_approach": {
                "title": "Evaluation Pipelines",
                "description": "Automated evaluation pipelines ensure quality before deployment.",
                "features": [
                    "Automated regression testing",
                    "Baseline comparison for model updates",
                    "Custom evaluation metrics",
                    "CI/CD integration",
                ],
            },
            "permissioning": {
                "title": "Access Controls",
                "description": "Role-based access for deployment, monitoring, and configuration.",
                "features": [
                    "Deployment approval workflows",
                    "Monitoring dashboard access control",
                    "Configuration change permissions",
                    "Audit log access",
                ],
            },
            "evaluation": {
                "title": "Evaluation Framework",
                "description": "Comprehensive evaluation ensures reliability and quality.",
                "metrics": [
                    "Performance Metrics: Latency, throughput, error rates",
                    "Quality Metrics: Accuracy, relevance, completeness",
                    "Cost Metrics: Token usage, API costs",
                    "Reliability Metrics: Uptime, availability",
                ],
            },
            "deployment": {
                "patterns": [
                    "SaaS: Managed LLMOps platform",
                    "Self-Hosted: Deploy in your infrastructure",
                    "Hybrid: Mix of managed and self-hosted components",
                ],
                "integrations": [
                    "GitHub Actions, GitLab CI/CD",
                    "Datadog, New Relic, Prometheus",
                    "Slack, PagerDuty for alerts",
                    "All AI applications",
                ],
            },
            "deliverables": {
                "title": "What You Get in 4-6 Weeks",
                "items": [
                    "Evaluation pipelines",
                    "Tracing and observability",
                    "Prompt and model versioning",
                    "CI/CD gating",
                    "Rollback strategy",
                    "Monitoring dashboards",
                    "Alerting configuration",
                    "Documentation and runbooks",
                ],
            },
            "pricing": {
                "range": "$75k–$125k",
                "duration": "4–6 weeks",
                "link": "/pricing",
            },
            "cta": {
                "primary": "Request Demo",
                "primary_link": "/demo",
                "secondary": "View Pricing",
                "secondary_link": "/pricing",
            },
        },
        "genai-security": {
            "title": "GenAI Security Hardening",
            "slug": "genai-security",
            "subtitle": "Enterprise Readiness Audit",
            "description": "Red-team, guardrails, leakage checks, and an exec-ready risk report.",
            "outcomes": [
                "Comprehensive security assessment of your GenAI systems",
                "Identified vulnerabilities and remediation roadmap",
                "Executive-ready risk report for stakeholders",
            ],
            "target_users": [
                "Security Teams",
                "AI Governance Teams",
                "Risk Management",
                "Executive Leadership",
            ],
            "evidence_approach": {
                "title": "Security Testing",
                "description": "Comprehensive security testing identifies vulnerabilities and risks.",
                "features": [
                    "Red-team penetration testing",
                    "Prompt injection testing",
                    "Data leakage assessment",
                    "Adversarial testing",
                ],
            },
            "permissioning": {
                "title": "Security Controls",
                "description": "Assessment of access controls and security measures.",
                "features": [
                    "Access control review",
                    "Authentication and authorization assessment",
                    "Data access pattern analysis",
                    "Privilege escalation testing",
                ],
            },
            "evaluation": {
                "title": "Risk Assessment",
                "description": "Comprehensive risk assessment across multiple dimensions.",
                "metrics": [
                    "Vulnerability Count: Number of identified vulnerabilities",
                    "Risk Score: Overall risk rating",
                    "Compliance Gap: Gaps in security compliance",
                    "Remediation Priority: Prioritized remediation roadmap",
                ],
            },
            "deployment": {
                "patterns": [
                    "Assessment: On-site or remote security assessment",
                    "Remediation: Implementation of security controls",
                    "Ongoing: Continuous security monitoring",
                ],
                "integrations": [
                    "Security information and event management (SIEM)",
                    "Vulnerability management systems",
                    "Compliance frameworks",
                    "Risk management platforms",
                ],
            },
            "deliverables": {
                "title": "What You Get in 3-4 Weeks",
                "items": [
                    "Security assessment report",
                    "Vulnerability findings and remediation roadmap",
                    "Guardrails implementation",
                    "OWASP-aligned testing results",
                    "Policy enforcement recommendations",
                    "Security documentation",
                    "Executive risk report",
                    "Remediation support",
                ],
            },
            "pricing": {
                "range": "$50k–$85k",
                "duration": "3–4 weeks",
                "link": "/pricing",
            },
            "cta": {
                "primary": "Request Assessment",
                "primary_link": "/contact",
                "secondary": "View Pricing",
                "secondary_link": "/pricing",
            },
        },
        "synthetic-media-compliance": {
            "title": "Synthetic Media Compliance",
            "slug": "synthetic-media-compliance",
            "subtitle": "NY/Ads-Focused Controls",
            "description": "Disclosure workflows, audit trails, and compliance-ready enforcement logic for AI media.",
            "outcomes": [
                "Automated disclosure workflows for AI-generated content",
                "Complete audit trails for compliance",
                "Brand safety and provenance tracking",
            ],
            "target_users": [
                "Media Companies",
                "Advertising Agencies",
                "Content Operations",
                "Compliance Teams",
            ],
            "evidence_approach": {
                "title": "Provenance & Disclosure",
                "description": "Complete tracking of AI-generated content with disclosure workflows.",
                "features": [
                    "Automatic provenance tracking",
                    "Disclosure workflow automation",
                    "Content labeling and tagging",
                    "Audit trail generation",
                ],
            },
            "permissioning": {
                "title": "Access Controls",
                "description": "Role-based access for content review and approval.",
                "features": [
                    "Content review permissions",
                    "Approval workflow roles",
                    "Disclosure override permissions",
                    "Audit log access",
                ],
            },
            "evaluation": {
                "title": "Compliance Evaluation",
                "description": "Evaluation ensures compliance with disclosure requirements.",
                "metrics": [
                    "Disclosure Compliance Rate: Percentage of content properly disclosed",
                    "Audit Trail Completeness: Completeness of audit records",
                    "Brand Safety Score: Brand safety assessment",
                    "Provenance Accuracy: Accuracy of provenance tracking",
                ],
            },
            "deployment": {
                "patterns": [
                    "SaaS: Managed compliance platform",
                    "API Integration: Integrate with existing content systems",
                    "On-Premise: Deploy in your infrastructure",
                ],
                "integrations": [
                    "Content management systems",
                    "Advertising platforms",
                    "Social media platforms",
                    "Compliance management systems",
                ],
            },
            "deliverables": {
                "title": "What You Get in 3-5 Weeks",
                "items": [
                    "Disclosure logic implementation",
                    "Provenance workflow",
                    "Policy mapping and enforcement",
                    "Auditability framework",
                    "Brand safety checks",
                    "Integration with content systems",
                    "Compliance documentation",
                    "Training and support",
                ],
            },
            "pricing": {
                "range": "$65k–$110k",
                "duration": "3–5 weeks",
                "link": "/pricing",
            },
            "cta": {
                "primary": "Request Demo",
                "primary_link": "/demo",
                "secondary": "View Pricing",
                "secondary_link": "/pricing",
            },
        },
    }
    return products.get(slug)
