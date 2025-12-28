from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

from app.config import settings

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def get_rag_copilots_article_content():
    """Get the full RAG Copilots article content"""
    return """<p>Financial services didn't fall in love with generative AI because it writes fluent paragraphs. It fell in love with the <em>idea</em> of compressing the time between "question asked" and "decision defended."</p>

<p>But finance also has an allergy to ungrounded prose. A model that "sounds right" is not a model you can supervise, audit, or explain under pressure.</p>

<p>That's why the future doesn't look like a free-form chatbot bolted onto a document drive. It looks like <strong>RAG copilots</strong>: systems that treat enterprise knowledge as the primary source of truth, and treat the LLM as a reasoning-and-language layer constrained by retrieval, policy, and evidence.</p>

<p>At <strong>Ishtar AI</strong>, we think the winners in this space will build copilots that are:</p>

<ul>
<li><strong>Evidence-first</strong> (every answer is attributable),</li>
<li><strong>Policy-aware</strong> (access, jurisdiction, and confidentiality are enforced before generation),</li>
<li><strong>Auditable by design</strong> (traceability is a product feature, not an afterthought),</li>
<li><strong>Measurable</strong> (quality is evaluated like a risk model, not a demo).</li>
</ul>

<p>Below is a technical view of where RAG copilots are going in finance—especially for <strong>compliance</strong> and <strong>research</strong>—and what best practices separate pilots from production systems.</p>

<hr>

<h2>Why finance needs RAG, not "just an LLM"</h2>

<p>A base LLM is fundamentally a probabilistic text generator trained on broad patterns. In finance, that creates immediate friction:</p>

<ul>
<li><strong>Supervision and recordkeeping:</strong> You don't just need an answer—you need <em>what it was based on</em>, who was allowed to see it, and what version of the truth existed at that time.</li>
<li><strong>Non-public information boundaries:</strong> "Helpful" can become "harmful" if retrieval crosses Chinese walls or leaks MNPI.</li>
<li><strong>Regulatory defensibility:</strong> A compliance decision that can't cite underlying policy language, procedures, communications, or evidence is fragile.</li>
<li><strong>Operational risk:</strong> Hallucinations aren't just incorrect—they are <em>uncontrolled statements</em> that can propagate into downstream memos, client comms, and filings.</li>
</ul>

<p><strong>RAG (Retrieval-Augmented Generation)</strong> changes the center of gravity. Instead of asking a model to invent, you ask it to <em>retrieve</em> from approved corpora, then <em>compose</em> a response that is explicitly grounded.</p>

<p>The future RAG copilot is not "ChatGPT with a vector database." It is an <strong>evidence compiler</strong> with a language interface.</p>

<hr>

<h2>What a "RAG copilot" actually is (and what it isn't)</h2>

<p>A production-grade RAG copilot has two planes:</p>

<ul>
<li><strong>Data plane:</strong> ingestion, chunking, embeddings, indexing, retrieval, citation, and provenance tracking</li>
<li><strong>Control plane:</strong> identity, entitlement enforcement, policy gating, audit logging, evaluation, and supervisory workflows</li>
</ul>

<p>It is <em>not</em> a system that:</p>

<ul>
<li>dumps top‑K retrieved chunks into a prompt and hopes for the best,</li>
<li>treats citations as decoration,</li>
<li>ignores access control in retrieval,</li>
<li>lacks measurement beyond "users like it."</li>
</ul>

<p>A finance-grade copilot behaves more like a cautious analyst: it cites, it abstains, it flags uncertainty, it respects boundaries, and it leaves a paper trail.</p>

<hr>

<h2>Visual 1 — Reference architecture for a finance-grade RAG copilot</h2>

<p>Below is a reference architecture that reflects what actually matters in financial services: provenance, policy, and observability.</p>

<div class="diagram-container">
<svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: white; border: 1px solid #e2e8f0; border-radius: 8px;">
  <!-- Title -->
  <text x="600" y="30" text-anchor="middle" font-family="Inter, sans-serif" font-size="18" font-weight="600" fill="#1e3a8a">Finance-Grade RAG Copilot Architecture</text>
  
  <!-- User -->
  <rect x="50" y="80" width="140" height="60" rx="5" fill="#1e3a8a" stroke="#1e40af" stroke-width="2"/>
  <text x="120" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">User</text>
  <text x="120" y="125" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="white">Compliance /</text>
  <text x="120" y="138" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="white">Research / Risk</text>
  
  <!-- Copilot UI -->
  <rect x="250" y="80" width="140" height="60" rx="5" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
  <text x="320" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Copilot UI</text>
  
  <!-- Arrow User to UI -->
  <path d="M 190 110 L 250 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  <text x="220" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="#64748b">Question</text>
  
  <!-- Identity & Entitlements -->
  <rect x="450" y="80" width="160" height="60" rx="5" fill="#6366f1" stroke="#4f46e5" stroke-width="2"/>
  <text x="530" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Identity &amp;</text>
  <text x="530" y="125" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Entitlements</text>
  
  <!-- Arrow UI to IAM -->
  <path d="M 390 110 L 450 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Query Planner -->
  <rect x="670" y="80" width="140" height="60" rx="5" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>
  <text x="740" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Query Planner</text>
  
  <!-- Arrow IAM to QP -->
  <path d="M 610 110 L 670 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  <text x="640" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#64748b">ABAC/RBAC</text>
  
  <!-- Retrieval Layer -->
  <rect x="870" y="80" width="140" height="60" rx="5" fill="#a855f7" stroke="#9333ea" stroke-width="2"/>
  <text x="940" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Retrieval Layer</text>
  
  <!-- Arrow QP to RET -->
  <path d="M 810 110 L 870 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  <text x="840" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#64748b">Policy-aware</text>
  
  <!-- Hybrid Search -->
  <rect x="870" y="180" width="140" height="50" rx="5" fill="#c084fc" stroke="#a855f7" stroke-width="2"/>
  <text x="940" y="200" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Hybrid Search</text>
  <text x="940" y="215" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#475569">BM25 + Vector</text>
  
  <!-- Arrow RET to HYB -->
  <path d="M 940 140 L 940 180" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Reranker -->
  <rect x="870" y="260" width="140" height="50" rx="5" fill="#d8b4fe" stroke="#c084fc" stroke-width="2"/>
  <text x="940" y="280" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Reranker</text>
  
  <!-- Arrow HYB to RR -->
  <path d="M 940 230 L 940 260" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Context Builder -->
  <rect x="870" y="340" width="140" height="50" rx="5" fill="#e9d5ff" stroke="#d8b4fe" stroke-width="2"/>
  <text x="940" y="360" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Context Builder</text>
  <text x="940" y="375" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">time-slice, dedupe</text>
  
  <!-- Arrow RR to CB -->
  <path d="M 940 310 L 940 340" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- LLM Generation -->
  <rect x="670" y="420" width="140" height="50" rx="5" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
  <text x="740" y="440" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">LLM Generation</text>
  <text x="740" y="455" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="white">guarded, schema-guided</text>
  
  <!-- Arrow CB to LLM -->
  <path d="M 870 365 L 810 420" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Post-Processing -->
  <rect x="450" y="420" width="140" height="50" rx="5" fill="#f97316" stroke="#ea580c" stroke-width="2"/>
  <text x="520" y="440" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">Post-Processing</text>
  <text x="520" y="455" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="white">redaction, tone</text>
  
  <!-- Arrow LLM to POST -->
  <path d="M 670 445 L 590 445" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Arrow POST to UI -->
  <path d="M 450 445 L 320 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Data Plane Box -->
  <rect x="50" y="520" width="500" height="240" rx="5" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="300" y="545" text-anchor="middle" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#1e3a8a">Data Plane</text>
  
  <!-- Sources -->
  <rect x="70" y="560" width="120" height="50" rx="5" fill="#e0e7ff" stroke="#6366f1" stroke-width="1"/>
  <text x="130" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Sources</text>
  <text x="130" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">Policies, Procedures,</text>
  <text x="130" y="605" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">Filings, Emails</text>
  
  <!-- Ingestion -->
  <rect x="210" y="560" width="120" height="50" rx="5" fill="#ddd6fe" stroke="#8b5cf6" stroke-width="1"/>
  <text x="270" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Ingestion +</text>
  <text x="270" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Parsing</text>
  
  <!-- Chunking -->
  <rect x="350" y="560" width="120" height="50" rx="5" fill="#e9d5ff" stroke="#a855f7" stroke-width="1"/>
  <text x="410" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Chunking +</text>
  <text x="410" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Metadata</text>
  
  <!-- Embedding -->
  <rect x="70" y="630" width="120" height="50" rx="5" fill="#fce7f3" stroke="#ec4899" stroke-width="1"/>
  <text x="130" y="650" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Embedding</text>
  
  <!-- Index -->
  <rect x="210" y="630" width="120" height="50" rx="5" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
  <text x="270" y="650" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Index /</text>
  <text x="270" y="665" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Vector Store</text>
  
  <!-- Arrows in Data Plane -->
  <path d="M 190 585 L 210 585" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 330 585 L 350 585" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 410 610 L 410 630" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 190 655 L 210 655" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 330 655 L 870 110" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  
  <!-- Control Plane Box -->
  <rect x="600" y="520" width="550" height="240" rx="5" fill="#fef2f2" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="875" y="545" text-anchor="middle" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#dc2626">Control Plane</text>
  
  <!-- Audit Logging -->
  <rect x="620" y="560" width="140" height="50" rx="5" fill="#fee2e2" stroke="#ef4444" stroke-width="1"/>
  <text x="690" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Audit Logging</text>
  <text x="690" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">prompt, retrieval, response</text>
  
  <!-- Policy Engine -->
  <rect x="780" y="560" width="140" height="50" rx="5" fill="#fecaca" stroke="#f87171" stroke-width="1"/>
  <text x="850" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Policy Engine</text>
  <text x="850" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">OPA-style rules</text>
  
  <!-- Evaluation Harness -->
  <rect x="940" y="560" width="140" height="50" rx="5" fill="#fca5a5" stroke="#f87171" stroke-width="1"/>
  <text x="1010" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Evaluation</text>
  <text x="1010" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Harness</text>
  
  <!-- Supervision Workflow -->
  <rect x="620" y="630" width="140" height="50" rx="5" fill="#f87171" stroke="#ef4444" stroke-width="1"/>
  <text x="690" y="650" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">Supervision</text>
  <text x="690" y="665" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">Workflow</text>
  
  <!-- Control Plane Arrows -->
  <path d="M 530 110 L 620 585" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 740 110 L 850 560" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 850 110 L 850 560" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 740 445 L 1010 585" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 320 110 L 620 655" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 520 445 L 620 655" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#64748b"/>
    </marker>
    <marker id="arrowhead-small" markerWidth="8" markerHeight="8" refX="7" refY="2.5" orient="auto">
      <polygon points="0 0, 8 2.5, 0 5" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

<p><strong>Key idea:</strong> In finance, the <em>retrieval</em> step is a regulated act. The system must prove it retrieved only what the user was allowed to access, and that the response was grounded in those artifacts.</p>

<hr>

<h2>How RAG copilots transform compliance workflows</h2>

<p>Compliance work is largely the business of <em>mapping language to obligations</em>:</p>

<ul>
<li>"What does this policy require?"</li>
<li>"Does this communication violate the rule?"</li>
<li>"Which controls apply to this scenario?"</li>
<li>"What changed since last quarter?"</li>
</ul>

<p>RAG copilots accelerate this by turning corpora into an interactive evidence layer—<strong>without breaking defensibility</strong>.</p>

<h3>High-leverage compliance use cases</h3>

<h4>1. Regulatory change management</h4>

<ul>
<li>Retrieve deltas across regulatory updates, internal memos, implementation plans</li>
<li>Generate impact analysis <em>with evidence links</em></li>
<li>Track "as-of" dates to avoid mixing old and new interpretations</li>
</ul>

<h4>2. Policy and procedure Q&A</h4>

<ul>
<li>Answer "what do we do?" questions with policy citations</li>
<li>Highlight ambiguous language and route to legal/compliance reviewers</li>
<li>Provide "approved snippets" for frontline teams (contact center, advisors)</li>
</ul>

<h4>3. Marketing and communications review</h4>

<ul>
<li>Ground review decisions in internal guidelines + external requirements</li>
<li>Flag risky language patterns, missing disclosures, or prohibited promises</li>
<li>Produce a reviewer memo with citations to policy text</li>
</ul>

<h4>4. Surveillance case triage</h4>

<ul>
<li>Summarize cases from alerts + communications + trade context</li>
<li>Keep a strict boundary: <em>summarize only what's retrieved and permissible</em></li>
<li>Produce structured outputs for downstream case management</li>
</ul>

<h3>Visual 2 — "Evidence-first" compliance interaction pattern (sequence)</h3>

<div class="diagram-container">
<svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: white; border: 1px solid #e2e8f0; border-radius: 8px;">
  <!-- Title -->
  <text x="500" y="30" text-anchor="middle" font-family="Inter, sans-serif" font-size="16" font-weight="600" fill="#1e3a8a">Evidence-First Compliance Interaction</text>
  
  <!-- Participants -->
  <rect x="50" y="60" width="180" height="40" rx="5" fill="#1e3a8a" stroke="#1e40af" stroke-width="2"/>
  <text x="140" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Compliance Officer</text>
  
  <rect x="270" y="60" width="180" height="40" rx="5" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">RAG Copilot</text>
  
  <rect x="490" y="60" width="180" height="40" rx="5" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>
  <text x="580" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Policy Engine</text>
  
  <rect x="710" y="60" width="240" height="40" rx="5" fill="#6366f1" stroke="#4f46e5" stroke-width="2"/>
  <text x="830" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Sources (Policies/Procedures/Comms)</text>
  
  <!-- Lifelines -->
  <line x1="140" y1="100" x2="140" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="360" y1="100" x2="360" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="580" y1="100" x2="580" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="830" y1="100" x2="830" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  
  <!-- Message 1: C->>R -->
  <path d="M 140 130 L 360 130" stroke="#1e3a8a" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="200" y="115" width="120" height="20" rx="3" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1"/>
  <text x="260" y="128" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">"Can this email language</text>
  <text x="260" y="140" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">be used for clients?"</text>
  
  <!-- Message 2: R->>P -->
  <path d="M 360 170 L 580 170" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="420" y="155" width="140" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="490" y="168" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Evaluate entitlements +</text>
  <text x="490" y="180" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">jurisdiction + comms category</text>
  
  <!-- Message 3: P-->>R -->
  <path d="M 580 210 L 360 210" stroke="#8b5cf6" stroke-width="2" fill="none" stroke-dasharray="5,5" marker-end="url(#arrowhead-seq-dashed)"/>
  <rect x="380" y="195" width="180" height="20" rx="3" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1"/>
  <text x="470" y="208" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Allowed corpora + required</text>
  <text x="470" y="220" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">disclaimers + constraints</text>
  
  <!-- Message 4: R->>S -->
  <path d="M 360 250 L 830 250" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="500" y="235" width="300" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="650" y="248" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Retrieve relevant policy clauses +</text>
  <text x="650" y="260" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">prior approvals + templates</text>
  
  <!-- Message 5: S-->>R -->
  <path d="M 830 290 L 360 290" stroke="#6366f1" stroke-width="2" fill="none" stroke-dasharray="5,5" marker-end="url(#arrowhead-seq-dashed)"/>
  <rect x="380" y="275" width="420" height="20" rx="3" fill="#eef2ff" stroke="#6366f1" stroke-width="1"/>
  <text x="590" y="288" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Evidence set (with doc IDs,</text>
  <text x="590" y="300" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">timestamps, snippets)</text>
  
  <!-- Message 6: R->>R (self) -->
  <path d="M 380 330 Q 340 350, 380 370" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="300" y="335" width="140" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="370" y="348" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Generate decision memo</text>
  <text x="370" y="360" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">(schema-guided) + citations</text>
  
  <!-- Message 7: R-->>C -->
  <path d="M 360 410 L 140 410" stroke="#3b82f6" stroke-width="2" fill="none" stroke-dasharray="5,5" marker-end="url(#arrowhead-seq-dashed)"/>
  <rect x="180" y="395" width="160" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="260" y="408" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Answer + citations +</text>
  <text x="260" y="420" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">"If uncertain: escalate" path</text>
  
  <!-- Message 8: R->>R (self) - Log -->
  <path d="M 380 450 Q 340 470, 380 490" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="300" y="455" width="140" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="370" y="468" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Log retrieval trace +</text>
  <text x="370" y="480" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">response for supervision/audit</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrowhead-seq" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#64748b"/>
    </marker>
    <marker id="arrowhead-seq-dashed" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#64748b" opacity="0.7"/>
    </marker>
  </defs>
</svg>
</div>

<p><strong>The future here is "compliance memos on demand,"</strong> where every conclusion is linked to evidence and the system knows when it must abstain or escalate.</p>

<hr>

<h2>How RAG copilots transform research workflows</h2>

<p>Research in finance isn't just summarization. It's <strong>triangulation</strong> across heterogeneous sources:</p>

<ul>
<li>public filings + investor presentations + transcripts</li>
<li>internal notes + prior coverage</li>
<li>vendor research + market data</li>
<li>risk factors, covenant language, legal terms</li>
</ul>

<p>The limiting factor is rarely intelligence; it's <em>time-to-context</em>.</p>

<p>A RAG copilot helps by:</p>

<ul>
<li>finding the right fragments across massive corpora,</li>
<li>presenting the evidence set compactly,</li>
<li>generating structured notes that are reusable.</li>
</ul>

<h3>High-leverage research use cases</h3>

<h4>1. Filings and transcript intelligence</h4>

<ul>
<li>Retrieve statements about guidance, risk factors, segment performance</li>
<li>Compare across quarters (time-sliced retrieval)</li>
<li>Generate "what changed?" briefs with quoted evidence</li>
</ul>

<h4>2. Credit / covenant analysis</h4>

<ul>
<li>Extract covenant definitions and thresholds</li>
<li>Identify exceptions and definitions buried in exhibits</li>
<li>Produce structured covenant checklists linked to source clauses</li>
</ul>

<h4>3. Internal knowledge reuse</h4>

<ul>
<li>Find prior analysis, valuation assumptions, debate threads</li>
<li>Prevent institutional amnesia while respecting information barriers</li>
</ul>

<h4>4. Due diligence copilots</h4>

<ul>
<li>Answer "what do we know about X?" with provenance</li>
<li>Track contradictions across sources (and label them explicitly)</li>
</ul>

<p>In short: RAG copilots turn research into an <strong>iterative evidence assembly</strong> process, not a blank-page writing exercise.</p>

<hr>

<h2>The best practices that separate demos from production</h2>

<h3>1) Treat retrieval as a first-class system, not a utility</h3>

<p><strong>Best practice:</strong> Build retrieval like you'd build search for a regulated environment.</p>

<ul>
<li>Hybrid retrieval (lexical + semantic) to reduce brittle misses</li>
<li>Reranking to improve top‑K quality</li>
<li>Domain-specific chunking strategies (policies ≠ transcripts ≠ tabular exhibits)</li>
<li>Metadata is non-negotiable: author, timestamp, jurisdiction, doc type, business line, confidentiality tier</li>
</ul>

<p><strong>Anti-pattern:</strong> "We embed PDFs and hope the top chunk is relevant."</p>

<h3>2) Enforce entitlements at retrieval time (not just at UI time)</h3>

<p>In finance, the greatest RAG risk isn't hallucination—it's <strong>unauthorized retrieval</strong>.</p>

<p><strong>Best practice:</strong></p>

<ul>
<li>Apply <strong>ABAC/RBAC filters</strong> as part of the retrieval query</li>
<li>Segment indexes by business unit / wall / region where appropriate</li>
<li>Use "policy-aware query planning" that knows which corpora are allowed</li>
</ul>

<p><strong>Anti-pattern:</strong> Retrieve broadly and redact later. Redaction is not a substitute for access control.</p>

<h3>3) Design answer formats for auditability</h3>

<p>A finance RAG copilot should produce outputs that can be reviewed, stored, and defended.</p>

<p><strong>Best practice:</strong> Use schema-guided generation and require citations per claim.</p>

<h3>Visual 3 — Example "evidence-native" answer schema</h3>

<p>The copilot produces structured, auditable outputs with explicit evidence links:</p>

<div class="code-example-container">
<pre><code class="language-json">{
  <span class="json-key">"question"</span>: <span class="json-string">"Is this marketing phrase compliant for retail clients?"</span>,
  <span class="json-key">"answer"</span>: <span class="json-string">"Likely non-compliant as written. It implies guaranteed performance..."</span>,
  <span class="json-key">"decision"</span>: <span class="json-value">"REJECT"</span>,
  <span class="json-key">"rationale"</span>: [
    {
      <span class="json-key">"claim"</span>: <span class="json-string">"Language implies a guarantee."</span>,
      <span class="json-key">"evidence"</span>: [
        {
          <span class="json-key">"doc_id"</span>: <span class="json-string">"POL-MKT-014"</span>,
          <span class="json-key">"snippet"</span>: <span class="json-string">"Avoid guarantees or statements implying certainty of returns..."</span>,
          <span class="json-key">"location"</span>: <span class="json-string">"Section 3.2"</span>,
          <span class="json-key">"as_of"</span>: <span class="json-string">"2025-08-01"</span>
        }
      ]
    }
  ],
  <span class="json-key">"required_changes"</span>: [
    <span class="json-string">"Remove guarantee language"</span>,
    <span class="json-string">"Add required risk disclosure XYZ"</span>
  ],
  <span class="json-key">"confidence"</span>: <span class="json-value">"medium"</span>,
  <span class="json-key">"escalation"</span>: {
    <span class="json-key">"needed"</span>: <span class="json-boolean">true</span>,
    <span class="json-key">"reason"</span>: <span class="json-string">"Retail jurisdiction nuance; request legal sign-off"</span>
  },
  <span class="json-key">"audit"</span>: {
    <span class="json-key">"retrieval_trace_id"</span>: <span class="json-string">"rt_abc123"</span>,
    <span class="json-key">"policy_profile"</span>: <span class="json-string">"Retail-US"</span>
  }
}</code></pre>
</div>

<p>This turns the copilot into a <strong>decision support system</strong> rather than a "smart text box."</p>

<h3>4) Build prompt-injection and data-exfiltration defenses into RAG</h3>

<p>RAG systems are vulnerable to:</p>

<ul>
<li>malicious instructions hidden inside retrieved documents ("ignore previous rules…"),</li>
<li>cross-document contamination ("this chunk says to reveal secrets"),</li>
<li>tool misuse if the copilot can take actions.</li>
</ul>

<p><strong>Best practice:</strong></p>

<ul>
<li>Treat retrieved text as <strong>untrusted input</strong></li>
<li>Strip or neutralize instruction-like patterns in retrieved content</li>
<li>Use tool access with least privilege + explicit user approval steps</li>
<li>Maintain a "system policy contract" the model cannot override</li>
</ul>

<p><strong>Anti-pattern:</strong> Let retrieved content freely steer system behavior.</p>

<h3>5) Measurement: evaluate groundedness, not vibes</h3>

<p>In regulated environments, you need evaluation like model risk management:</p>

<h4>Retrieval metrics</h4>

<ul>
<li>precision@K / recall@K on curated queries</li>
<li>coverage of required documents for specific tasks</li>
<li>latency and stability</li>
</ul>

<h4>Answer metrics</h4>

<ul>
<li>attribution accuracy ("is the cited snippet actually supporting the claim?")</li>
<li>groundedness (does the answer introduce unsupported facts?)</li>
<li>abstention quality (does it refuse when evidence is insufficient?)</li>
<li>consistency under paraphrase</li>
</ul>

<h4>Operational metrics</h4>

<ul>
<li>escalation rate (too high = unusable; too low = risky)</li>
<li>reviewer override rate</li>
<li>"time-to-resolution" for cases / reviews</li>
</ul>

<p><strong>Anti-pattern:</strong> Only measuring thumbs-up/down.</p>

<hr>

<h2>A controls matrix for finance-grade RAG copilots</h2>

<p>Below is a practical mapping of common risks to controls and "audit artifacts" you should be able to produce.</p>

<table>
<thead>
<tr>
<th>Risk</th>
<th>Control</th>
<th>What you should be able to prove</th>
</tr>
</thead>
<tbody>
<tr>
<td>Unauthorized data access / wall crossing</td>
<td>ABAC/RBAC enforced in retrieval, index segmentation</td>
<td>Retrieval logs show user claims + allowed corpora + filtered results</td>
</tr>
<tr>
<td>Hallucinated claims</td>
<td>Evidence-required answer schema + abstain policy</td>
<td>Each claim maps to citations; unsupported claims trigger refusal/escalation</td>
</tr>
<tr>
<td>Outdated policy guidance</td>
<td>Time-sliced retrieval + document versioning</td>
<td>Answers reference "as-of" dates and current policy versions</td>
</tr>
<tr>
<td>Prompt injection via documents</td>
<td>Treat retrieval as untrusted; sanitize/parse; instruction filters</td>
<td>Stored evidence set + sanitization steps + policy engine decisions</td>
</tr>
<tr>
<td>PII leakage</td>
<td>PII detection + redaction + constrained outputs</td>
<td>Redaction logs and policy configuration by jurisdiction</td>
</tr>
<tr>
<td>Poor supervision & audit readiness</td>
<td>Immutable logging + review workflows</td>
<td>End-to-end trace: prompt → retrieval → evidence → response → reviewer decision</td>
</tr>
<tr>
<td>Model drift / quality regression</td>
<td>Continuous evaluation harness + regression gates</td>
<td>Evaluation reports by release; rollback triggers</td>
</tr>
</tbody>
</table>

<hr>

<h2>The future: where RAG copilots are heading in financial services</h2>

<p>Over the next couple of years, the "copilot" pattern will become less about chat and more about <strong>workflow-native reasoning</strong>:</p>

<h3>1) The copilot becomes a "context compiler"</h3>

<p>Instead of "retrieve top‑K chunks," systems will build <em>structured context packs</em>:</p>

<ul>
<li>policy pack (relevant clauses, jurisdictional overlays)</li>
<li>evidence pack (documents, excerpts, timestamps)</li>
<li>constraints pack (what not to say, required disclaimers, escalation rules)</li>
</ul>

<h3>2) Retrieval will be federated and time-aware</h3>

<p>Financial knowledge is distributed and temporal:</p>

<ul>
<li>multiple repositories (wikis, ECM, case mgmt, filings, vendor data)</li>
<li>multiple truths over time (policy updates, revised disclosures)</li>
</ul>

<p>Expect <strong>federated retrieval</strong> (search across sources without centralizing everything) plus <strong>time travel</strong> ("answer as-of March 2024").</p>

<h3>3) "LLM + structured data" becomes standard</h3>

<p>For research, copilots that only read documents will plateau. The next leap is combining:</p>

<ul>
<li>unstructured evidence (docs)</li>
<li>structured facts (market/position data, risk metrics)</li>
<li>tools (calculations, tabular extraction, comparisons)</li>
</ul>

<p>The best systems will clearly separate:</p>

<ul>
<li><strong>facts from systems of record</strong></li>
<li><strong>interpretation from retrieved documents</strong></li>
<li><strong>language generation from both</strong></li>
</ul>

<h3>4) Guardrails become code, not prompts</h3>

<p>Prompt-only safety won't satisfy high-assurance needs. Guardrails will live in:</p>

<ul>
<li>policy engines</li>
<li>schema validators</li>
<li>retrieval filters</li>
<li>deterministic post-processors</li>
</ul>

<p>In other words: <strong>governance moves out of the prompt and into the architecture.</strong></p>

<hr>

<h2>How Ishtar AI thinks about building RAG copilots in finance</h2>

<p>We approach RAG copilots as <strong>regulated decision support systems</strong>:</p>

<ul>
<li><strong>Evidence-native UX:</strong> answers are inseparable from citations and provenance</li>
<li><strong>Entitlements-first retrieval:</strong> identity and policy constraints are enforced before context is built</li>
<li><strong>Workflow integration:</strong> supervision, escalations, and review artifacts are part of the product</li>
<li><strong>Evaluation as a release gate:</strong> every change is tested against curated finance-specific benchmarks</li>
<li><strong>Observability by design:</strong> trace IDs, retrieval logs, and "why this answer" are always available</li>
</ul>

<p>If you can't explain an output, you don't own it. Finance demands ownership.</p>

<hr>

<h2>Closing thought: the winning copilot is the one you can defend</h2>

<p>The future of RAG copilots in financial services is not a model that writes the best paragraphs. It's a system that turns institutional knowledge into <strong>defensible decisions</strong>, faster:</p>

<ul>
<li>grounded answers,</li>
<li>correct boundaries,</li>
<li>measurable reliability,</li>
<li>audit-ready traces.</li>
</ul>

<p>That's not just AI. That's operational infrastructure for knowledge work.</p>"""


