# 📖 How to Use the OWASP TriSuElla-AIDLCA Framework (v3.0)

> **AI-Driven Development Life Cycle & Autonomous Agent Governance (LLMSecOps)**  
> **Version**: 3.0 | **Status**: Institutionalized | **Total Checks**: 285 | **Rules**: 184  
> **Author**: [Bhaskar Puppala (PATEL)](https://www.linkedin.com/in/bhaskerkpatel/)  
> **Detailed Docs**: [TRISUELLA-AIDLCA-Rules/docs/how-to-use.md](TRISUELLA-AIDLCA-Rules/docs/how-to-use.md)

---

## 🧭 Executive Summary

The **OWASP TriSuElla-AIDLCA Framework** ensures that AI-assisted code generation, autonomous agent workflows, and cloud-native deployments operate within deterministic, Zero-Trust, policy-governed boundaries.

Rooted in the three pillars:
- 🔴 **SISU (Resilience & Execution)**: Deterministic execution, crash recovery, and safety invariants.
- 🔵 **TILLIT (Trust, Zero-Trust & Compliance)**: Zero-Trust verification, multi-cloud CSPM, DPDPA, GDPR, and EU AI Act compliance.
- 🟢 **DUGNAD (Collaboration & Orchestration)**: Multi-agent coordination with **Dual-Key Human-in-the-Loop (HITL)** gates.

---

## ⚡ 30-Second Turnkey Setup

### Option 1: Automated Scaffolding with `trisu-cli` (Recommended)

Run the zero-dependency Python CLI to instantly initialize TriSuElla in any existing project or repository:

```bash
# Scaffold into current directory or target project
python tools/trisu-cli/trisu_validator.py init --target .
```

This automatically generates:
1. `.cursorrules` — Active directives for Cursor AI
2. `CLAUDE.md` — Active directives for Claude Code & Claude Projects
3. `.windsurfrules` — Active directives for Windsurf
4. `.github/copilot-instructions.md` — Active directives for GitHub Copilot
5. `trisuella.config.yaml` — Declarative policy manifest and Multi-Cloud CSPM configuration
6. `.pre-commit-config.yaml` — Local Git pre-commit hook blocking secret leaks and critical violations
7. `.github/workflows/trisuella-gate.yml` — Automated CI/CD PR blocking gate
8. `audit.md` & `TRISUELLA-AIDLCA-state.md` — Compliance evidence & runtime tracking

---

### Option 2: Drop-in Integration via Templates

If you prefer manual placement, copy the ready-to-use templates from `templates/`:
- **Cursor**: Copy `templates/.cursorrules` to your project root.
- **Claude Code**: Copy `templates/CLAUDE.md` to your project root.
- **GitHub Copilot**: Copy `templates/copilot-instructions.md` to `.github/copilot-instructions.md`.
- **Windsurf**: Copy `templates/.windsurfrules` to your project root.
- **Policy Config**: Copy `templates/trisuella.config.yaml` to your project root.

---

### Option 3: Direct Prompt / Assistant Instructions

Add the following directive to your AI tool's system prompt or custom instructions:
> *"Always follow the OWASP TriSuElla-AIDLCA v3.0 secure development workflow defined in TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md. Enforce the 20-item Security Code Review Checklist on all code generation turns and block any [CRITICAL] or [HIGH] violations."*

---

## 🛠️ CLI Operations & Gatekeeper Commands

The `tools/trisu-cli/trisu_validator.py` script requires no third-party dependencies (pure Python standard library):

```bash
# 1. Structural Readiness Check
python tools/trisu-cli/trisu_validator.py check

# 2. Blocking Security Audit & SARIF Export (GitHub Code Scanning)
python tools/trisu-cli/trisu_validator.py audit --sarif audit.sarif

# 3. CycloneDX AI v1.6 Bill of Materials (AI-BoM) Generation
python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json

# 4. Master Rule Index Verification (184 unique TRISU-* rule IDs)
python tools/trisu-cli/trisu_validator.py rules
```

---

## ☁️ Multi-Cloud CSPM & Auditing (`TRISU-CSPM`)

The framework enforces 14 enterprise-grade Cloud Security Posture Management (CSPM) controls across the top 5 cloud providers:

| Domain / Control | AWS | Microsoft Azure | Google Cloud (GCP) | Alibaba Cloud (Aliyun) | Oracle Cloud (OCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Continuous CSPM & CIS** | Security Hub (CIS L2) | Defender for Cloud | SCC Premium | Security Center Enterprise | Cloud Guard & Security Zones |
| **Workload IAM / NHI** | Roles Anywhere / OIDC | Workload Identity | Workload Identity Fed | RAM Role SSO / OIDC | Workload Principals |
| **Storage WORM Lock** | S3 Object Lock (Compliance) | Blob Immutability Policy | GCS Bucket Lock | OSS WORM Retention Policy | Object Storage Retention Rules |
| **Zero-Trust Perimeter** | PrivateLink & VPC Endpoints | Private Link / Endpoints | Private Service Connect | VPC PrivateZone / PrivateLink | Service Gateway / Endpoints |
| **Tamper-Evident Audit** | CloudTrail Multi-Region | Azure Monitor Logs | Cloud Audit Logs (Admin+Data) | ActionTrail Multi-Region | Audit Service (365-day) |
| **Drift Self-Healing** | Config Conformance Packs | Policy DeployIfNotExists | Eventarc + Cloud Functions | Cloud Config Auto-Remediation | Event Service + Functions |
| **Dedicated HSM / CMEK** | KMS (CMEK) / CloudHSM | Key Vault Managed HSM | Cloud KMS / Cloud HSM | KMS Hardware HSM | Vault Dedicated KMS (FIPS L3) |
| **Sovereignty Geofencing** | SCP `aws:RequestedRegion` | Policy `allowed-locations` | Org Policy `resourceLocations`| Resource Mgmt Control Policy | Security Zones Region Policy |
| **KSPM (Kubernetes)** | EKS (Private Endpoint) | AKS (Private Cluster) | GKE (Private Cluster) | ACK (Private Cluster) | OKE (Private API Server) |
| **DSPM (Databases)** | RDS/Aurora (Private VPC) | Azure SQL/Cosmos DB | Cloud SQL/Spanner (Private IP) | PolarDB/ApsaraDB (VPC White) | Autonomous DB (Private IP) |
| **AI-CSPM / CWPP** | SageMaker Private VPC | Azure OpenAI Private Link | Vertex AI VPC SC | PAI Private Link | OCI GenAI Private Endpoints |
| **CIEM (Entitlements)** | IAM Access Analyzer | Entra Permissions Mgmt | IAM Recommender | RAM ActionTrail Analyzer | IAM Policy Recommender |
| **Edge WAF & Anti-DDoS** | AWS WAF v2 + Shield Adv | Azure WAF v2 + DDoS | Cloud Armor (L7 WAF) | WAF 3.0 + Anti-DDoS Pro | OCI WAF + DDoS Protection |
| **Shift-Left IaC Scan** | Checkov / cfn-guard | Checkov / Bicep Linter | Checkov / KICS / gcloud | Checkov / Terraform Alibaba | Checkov / OCI TF Validator |

---

## 🤖 Multi-Agent Orchestration (`TRISUELLA-AIDLCAa`)

For automated development pipelines, deploy the 8-agent zero-trust pipeline:
1. **Planner**: Scope definition, STRIDE & STRIDE-AI threat modeling.
2. **Designer**: NFR mapping, Cloud/CSPM architecture, Secrets by Design.
3. **Builder**: Policy-governed code generation + 20-item security review.
4. **Tester**: SAST, DAST, secret scanning, PyRIT / Garak AI red-teaming.
5. **Releaser**: AI-BoM cataloging, CycloneDX v1.6 generation, Cosign signing.
6. **Deployer**: Dual-Key Human-in-the-Loop (HITL) gate & canary rollout.
7. **Monitor**: Continuous drift detection, telemetry, and audit validation.
8. **Improver**: Automated patch synthesis and continuous hardening.

---

## 📚 Key Reference Documents

- **Master Rules Specification (285 Checks)**: [TRISUELLA_MASTER_RULES_AND_CHECKS.md](TRISUELLA_MASTER_RULES_AND_CHECKS.md)
- **Detailed Developer Manual & Crosswalk**: [TRISUELLA-AIDLCA-Rules/FULL_README.md](TRISUELLA-AIDLCA-Rules/FULL_README.md)
- **Framework Philosophy & Charter**: [TRISUELLA-AIDLCA-Rules/CHARTER.md](TRISUELLA-AIDLCA-Rules/CHARTER.md)
- **Step-by-Step Integration Guide**: [TRISUELLA-AIDLCA-Rules/docs/how-to-use.md](TRISUELLA-AIDLCA-Rules/docs/how-to-use.md)
- **Turnkey Prompt Library (28 Prompts)**: [TRISUELLA-AIDLCA-Rules/prompts/README.md](TRISUELLA-AIDLCA-Rules/prompts/README.md)
- **Autonomous Multi-Agent Architecture**: [TRISUELLA-AIDLCAa/README.md](TRISUELLA-AIDLCAa/README.md)
- **Visual Compliance Dashboard**: [tools/sisu-ui/index.html](tools/sisu-ui/index.html)

---

*OWASP TriSuElla-AIDLCA Secure Development Framework v3.0 — Security-First, AI-Native. Built for Agentic Autonomy.*
