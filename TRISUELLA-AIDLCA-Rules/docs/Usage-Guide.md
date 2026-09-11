# OWASP TriSuElla-AIDLCA Secure Development Framework — Usage Guide (v3.0)

> **TriSuElla-AIDLCA SDF** — Security-First, AI-Native, Multi-Cloud Governed. From Idea to Production.  
> **Version**: 3.0 | **Total Checks**: 285 | **Rule Identifiers**: 184  
> **Author**: [Bhaskar Puppala (PATEL)](https://www.linkedin.com/in/bhaskerkpatel/)  

This guide explains how to integrate and operationalize the **TriSuElla-AIDLCA Secure Development Framework** across your software lifecycle, whether you are a vibe coder prototyping an autonomous SaaS, an enterprise engineering team deploying to multi-cloud infrastructure, or a security architect enforcing automated DevSecOps and AI agent governance.

---

## 🏛️ What This Framework Is

The **TriSuElla-AIDLCA Framework** is a policy-as-code ruleset, automated gatekeeper, and multi-agent governance standard. It embeds security, privacy, compliance, and cloud posture into every phase of AI-accelerated development:

- 🔴 **SISU (Resilience & Execution)**: Deterministic, resilient execution across Inception, Construction, and Operations with automated rollback and fault tolerance.
- 🔵 **TILLIT (Trust, Zero-Trust & Compliance)**: Zero-Trust cryptographic identity, automated DPDPA/GDPR/EU AI Act/RBI compliance, and 100% auditable logging.
- 🟢 **DUGNAD (Orchestration & Human Collaboration)**: Multi-agent coordination with mandatory **Dual-Key Human-in-the-Loop (HITL)** approval gates.

The framework supports all modern IDEs, coding assistants, and CI/CD pipelines:
- **Cursor** (`.cursorrules`)
- **Claude Code & Claude Projects** (`CLAUDE.md`)
- **GitHub Copilot** (`.github/copilot-instructions.md`)
- **Windsurf** (`.windsurfrules`)
- **GitHub Actions CI/CD** (`.github/workflows/trisuella-gate.yml`)
- **Autonomous Multi-Agent Systems** (`TRISUELLA-AIDLCAa` zero-trust message envelopes)

---

## ⚡ Quick Start — 3 Minutes to Production Governance

### Step 1: Automated Scaffolding with `trisu-cli` (Recommended)

Run the zero-dependency Python CLI tool to scaffold all drop-in configs, state trackers, and CI gates into any repository:

```bash
# Initialize into target repository
python tools/trisu-cli/trisu_validator.py init --target /path/to/your-repo
```

This instantly creates:
- `.cursorrules` (Cursor AI directives)
- `CLAUDE.md` (Claude Code directives)
- `.windsurfrules` (Windsurf directives)
- `.github/copilot-instructions.md` (GitHub Copilot directives)
- `trisuella.config.yaml` (Project policy manifest with Multi-Cloud CSPM settings)
- `.pre-commit-config.yaml` (Local git commit blocker)
- `.github/workflows/trisuella-gate.yml` (CI/CD PR gate)
- `audit.md` & `TRISUELLA-AIDLCA-state.md` (State tracking)

---

### Step 2: Configure Your Project & Multi-Cloud Policy

Open `trisuella.config.yaml` and set your risk tier, compliance frameworks, and cloud providers:

```yaml
version: "3.0"
project:
  name: "My Secure AI Application"
  risk_tier: "tier_2" # tier_1 (critical), tier_2 (enterprise), tier_3 (standard)

compliance:
  active_frameworks:
    - "DPDPA-2023"
    - "GDPR"
    - "OWASP-LLM-Top-10-2025"
    - "EU-AI-Act-High-Risk"

cspm:
  enabled: true
  audit_interval: "continuous"
  providers:
    aws:
      enabled: true
      immutability_mode: "COMPLIANCE"
    azure:
      enabled: true
    gcp:
      enabled: true
    alibaba_cloud:
      enabled: false
    oci:
      enabled: false
```

---

### Step 3: Run Validation & Security Audits

Verify your repository health and export security findings to GitHub Code Scanning:

```bash
# 1. Verify artifact readiness and configuration integrity
python tools/trisu-cli/trisu_validator.py check

# 2. Run blocking security audits and export SARIF report
python tools/trisu-cli/trisu_validator.py audit --sarif audit.sarif

# 3. Generate a machine-readable CycloneDX AI v1.6 Bill of Materials (AI-BoM)
python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json

# 4. Verify rule integrity across all 184 TRISU-* identifiers
python tools/trisu-cli/trisu_validator.py rules
```

---

## 🎯 Integration Patterns by Use Case

### Pattern A: Vibe Coding & Solo Prototyping
For rapid, iterative prototyping with Cursor, Windsurf, or Claude:
1. Drop `.cursorrules` or `CLAUDE.md` into your workspace.
2. Start chatting: *"Follow TriSuElla-AIDLCA v3.0 rules. We are building [Project Description]."*
3. The AI co-pilot automatically conducts threat modeling, enforces input sanitization, and runs the **20-Item Security Review Checklist** at the end of each code generation turn.

### Pattern B: Enterprise Engineering Teams
For shared team repositories:
1. Commit `trisuella.config.yaml` to the repo root.
2. Install pre-commit hooks via `pre-commit install` (blocks commits containing unredacted API keys or failing checks).
3. Commit `.github/workflows/trisuella-gate.yml`. Pull Requests automatically run `trisu_validator.py audit` and block merges if `[CRITICAL]` or `[HIGH]` checks fail.

### Pattern C: Multi-Cloud Infrastructure & CSPM Auditing
For cloud-native deployments across AWS, Azure, GCP, Alibaba Cloud, and OCI:
1. Reference `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/security/cloud-security/cloud-security.md`.
2. Enforce the 14 **TRISU-CSPM** controls:
   - **KSPM**: Private K8s API servers and admission controllers (EKS, AKS, GKE, ACK, OKE).
   - **DSPM**: Private endpoints, TLS 1.3, TDE encryption (RDS, Cosmos, Cloud SQL, PolarDB, Autonomous DB).
   - **AI-CSPM / CWPP**: IMDSv2, private VPC perimeter for model endpoints (SageMaker, Azure OpenAI, Vertex AI, PAI, OCI GenAI).
   - **CIEM**: Revocation of dormant credentials and excessive permissions.
   - **Shift-Left IaC**: Pre-merge Terraform, Bicep, and CloudFormation scanning.

### Pattern D: Autonomous Multi-Agent Factory (`TRISUELLA-AIDLCAa`)
For autonomous software factories using specialized AI agents:
1. Deploy the 8-stage pipeline (`Planner`, `Designer`, `Builder`, `Tester`, `Releaser`, `Deployer`, `Monitor`, `Improver`).
2. Agents communicate via **TRISU-ZTP** zero-trust JSON envelopes.
3. Every deployment action requires signed **Dual-Key Human-in-the-Loop (HITL)** cryptographic approval before container push or cloud infrastructure modification.

---

## 📋 The 3 Development Phases

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TRISUELLA-AIDLCA v3.0                           │
├───────────────────┬────────────────────────────┬───────────────────────┤
│ Phase 1: INCEPTION│ Phase 2: CONSTRUCTION      │ Phase 3: OPERATIONS   │
│ (Plan & Model)    │ (Design, Code & Verify)    │ (Deploy & Observe)    │
├───────────────────┼────────────────────────────┼───────────────────────┤
│ • Workspace Scan  │ • Functional Design        │ • CI/CD PR Gates      │
│ • Requirements    │ • NFR & Cloud Architecture │ • Safe Deployment Plan│
│ • STRIDE Threat   │ • Secrets by Design        │ • Observability Setup │
│   Modeling (DREAD)│ • Code Gen + 20-Item Review│ • Incident Playbooks  │
│ • User Stories    │ • SAST/DAST/Secret Scans   │ • Automated Drift     │
│ • Unit Planning   │ • PyRIT / Garak AI Tests   │   Remediation         │
└───────────────────┴────────────────────────────┴───────────────────────┘
```

---

## 📁 Repository Directory Structure Reference

```
OWASP-TriSuElla-AIDLCA-FrameWork/
├── README.md                                    ← Main project entrypoint & quickstart (v3.0)
├── TRISUELLA_MASTER_RULES_AND_CHECKS.md         ← Unified master rulebook (285 checks, 184 rules)
├── ai-bom.json                                  ← Machine-readable CycloneDX AI v1.6 BoM
├── trisuella.config.yaml                        ← Declarative policy & CSPM manifest
├── CLAUDE.md & .cursorrules                     ← Workspace rules for Claude Code & Cursor
├── LICENSE                                      ← Open-source Apache-2.0 license
│
├── templates/                                   ← Drop-in developer configs & CI/CD workflows
│   ├── .cursorrules                             ← Cursor IDE rules template
│   ├── CLAUDE.md                                ← Claude Code instructions template
│   ├── .windsurfrules                           ← Windsurf rules template
│   ├── copilot-instructions.md                  ← GitHub Copilot instructions template
│   ├── trisuella.config.yaml                    ← Declarative policy manifest template
│   ├── .pre-commit-config.yaml                  ← Git pre-commit hook template
│   └── .github/workflows/trisuella-gate.yml     ← GitHub Actions CI/CD blocking gate
│
├── tools/                                       ← Governance tooling & runtime gatekeepers
│   ├── trisu-cli/
│   │   └── trisu_validator.py                   ← Zero-dependency CLI (check, audit, init, bom, rules)
│   └── sisu-ui/                                 ← Sisu Nexus visual compliance dashboard
│       ├── index.html                           ← Web UI dashboard interface
│       ├── sisu-ui-design-spec.md               ← UI/UX architecture & metrics specification
│       └── sample-data/                         ← Sample governance & compliance dataset
│
├── TRISUELLA-AIDLCAa/                           ← 8-Stage Autonomous Multi-Agent Governance
│   └── README.md                                ← Zero-Trust Protocol (ZTP), envelopes & Dual-Key HITL
│
├── TRISUELLA-AIDLCA-docs/                       ← Operational state tracking & crosswalk matrices
│   ├── TRISUELLA-AIDLCA-state.md                ← Runtime workflow state & extension tracking
│   └── AICM-AIDLCA-Crosswalk.md                 ← CSA AICM v1.0.3 to TriSuElla crosswalk
│
├── Data-Source/                                 ← Foundational regulatory baselines & standards
│   ├── AICMv1.0.3+AI_CAIQv1.0.2 bundle          ← CSA AI Control Matrix spreadsheets & guides
│   ├── Architecting_Cyber_Resilience_BFSI       ← RBI Cyber Resilience guidelines & manuscript
│   ├── FREE-AI_Committee_Report                 ← Responsible AI & ethical governance report
│   └── INDIAN_CYBERSECURITY                     ← CERT-In & statutory compliance references
│
└── TRISUELLA-AIDLCA-Rules/                      ← Core specifications, workflows & prompts
    ├── README.md                                ← Philosophy, severity scale & quick summary
    ├── CHARTER.md                               ← Strategic mission, foundational pillars & charter
    ├── FULL_README.md                           ← Comprehensive manual, CSPM crosswalk & changelog
    │
    ├── TRISUELLA-AIDLCA-rules/
    │   └── core-workflow.md                     ← Master TRISUELLA-AIDLCA workflow (all 3 phases)
    │
    ├── TRISUELLA-AIDLCA-rule-details/           ← Detailed rules per phase and extension
    │   ├── common/                              ← Loaded at every workflow start (11 files)
    │   ├── inception/                           ← Phase 1: Plan, model threats, design architecture
    │   ├── construction/                        ← Phase 2: Design, generate, test per unit
    │   ├── operations/                          ← Phase 3: Deploy, observe, respond
    │   └── extensions/                          ← Modular opt-in extensions
    │       ├── security/                        ← Baseline, AI-Agentic, Cloud/CSPM, Infra, Privacy, Data, Zero-Trust
    │       ├── compliance/                      ← DPDPA, India BFSI, AI-DLCA, GDPR, HIPAA, PCI-DSS
    │       └── testing/                         ← Property-Based Testing (PBT)
    │
    ├── prompts/                                 ← Turnkey prompt library across all stages
    │   ├── README.md                            ← Index of all prompt suites (P, B, T, A, C)
    │   ├── planning/                            ← Requirements & STRIDE threat model prompts
    │   ├── build/                               ← Secure code generation & review prompts
    │   ├── test/                                ← Security test & prompt injection prompts
    │   ├── ai-agents/                           ← AI/agentic feature design & MCP review prompts
    │   └── compliance/                          ← DPDPA, GDPR, HIPAA, PCI compliance prompts
    │
    └── docs/                                    ← Developer and architectural documentation
        ├── Usage-Guide.md                       ← Integration guide for all AI tools & IDEs (This File)
        ├── faq.md                               ← 25+ frequently asked questions
        ├── benefits.md                          ← Benefits by role & 4 real-world scenarios
        ├── vibe-coding-guide.md                 ← Fast-track guide for vibe coders
        ├── which-extensions.md                  ← Decision tree for extension selection
        └── adr-template.md                      ← Architecture Decision Record template
```

---

## 🧰 The Prompt Template Library

The `prompts/` directory contains 28 production-ready prompt templates:
- **Planning (`prompts/planning/`)**: Kickoff, requirements gathering, STRIDE/STRIDE-AI threat modeling, and architecture security review.
- **Build (`prompts/build/`)**: Secure API endpoint generation, security code review, hardened Dockerfiles, and database schemas.
- **Test (`prompts/test/`)**: API security testing, PyRIT/Garak prompt injection suites, dependency scanning, and secret audit setup.
- **AI Agents (`prompts/ai-agents/`)**: Secure LLM feature design, multi-agent pipeline setup, RAG data isolation, and Model Context Protocol (MCP) server review.
- **Compliance (`prompts/compliance/`)**: DPDPA compliance, GDPR gap assessment, HIPAA controls, and PCI-DSS scoping.

---

## 💡 Best Practices for Engineering Teams

1. **Never Bypass `[CRITICAL]` Blockers**: If the CLI or agent flags a blocking issue (e.g., hardcoded secret, missing authentication, non-isolated cloud storage), fix the root cause.
2. **Layer 1 First**: Ensure Cloud IAM, network perimeters, and secret management are hardened before obsessing over prompt injection guardrails.
3. **Automate in CI/CD**: Run `python tools/trisu-cli/trisu_validator.py audit` as a required GitHub Actions status check on all pull requests.
4. **Maintain the Audit Trail**: Ensure `audit.md` is committed alongside architectural changes for seamless SOC 2, ISO 42001, and DPDPA compliance evidence.

---

*OWASP TriSuElla-AIDLCA Secure Development Framework v3.0 — Security-First, AI-Native. Built for Agentic Autonomy.*