# Add config to all template contexts
def get_template_context(request: Request, **kwargs):
    """Get template context with config"""
    context = {"request": request, "config": settings, **kwargs}
    return context


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", get_template_context(request))


@router.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    """Services page"""
    return templates.TemplateResponse("services.html", get_template_context(request))


@router.get("/finance", response_class=HTMLResponse)
async def finance(request: Request):
    """Finance focus page"""
    return templates.TemplateResponse("finance.html", get_template_context(request))


@router.get("/media-ads", response_class=HTMLResponse)
async def media_ads(request: Request):
    """Media/Advertising focus page"""
    return templates.TemplateResponse("media_ads.html", get_template_context(request))


@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact page"""
    return templates.TemplateResponse("contact.html", get_template_context(request))


@router.get("/privacy", response_class=HTMLResponse)
async def privacy(request: Request):
    """Privacy Policy page"""
    return templates.TemplateResponse("privacy.html", get_template_context(request))


@router.get("/terms", response_class=HTMLResponse)
async def terms(request: Request):
    """Terms of Service page"""
    return templates.TemplateResponse("terms.html", get_template_context(request))


@router.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    """Blog page"""
    # Placeholder blog posts
    posts = [
        {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "slug": "future-of-rag-copilots-financial-services",
            "author": "Ishtar AI Team",
        },
        {
            "title": "AI Governance: Building Trust in Enterprise AI Systems",
            "excerpt": "Best practices for implementing governance frameworks that ensure AI systems are secure, compliant, and reliable.",
            "date": "2024-01-10",
            "slug": "ai-governance-trust-enterprise",
            "author": "Ishtar AI Team",
        },
        {
            "title": "Synthetic Media Compliance: What Media Companies Need to Know",
            "excerpt": "Navigating the regulatory landscape for AI-generated content and ensuring brand safety in the age of synthetic media.",
            "date": "2024-01-05",
            "slug": "synthetic-media-compliance-guide",
            "author": "Ishtar AI Team",
        },
    ]
    return templates.TemplateResponse(
        "blog.html", get_template_context(request, posts=posts)
    )


@router.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    """Individual blog post page"""
    # Article content mapping
    articles = {
        "future-of-rag-copilots-financial-services": {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "slug": "future-of-rag-copilots-financial-services",
            "content": get_rag_copilots_article_content(),
        },
        "future-of-rag-copilots-finance": {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "slug": "future-of-rag-copilots-finance",
            "content": get_rag_copilots_article_content(),
        },
    }

    # Get article or return placeholder
    post = articles.get(
        slug,
        {
            "title": "Blog Post",
            "content": "<p>This is a placeholder blog post. Content coming soon.</p>",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "excerpt": "Blog post excerpt.",
            "slug": slug,
        },
    )

    # Ensure slug is set for all posts
    if "slug" not in post:
        post["slug"] = slug

    return templates.TemplateResponse(
        "blog_post.html", get_template_context(request, post=post)
    )


def get_rag_copilots_article_content():
    """Get the full RAG Copilots article content"""
    return """<p>Financial services didn't fall in love with generative AI because it writes fluent paragraphs. It fell in love with the <em>idea</em> of compressing the time between "question asked" and "decision defended."</p>

<p>But finance also has an allergy to ungrounded prose. A model that "sounds right" is not a model you can supervise, audit, or explain under pressure.</p>

<p>That's why the future doesn't look like a free-form chatbot bolted onto a document drive. It looks like <strong>RAG copilots</strong>: systems that treat enterprise knowledge as the primary source of truth, and treat the LLM as a reasoning-and-language layer constrained by retrieval, policy, and evidence.</p>

<p>At <strong>Ishtar AI</strong>, we think the winners in this space will build copilots that are:</p>

<ul>
<li><strong>Evidence-first</strong> (every answer is attributable),</li>
<li><strong>Policy-aware</strong> (access, jurisdiction, and confidentiality are enforced before generation),</li>
<li><strong>Auditable by design</strong> (traceability is a product feature, not an afterthought),</li>
<li><strong>Measurable</strong> (quality is evaluated like a risk model, not a demo).</li>
</ul>

<p>Below is a technical view of where RAG copilots are going in finance—especially for <strong>compliance</strong> and <strong>research</strong>—and what best practices separate pilots from production systems.</p>

<hr>

<h2>Why finance needs RAG, not "just an LLM"</h2>

<p>A base LLM is fundamentally a probabilistic text generator trained on broad patterns. In finance, that creates immediate friction:</p>

<ul>
<li><strong>Supervision and recordkeeping:</strong> You don't just need an answer—you need <em>what it was based on</em>, who was allowed to see it, and what version of the truth existed at that time.</li>
<li><strong>Non-public information boundaries:</strong> "Helpful" can become "harmful" if retrieval crosses Chinese walls or leaks MNPI.</li>
<li><strong>Regulatory defensibility:</strong> A compliance decision that can't cite underlying policy language, procedures, communications, or evidence is fragile.</li>
<li><strong>Operational risk:</strong> Hallucinations aren't just incorrect—they are <em>uncontrolled statements</em> that can propagate into downstream memos, client comms, and filings.</li>
</ul>

<p><strong>RAG (Retrieval-Augmented Generation)</strong> changes the center of gravity. Instead of asking a model to invent, you ask it to <em>retrieve</em> from approved corpora, then <em>compose</em> a response that is explicitly grounded.</p>

<p>The future RAG copilot is not "ChatGPT with a vector database." It is an <strong>evidence compiler</strong> with a language interface.</p>

<hr>

<h2>What a "RAG copilot" actually is (and what it isn't)</h2>

<p>A production-grade RAG copilot has two planes:</p>

<ul>
<li><strong>Data plane:</strong> ingestion, chunking, embeddings, indexing, retrieval, citation, and provenance tracking</li>
<li><strong>Control plane:</strong> identity, entitlement enforcement, policy gating, audit logging, evaluation, and supervisory workflows</li>
</ul>

<p>It is <em>not</em> a system that:</p>

<ul>
<li>dumps top‑K retrieved chunks into a prompt and hopes for the best,</li>
<li>treats citations as decoration,</li>
<li>ignores access control in retrieval,</li>
<li>lacks measurement beyond "users like it."</li>
</ul>

<p>A finance-grade copilot behaves more like a cautious analyst: it cites, it abstains, it flags uncertainty, it respects boundaries, and it leaves a paper trail.</p>

<hr>

<h2>Visual 1 — Reference architecture for a finance-grade RAG copilot</h2>

<p>Below is a reference architecture that reflects what actually matters in financial services: provenance, policy, and observability.</p>

<div class="diagram-container">
<svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: white; border: 1px solid #e2e8f0; border-radius: 8px;">
  <!-- Title -->
  <text x="600" y="30" text-anchor="middle" font-family="Inter, sans-serif" font-size="18" font-weight="600" fill="#1e3a8a">Finance-Grade RAG Copilot Architecture</text>
  
  <!-- User -->
  <rect x="50" y="80" width="140" height="60" rx="5" fill="#1e3a8a" stroke="#1e40af" stroke-width="2"/>
  <text x="120" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">User</text>
  <text x="120" y="125" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="white">Compliance /</text>
  <text x="120" y="138" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="white">Research / Risk</text>
  
  <!-- Copilot UI -->
  <rect x="250" y="80" width="140" height="60" rx="5" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
  <text x="320" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Copilot UI</text>
  
  <!-- Arrow User to UI -->
  <path d="M 190 110 L 250 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  <text x="220" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="#64748b">Question</text>
  
  <!-- Identity & Entitlements -->
  <rect x="450" y="80" width="160" height="60" rx="5" fill="#6366f1" stroke="#4f46e5" stroke-width="2"/>
  <text x="530" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Identity &amp;</text>
  <text x="530" y="125" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Entitlements</text>
  
  <!-- Arrow UI to IAM -->
  <path d="M 390 110 L 450 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Query Planner -->
  <rect x="670" y="80" width="140" height="60" rx="5" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>
  <text x="740" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Query Planner</text>
  
  <!-- Arrow IAM to QP -->
  <path d="M 610 110 L 670 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  <text x="640" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#64748b">ABAC/RBAC</text>
  
  <!-- Retrieval Layer -->
  <rect x="870" y="80" width="140" height="60" rx="5" fill="#a855f7" stroke="#9333ea" stroke-width="2"/>
  <text x="940" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Retrieval Layer</text>
  
  <!-- Arrow QP to RET -->
  <path d="M 810 110 L 870 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  <text x="840" y="105" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#64748b">Policy-aware</text>
  
  <!-- Hybrid Search -->
  <rect x="870" y="180" width="140" height="50" rx="5" fill="#c084fc" stroke="#a855f7" stroke-width="2"/>
  <text x="940" y="200" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Hybrid Search</text>
  <text x="940" y="215" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#475569">BM25 + Vector</text>
  
  <!-- Arrow RET to HYB -->
  <path d="M 940 140 L 940 180" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Reranker -->
  <rect x="870" y="260" width="140" height="50" rx="5" fill="#d8b4fe" stroke="#c084fc" stroke-width="2"/>
  <text x="940" y="280" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Reranker</text>
  
  <!-- Arrow HYB to RR -->
  <path d="M 940 230 L 940 260" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Context Builder -->
  <rect x="870" y="340" width="140" height="50" rx="5" fill="#e9d5ff" stroke="#d8b4fe" stroke-width="2"/>
  <text x="940" y="360" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Context Builder</text>
  <text x="940" y="375" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">time-slice, dedupe</text>
  
  <!-- Arrow RR to CB -->
  <path d="M 940 310 L 940 340" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- LLM Generation -->
  <rect x="670" y="420" width="140" height="50" rx="5" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
  <text x="740" y="440" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">LLM Generation</text>
  <text x="740" y="455" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="white">guarded, schema-guided</text>
  
  <!-- Arrow CB to LLM -->
  <path d="M 870 365 L 810 420" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Post-Processing -->
  <rect x="450" y="420" width="140" height="50" rx="5" fill="#f97316" stroke="#ea580c" stroke-width="2"/>
  <text x="520" y="440" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">Post-Processing</text>
  <text x="520" y="455" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="white">redaction, tone</text>
  
  <!-- Arrow LLM to POST -->
  <path d="M 670 445 L 590 445" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Arrow POST to UI -->
  <path d="M 450 445 L 320 110" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Data Plane Box -->
  <rect x="50" y="520" width="500" height="240" rx="5" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="300" y="545" text-anchor="middle" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#1e3a8a">Data Plane</text>
  
  <!-- Sources -->
  <rect x="70" y="560" width="120" height="50" rx="5" fill="#e0e7ff" stroke="#6366f1" stroke-width="1"/>
  <text x="130" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Sources</text>
  <text x="130" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">Policies, Procedures,</text>
  <text x="130" y="605" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">Filings, Emails</text>
  
  <!-- Ingestion -->
  <rect x="210" y="560" width="120" height="50" rx="5" fill="#ddd6fe" stroke="#8b5cf6" stroke-width="1"/>
  <text x="270" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Ingestion +</text>
  <text x="270" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Parsing</text>
  
  <!-- Chunking -->
  <rect x="350" y="560" width="120" height="50" rx="5" fill="#e9d5ff" stroke="#a855f7" stroke-width="1"/>
  <text x="410" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Chunking +</text>
  <text x="410" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Metadata</text>
  
  <!-- Embedding -->
  <rect x="70" y="630" width="120" height="50" rx="5" fill="#fce7f3" stroke="#ec4899" stroke-width="1"/>
  <text x="130" y="650" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Embedding</text>
  
  <!-- Index -->
  <rect x="210" y="630" width="120" height="50" rx="5" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
  <text x="270" y="650" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Index /</text>
  <text x="270" y="665" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Vector Store</text>
  
  <!-- Arrows in Data Plane -->
  <path d="M 190 585 L 210 585" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 330 585 L 350 585" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 410 610 L 410 630" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 190 655 L 210 655" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  <path d="M 330 655 L 870 110" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#arrowhead-small)"/>
  
  <!-- Control Plane Box -->
  <rect x="600" y="520" width="550" height="240" rx="5" fill="#fef2f2" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="875" y="545" text-anchor="middle" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#dc2626">Control Plane</text>
  
  <!-- Audit Logging -->
  <rect x="620" y="560" width="140" height="50" rx="5" fill="#fee2e2" stroke="#ef4444" stroke-width="1"/>
  <text x="690" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Audit Logging</text>
  <text x="690" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">prompt, retrieval, response</text>
  
  <!-- Policy Engine -->
  <rect x="780" y="560" width="140" height="50" rx="5" fill="#fecaca" stroke="#f87171" stroke-width="1"/>
  <text x="850" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Policy Engine</text>
  <text x="850" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" fill="#475569">OPA-style rules</text>
  
  <!-- Evaluation Harness -->
  <rect x="940" y="560" width="140" height="50" rx="5" fill="#fca5a5" stroke="#f87171" stroke-width="1"/>
  <text x="1010" y="580" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Evaluation</text>
  <text x="1010" y="595" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#1e293b">Harness</text>
  
  <!-- Supervision Workflow -->
  <rect x="620" y="630" width="140" height="50" rx="5" fill="#f87171" stroke="#ef4444" stroke-width="1"/>
  <text x="690" y="650" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">Supervision</text>
  <text x="690" y="665" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="white">Workflow</text>
  
  <!-- Control Plane Arrows -->
  <path d="M 530 110 L 620 585" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 740 110 L 850 560" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 850 110 L 850 560" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 740 445 L 1010 585" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 320 110 L 620 655" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  <path d="M 520 445 L 620 655" stroke="#dc2626" stroke-width="1.5" fill="none" stroke-dasharray="3,3" marker-end="url(#arrowhead-small)"/>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#64748b"/>
    </marker>
    <marker id="arrowhead-small" markerWidth="8" markerHeight="8" refX="7" refY="2.5" orient="auto">
      <polygon points="0 0, 8 2.5, 0 5" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

<p><strong>Key idea:</strong> In finance, the <em>retrieval</em> step is a regulated act. The system must prove it retrieved only what the user was allowed to access, and that the response was grounded in those artifacts.</p>

<hr>

<h2>How RAG copilots transform compliance workflows</h2>

<p>Compliance work is largely the business of <em>mapping language to obligations</em>:</p>

<ul>
<li>"What does this policy require?"</li>
<li>"Does this communication violate the rule?"</li>
<li>"Which controls apply to this scenario?"</li>
<li>"What changed since last quarter?"</li>
</ul>

<p>RAG copilots accelerate this by turning corpora into an interactive evidence layer—<strong>without breaking defensibility</strong>.</p>

<h3>High-leverage compliance use cases</h3>

<h4>1. Regulatory change management</h4>

<ul>
<li>Retrieve deltas across regulatory updates, internal memos, implementation plans</li>
<li>Generate impact analysis <em>with evidence links</em></li>
<li>Track "as-of" dates to avoid mixing old and new interpretations</li>
</ul>

<h4>2. Policy and procedure Q&A</h4>

<ul>
<li>Answer "what do we do?" questions with policy citations</li>
<li>Highlight ambiguous language and route to legal/compliance reviewers</li>
<li>Provide "approved snippets" for frontline teams (contact center, advisors)</li>
</ul>

<h4>3. Marketing and communications review</h4>

<ul>
<li>Ground review decisions in internal guidelines + external requirements</li>
<li>Flag risky language patterns, missing disclosures, or prohibited promises</li>
<li>Produce a reviewer memo with citations to policy text</li>
</ul>

<h4>4. Surveillance case triage</h4>

<ul>
<li>Summarize cases from alerts + communications + trade context</li>
<li>Keep a strict boundary: <em>summarize only what's retrieved and permissible</em></li>
<li>Produce structured outputs for downstream case management</li>
</ul>

<h3>Visual 2 — "Evidence-first" compliance interaction pattern (sequence)</h3>

<div class="diagram-container">
<svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: white; border: 1px solid #e2e8f0; border-radius: 8px;">
  <!-- Title -->
  <text x="500" y="30" text-anchor="middle" font-family="Inter, sans-serif" font-size="16" font-weight="600" fill="#1e3a8a">Evidence-First Compliance Interaction</text>
  
  <!-- Participants -->
  <rect x="50" y="60" width="180" height="40" rx="5" fill="#1e3a8a" stroke="#1e40af" stroke-width="2"/>
  <text x="140" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Compliance Officer</text>
  
  <rect x="270" y="60" width="180" height="40" rx="5" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">RAG Copilot</text>
  
  <rect x="490" y="60" width="180" height="40" rx="5" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>
  <text x="580" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Policy Engine</text>
  
  <rect x="710" y="60" width="240" height="40" rx="5" fill="#6366f1" stroke="#4f46e5" stroke-width="2"/>
  <text x="830" y="85" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="600" fill="white">Sources (Policies/Procedures/Comms)</text>
  
  <!-- Lifelines -->
  <line x1="140" y1="100" x2="140" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="360" y1="100" x2="360" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="580" y1="100" x2="580" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="830" y1="100" x2="830" y2="550" stroke="#64748b" stroke-width="2" stroke-dasharray="5,5"/>
  
  <!-- Message 1: C->>R -->
  <path d="M 140 130 L 360 130" stroke="#1e3a8a" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="200" y="115" width="120" height="20" rx="3" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1"/>
  <text x="260" y="128" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">"Can this email language</text>
  <text x="260" y="140" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">be used for clients?"</text>
  
  <!-- Message 2: R->>P -->
  <path d="M 360 170 L 580 170" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="420" y="155" width="140" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="490" y="168" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Evaluate entitlements +</text>
  <text x="490" y="180" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">jurisdiction + comms category</text>
  
  <!-- Message 3: P-->>R -->
  <path d="M 580 210 L 360 210" stroke="#8b5cf6" stroke-width="2" fill="none" stroke-dasharray="5,5" marker-end="url(#arrowhead-seq-dashed)"/>
  <rect x="380" y="195" width="180" height="20" rx="3" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1"/>
  <text x="470" y="208" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Allowed corpora + required</text>
  <text x="470" y="220" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">disclaimers + constraints</text>
  
  <!-- Message 4: R->>S -->
  <path d="M 360 250 L 830 250" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="500" y="235" width="300" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="650" y="248" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Retrieve relevant policy clauses +</text>
  <text x="650" y="260" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">prior approvals + templates</text>
  
  <!-- Message 5: S-->>R -->
  <path d="M 830 290 L 360 290" stroke="#6366f1" stroke-width="2" fill="none" stroke-dasharray="5,5" marker-end="url(#arrowhead-seq-dashed)"/>
  <rect x="380" y="275" width="420" height="20" rx="3" fill="#eef2ff" stroke="#6366f1" stroke-width="1"/>
  <text x="590" y="288" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Evidence set (with doc IDs,</text>
  <text x="590" y="300" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">timestamps, snippets)</text>
  
  <!-- Message 6: R->>R (self) -->
  <path d="M 380 330 Q 340 350, 380 370" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="300" y="335" width="140" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="370" y="348" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Generate decision memo</text>
  <text x="370" y="360" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">(schema-guided) + citations</text>
  
  <!-- Message 7: R-->>C -->
  <path d="M 360 410 L 140 410" stroke="#3b82f6" stroke-width="2" fill="none" stroke-dasharray="5,5" marker-end="url(#arrowhead-seq-dashed)"/>
  <rect x="180" y="395" width="160" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="260" y="408" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Answer + citations +</text>
  <text x="260" y="420" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">"If uncertain: escalate" path</text>
  
  <!-- Message 8: R->>R (self) - Log -->
  <path d="M 380 450 Q 340 470, 380 490" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#arrowhead-seq)"/>
  <rect x="300" y="455" width="140" height="20" rx="3" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="370" y="468" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">Log retrieval trace +</text>
  <text x="370" y="480" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#1e293b">response for supervision/audit</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrowhead-seq" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#64748b"/>
    </marker>
    <marker id="arrowhead-seq-dashed" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#64748b" opacity="0.7"/>
    </marker>
  </defs>
</svg>
</div>

<p><strong>The future here is "compliance memos on demand,"</strong> where every conclusion is linked to evidence and the system knows when it must abstain or escalate.</p>

<hr>

<h2>How RAG copilots transform research workflows</h2>

<p>Research in finance isn't just summarization. It's <strong>triangulation</strong> across heterogeneous sources:</p>

<ul>
<li>public filings + investor presentations + transcripts</li>
<li>internal notes + prior coverage</li>
<li>vendor research + market data</li>
<li>risk factors, covenant language, legal terms</li>
</ul>

<p>The limiting factor is rarely intelligence; it's <em>time-to-context</em>.</p>

<p>A RAG copilot helps by:</p>

<ul>
<li>finding the right fragments across massive corpora,</li>
<li>presenting the evidence set compactly,</li>
<li>generating structured notes that are reusable.</li>
</ul>

<h3>High-leverage research use cases</h3>

<h4>1. Filings and transcript intelligence</h4>

<ul>
<li>Retrieve statements about guidance, risk factors, segment performance</li>
<li>Compare across quarters (time-sliced retrieval)</li>
<li>Generate "what changed?" briefs with quoted evidence</li>
</ul>

<h4>2. Credit / covenant analysis</h4>

<ul>
<li>Extract covenant definitions and thresholds</li>
<li>Identify exceptions and definitions buried in exhibits</li>
<li>Produce structured covenant checklists linked to source clauses</li>
</ul>

<h4>3. Internal knowledge reuse</h4>

<ul>
<li>Find prior analysis, valuation assumptions, debate threads</li>
<li>Prevent institutional amnesia while respecting information barriers</li>
</ul>

<h4>4. Due diligence copilots</h4>

<ul>
<li>Answer "what do we know about X?" with provenance</li>
<li>Track contradictions across sources (and label them explicitly)</li>
</ul>

<p>In short: RAG copilots turn research into an <strong>iterative evidence assembly</strong> process, not a blank-page writing exercise.</p>

<hr>

<h2>The best practices that separate demos from production</h2>

<h3>1) Treat retrieval as a first-class system, not a utility</h3>

<p><strong>Best practice:</strong> Build retrieval like you'd build search for a regulated environment.</p>

<ul>
<li>Hybrid retrieval (lexical + semantic) to reduce brittle misses</li>
<li>Reranking to improve top‑K quality</li>
<li>Domain-specific chunking strategies (policies ≠ transcripts ≠ tabular exhibits)</li>
<li>Metadata is non-negotiable: author, timestamp, jurisdiction, doc type, business line, confidentiality tier</li>
</ul>

<p><strong>Anti-pattern:</strong> "We embed PDFs and hope the top chunk is relevant."</p>

<h3>2) Enforce entitlements at retrieval time (not just at UI time)</h3>

<p>In finance, the greatest RAG risk isn't hallucination—it's <strong>unauthorized retrieval</strong>.</p>

<p><strong>Best practice:</strong></p>

<ul>
<li>Apply <strong>ABAC/RBAC filters</strong> as part of the retrieval query</li>
<li>Segment indexes by business unit / wall / region where appropriate</li>
<li>Use "policy-aware query planning" that knows which corpora are allowed</li>
</ul>

<p><strong>Anti-pattern:</strong> Retrieve broadly and redact later. Redaction is not a substitute for access control.</p>

<h3>3) Design answer formats for auditability</h3>

<p>A finance RAG copilot should produce outputs that can be reviewed, stored, and defended.</p>

<p><strong>Best practice:</strong> Use schema-guided generation and require citations per claim.</p>

<h3>Visual 3 — Example "evidence-native" answer schema</h3>

<p>The copilot produces structured, auditable outputs with explicit evidence links:</p>

<div class="code-example-container">
<pre><code class="language-json">{
  <span class="json-key">"question"</span>: <span class="json-string">"Is this marketing phrase compliant for retail clients?"</span>,
  <span class="json-key">"answer"</span>: <span class="json-string">"Likely non-compliant as written. It implies guaranteed performance..."</span>,
  <span class="json-key">"decision"</span>: <span class="json-value">"REJECT"</span>,
  <span class="json-key">"rationale"</span>: [
    {
      <span class="json-key">"claim"</span>: <span class="json-string">"Language implies a guarantee."</span>,
      <span class="json-key">"evidence"</span>: [
        {
          <span class="json-key">"doc_id"</span>: <span class="json-string">"POL-MKT-014"</span>,
          <span class="json-key">"snippet"</span>: <span class="json-string">"Avoid guarantees or statements implying certainty of returns..."</span>,
          <span class="json-key">"location"</span>: <span class="json-string">"Section 3.2"</span>,
          <span class="json-key">"as_of"</span>: <span class="json-string">"2025-08-01"</span>
        }
      ]
    }
  ],
  <span class="json-key">"required_changes"</span>: [
    <span class="json-string">"Remove guarantee language"</span>,
    <span class="json-string">"Add required risk disclosure XYZ"</span>
  ],
  <span class="json-key">"confidence"</span>: <span class="json-value">"medium"</span>,
  <span class="json-key">"escalation"</span>: {
    <span class="json-key">"needed"</span>: <span class="json-boolean">true</span>,
    <span class="json-key">"reason"</span>: <span class="json-string">"Retail jurisdiction nuance; request legal sign-off"</span>
  },
  <span class="json-key">"audit"</span>: {
    <span class="json-key">"retrieval_trace_id"</span>: <span class="json-string">"rt_abc123"</span>,
    <span class="json-key">"policy_profile"</span>: <span class="json-string">"Retail-US"</span>
  }
}</code></pre>
</div>

<p>This turns the copilot into a <strong>decision support system</strong> rather than a "smart text box."</p>

<h3>4) Build prompt-injection and data-exfiltration defenses into RAG</h3>

<p>RAG systems are vulnerable to:</p>

<ul>
<li>malicious instructions hidden inside retrieved documents ("ignore previous rules…"),</li>
<li>cross-document contamination ("this chunk says to reveal secrets"),</li>
<li>tool misuse if the copilot can take actions.</li>
</ul>

<p><strong>Best practice:</strong></p>

<ul>
<li>Treat retrieved text as <strong>untrusted input</strong></li>
<li>Strip or neutralize instruction-like patterns in retrieved content</li>
<li>Use tool access with least privilege + explicit user approval steps</li>
<li>Maintain a "system policy contract" the model cannot override</li>
</ul>

<p><strong>Anti-pattern:</strong> Let retrieved content freely steer system behavior.</p>

<h3>5) Measurement: evaluate groundedness, not vibes</h3>

<p>In regulated environments, you need evaluation like model risk management:</p>

<h4>Retrieval metrics</h4>

<ul>
<li>precision@K / recall@K on curated queries</li>
<li>coverage of required documents for specific tasks</li>
<li>latency and stability</li>
</ul>

<h4>Answer metrics</h4>

<ul>
<li>attribution accuracy ("is the cited snippet actually supporting the claim?")</li>
<li>groundedness (does the answer introduce unsupported facts?)</li>
<li>abstention quality (does it refuse when evidence is insufficient?)</li>
<li>consistency under paraphrase</li>
</ul>

<h4>Operational metrics</h4>

<ul>
<li>escalation rate (too high = unusable; too low = risky)</li>
<li>reviewer override rate</li>
<li>"time-to-resolution" for cases / reviews</li>
</ul>

<p><strong>Anti-pattern:</strong> Only measuring thumbs-up/down.</p>

<hr>

<h2>A controls matrix for finance-grade RAG copilots</h2>

<p>Below is a practical mapping of common risks to controls and "audit artifacts" you should be able to produce.</p>

<table>
<thead>
<tr>
<th>Risk</th>
<th>Control</th>
<th>What you should be able to prove</th>
</tr>
</thead>
<tbody>
<tr>
<td>Unauthorized data access / wall crossing</td>
<td>ABAC/RBAC enforced in retrieval, index segmentation</td>
<td>Retrieval logs show user claims + allowed corpora + filtered results</td>
</tr>
<tr>
<td>Hallucinated claims</td>
<td>Evidence-required answer schema + abstain policy</td>
<td>Each claim maps to citations; unsupported claims trigger refusal/escalation</td>
</tr>
<tr>
<td>Outdated policy guidance</td>
<td>Time-sliced retrieval + document versioning</td>
<td>Answers reference "as-of" dates and current policy versions</td>
</tr>
<tr>
<td>Prompt injection via documents</td>
<td>Treat retrieval as untrusted; sanitize/parse; instruction filters</td>
<td>Stored evidence set + sanitization steps + policy engine decisions</td>
</tr>
<tr>
<td>PII leakage</td>
<td>PII detection + redaction + constrained outputs</td>
<td>Redaction logs and policy configuration by jurisdiction</td>
</tr>
<tr>
<td>Poor supervision & audit readiness</td>
<td>Immutable logging + review workflows</td>
<td>End-to-end trace: prompt → retrieval → evidence → response → reviewer decision</td>
</tr>
<tr>
<td>Model drift / quality regression</td>
<td>Continuous evaluation harness + regression gates</td>
<td>Evaluation reports by release; rollback triggers</td>
</tr>
</tbody>
</table>

<hr>

<h2>The future: where RAG copilots are heading in financial services</h2>

<p>Over the next couple of years, the "copilot" pattern will become less about chat and more about <strong>workflow-native reasoning</strong>:</p>

<h3>1) The copilot becomes a "context compiler"</h3>

<p>Instead of "retrieve top‑K chunks," systems will build <em>structured context packs</em>:</p>

<ul>
<li>policy pack (relevant clauses, jurisdictional overlays)</li>
<li>evidence pack (documents, excerpts, timestamps)</li>
<li>constraints pack (what not to say, required disclaimers, escalation rules)</li>
</ul>

<h3>2) Retrieval will be federated and time-aware</h3>

<p>Financial knowledge is distributed and temporal:</p>

<ul>
<li>multiple repositories (wikis, ECM, case mgmt, filings, vendor data)</li>
<li>multiple truths over time (policy updates, revised disclosures)</li>
</ul>

<p>Expect <strong>federated retrieval</strong> (search across sources without centralizing everything) plus <strong>time travel</strong> ("answer as-of March 2024").</p>

<h3>3) "LLM + structured data" becomes standard</h3>

<p>For research, copilots that only read documents will plateau. The next leap is combining:</p>

<ul>
<li>unstructured evidence (docs)</li>
<li>structured facts (market/position data, risk metrics)</li>
<li>tools (calculations, tabular extraction, comparisons)</li>
</ul>

<p>The best systems will clearly separate:</p>

<ul>
<li><strong>facts from systems of record</strong></li>
<li><strong>interpretation from retrieved documents</strong></li>
<li><strong>language generation from both</strong></li>
</ul>

<h3>4) Guardrails become code, not prompts</h3>

<p>Prompt-only safety won't satisfy high-assurance needs. Guardrails will live in:</p>

<ul>
<li>policy engines</li>
<li>schema validators</li>
<li>retrieval filters</li>
<li>deterministic post-processors</li>
</ul>

<p>In other words: <strong>governance moves out of the prompt and into the architecture.</strong></p>

<hr>

<h2>How Ishtar AI thinks about building RAG copilots in finance</h2>

<p>We approach RAG copilots as <strong>regulated decision support systems</strong>:</p>

<ul>
<li><strong>Evidence-native UX:</strong> answers are inseparable from citations and provenance</li>
<li><strong>Entitlements-first retrieval:</strong> identity and policy constraints are enforced before context is built</li>
<li><strong>Workflow integration:</strong> supervision, escalations, and review artifacts are part of the product</li>
<li><strong>Evaluation as a release gate:</strong> every change is tested against curated finance-specific benchmarks</li>
<li><strong>Observability by design:</strong> trace IDs, retrieval logs, and "why this answer" are always available</li>
</ul>

<p>If you can't explain an output, you don't own it. Finance demands ownership.</p>

<hr>

<h2>Closing thought: the winning copilot is the one you can defend</h2>

<p>The future of RAG copilots in financial services is not a model that writes the best paragraphs. It's a system that turns institutional knowledge into <strong>defensible decisions</strong>, faster:</p>

<ul>
<li>grounded answers,</li>
<li>correct boundaries,</li>
<li>measurable reliability,</li>
<li>audit-ready traces.</li>
</ul>

<p>That's not just AI. That's operational infrastructure for knowledge work.</p>"""


@router.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    """FAQ page"""
    faqs = [
        {
            "question": "What industries do you serve?",
            "answer": "We specialize in finance and media/advertising organizations, helping them implement enterprise-grade AI solutions.",
        },
        {
            "question": "How long does a typical implementation take?",
            "answer": "Implementation timelines vary based on project scope, but most engagements range from 8-16 weeks for production-ready solutions.",
        },
        {
            "question": "Do you provide ongoing support?",
            "answer": "Yes, we offer comprehensive support packages including maintenance, updates, and optimization services.",
        },
        {
            "question": "What security standards do you follow?",
            "answer": "We implement industry-standard security practices including encryption, audit trails, and compliance with SOC 2, GDPR, and other relevant frameworks.",
        },
        {
            "question": "Can you integrate with our existing systems?",
            "answer": "Absolutely. Our solutions are designed to integrate seamlessly with existing enterprise infrastructure and workflows.",
        },
        {
            "question": "What is your pricing model?",
            "answer": "Pricing varies based on project scope and requirements. Contact us for a customized quote tailored to your needs.",
        },
    ]
    return templates.TemplateResponse(
        "faq.html", get_template_context(request, faqs=faqs)
    )


@router.get("/pricing", response_class=HTMLResponse)
async def pricing(request: Request):
    """Pricing page"""
    return templates.TemplateResponse("pricing.html", get_template_context(request))


@router.post("/newsletter", response_class=HTMLResponse)
async def subscribe_newsletter(request: Request, email: str = Form(...)):
    """Handle newsletter subscription"""
    # TODO: Integrate with email service (Mailchimp, SendGrid, etc.)
    # For now, just return success
    return templates.TemplateResponse(
        "newsletter_success.html",
        get_template_context(request, email=email),
    )


@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: Optional[str] = None):
    """Search page"""
    results = []
    if q:
        # Placeholder search - in production, implement actual search
        # For now, return empty results
        results = []
    return templates.TemplateResponse(
        "search.html", get_template_context(request, query=q, results=results)
    )


@router.post("/contact", response_class=HTMLResponse)
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: Optional[str] = Form(None),
    company: Optional[str] = Form(None),
    message: str = Form(...),
    website: Optional[str] = Form(None),  # Honeypot field for spam protection
):
    """Handle contact form submission"""
    # Honeypot spam protection
    if website:
        # Bot detected, return success anyway to not reveal the honeypot
        return templates.TemplateResponse(
            "contact.html",
            get_template_context(
                request,
                success=True,
                message="Thank you for your message! We'll get back to you soon.",
            ),
        )

    # Send email if configured
    from app.utils.email import send_contact_form_email

    email_sent = await send_contact_form_email(
        name=name, email=email, phone=phone, company=company, message=message
    )

    if email_sent:
        success_message = "Thank you for your message! We'll get back to you soon."
    else:
        # Still show success to user even if email fails (log error server-side)
        success_message = "Thank you for your message! We'll get back to you soon."

    return templates.TemplateResponse(
        "contact.html",
        get_template_context(request, success=True, message=success_message),
    )
