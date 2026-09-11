# 📖 OWASP TriSuElla-AIDLCA Framework — Comprehensive Usage Guide (v3.0)

> **AI-Driven Development Life Cycle & Autonomous Agent Governance (LLMSecOps)**  
> **Version**: 3.0 | **Status**: Institutionalized | **Total Checks**: 285 | **Rules**: 184  
> **Author**: [Bhaskar Puppala (PATEL)](https://www.linkedin.com/in/bhaskerkpatel/)  
> **Repository**: [thundel/TriSuElla-AIDLCA-Framework](https://github.com/thundel/TriSuElla-AIDLCA-Framework) | [OWASP/OWASP-TriSuElla-AIDLCA-Framework](https://github.com/OWASP/OWASP-TriSuElla-AIDLCA-Framework)

---

## 🧭 Executive Summary & Core Philosophy

The **OWASP TriSuElla-AIDLCA Framework** is an enterprise-grade, policy-as-code standard that ensures AI-assisted code generation, autonomous agent workflows, and cloud-native deployments operate within deterministic, Zero-Trust, policy-governed boundaries.

Rooted in three Nordic and Finnish governance pillars:
- 🔴 **SISU (Resilience & Execution)**: Deterministic execution, automated crash recovery, non-negotiable safety invariants, and strict state rollbacks.
- 🔵 **TILLIT (Trust, Zero-Trust & Compliance)**: Mutual cryptographic authentication, non-human identity (NHI) federation, multi-cloud CSPM, and statutory compliance (DPDPA-2023, GDPR, EU AI Act, RBI Cyber Resilience, HIPAA, PCI-DSS).
- 🟢 **DUGNAD (Collaboration & Orchestration)**: Multi-agent coordination with **Dual-Key Human-in-the-Loop (HITL)** approval gates before irreversible actions.

The framework bridges the gap between fast-paced **vibe coding** and stringent **enterprise DevSecOps**, operating across 3 development phases:
1. **Phase 1: Inception** (Workspace scan, requirements gathering, STRIDE/STRIDE-AI threat modeling).
2. **Phase 2: Construction** (Secure system design, policy-governed code generation with a 20-item security checklist, SAST/DAST/secret audits, AI red-teaming).
3. **Phase 3: Operations** (CI/CD PR gating, safe canary deployments, multi-cloud CSPM drift remediation, and immutable incident playbooks).

---

## 🛠️ Step 1: Framework Setup into Your Development IDE of Choice

TriSuElla-AIDLCA is designed to be completely platform-agnostic and supports every major modern AI development environment.

### 1.1 Automated Scaffolding (Recommended — All IDEs in One Shot)

Run the zero-dependency Python CLI tool to scaffold all IDE configuration files, policy manifests, pre-commit hooks, and CI/CD pipelines into any repository with a single command:

```bash
# From the TriSuElla framework repository or your target project:
python tools/trisu-cli/trisu_validator.py init --target /path/to/your-project
```

This single command automatically generates:
1. `.cursorrules` — Active security directives for Cursor AI
2. `CLAUDE.md` — Active development and gatekeeper rules for Claude Code CLI and Claude Projects
3. `.windsurfrules` — Active directives for Windsurf Cascade
4. `.github/copilot-instructions.md` — Active system instructions for GitHub Copilot
5. `trisuella.config.yaml` — Declarative policy manifest and Multi-Cloud CSPM configuration
6. `.pre-commit-config.yaml` — Local Git pre-commit hook preventing secret leaks and critical violations
7. `.github/workflows/trisuella-gate.yml` — Automated CI/CD PR blocking gate
8. `audit.md` & `TRISUELLA-AIDLCA-state.md` — Compliance evidence & runtime tracking

---

### 1.2 IDE-Specific Manual Setup

If you prefer placing files manually or are customizing an existing workspace, use the following instructions for your specific IDE:

#### A. Cursor AI (`.cursorrules`)
1. Copy `templates/.cursorrules` to the root of your project:
   ```bash
   cp templates/.cursorrules /path/to/your-project/.cursorrules
   ```
2. **How it works in Cursor**:
   - Cursor automatically injects `.cursorrules` into the system prompt of both **Cursor Chat** (`Ctrl+L` / `Cmd+L`) and **Cursor Composer** (`Ctrl+I` / `Cmd+I`).
   - The AI co-pilot will automatically enforce Phase 1 threat modeling before generating new modules and execute the **20-Item Security Code Review Checklist** at the conclusion of every code edit.

#### B. Claude Code (CLI) & Claude Desktop / Projects (`CLAUDE.md`)
1. Copy `templates/CLAUDE.md` to your project root:
   ```bash
   cp templates/CLAUDE.md /path/to/your-project/CLAUDE.md
   ```
2. **For Claude Code CLI**:
   - When you launch `claude` in your terminal inside the repository, Claude Code automatically reads `CLAUDE.md` on startup as its persistent system instructions.
   - Claude Code will run `python tools/trisu-cli/trisu_validator.py check` before finishing sessions and block any `[CRITICAL]` violations.
3. **For Claude Projects (Web / Desktop)**:
   - Create a Project in Claude (claude.ai), click **Project Knowledge**, and upload `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md`.
   - In **Custom Instructions**, paste the contents of `templates/CLAUDE.md`.

#### C. GitHub Copilot (VS Code, JetBrains, Visual Studio)
1. Ensure the directory `.github` exists in your project root, then copy `templates/copilot-instructions.md`:
   ```bash
   mkdir -p /path/to/your-project/.github
   cp templates/copilot-instructions.md /path/to/your-project/.github/copilot-instructions.md
   ```
2. **How it works**:
   - GitHub Copilot Chat automatically loads `.github/copilot-instructions.md` as contextual rules for every prompt in VS Code and JetBrains IDEs.
   - When generating code, Copilot will enforce zero hardcoded secrets, input sanitization, parameterized queries, and least-privilege IAM patterns.

#### D. Windsurf IDE by Codeium (`.windsurfrules`)
1. Copy `templates/.windsurfrules` to your project root:
   ```bash
   cp templates/.windsurfrules /path/to/your-project/.windsurfrules
   ```
2. **How it works in Windsurf**:
   - Windsurf's **Cascade AI** agent automatically reads `.windsurfrules` to govern autonomous multi-file edits, terminal commands, and tool executions.

#### E. Google Antigravity IDE
1. Ensure `CLAUDE.md` is in the workspace root or create `.agents/rules/` inside your project root.
2. Antigravity automatically detects workspace rules and binds them into agent tool execution loops, preventing unsafe command execution and unvalidated file modifications.

#### F. Continue.dev / Cline / Roo Code / Aider (VS Code & JetBrains)
- **Continue.dev**: Open `~/.continue/config.json` and add `templates/CLAUDE.md` to the `systemMessage` or `rules` array.
- **Cline / Roo Code**: Paste the contents of `templates/CLAUDE.md` into the **Custom Instructions** textarea in the extension settings.
- **Aider**: Run aider with:
  ```bash
  aider --read templates/CLAUDE.md
  ```

---

### 1.3 Configuring the Policy Manifest (`trisuella.config.yaml`)

The `trisuella.config.yaml` file is the declarative source of truth for your project's security posture and compliance mandates. Customize it according to your deployment targets:

```yaml
version: "3.0"

project:
  name: "Enterprise GenAI Platform"
  risk_tier: "tier_2" # Options: tier_1 (critical/financial), tier_2 (enterprise), tier_3 (standard/internal)

compliance:
  active_frameworks:
    - "DPDPA-2023"              # Digital Personal Data Protection Act (India)
    - "GDPR"                    # General Data Protection Regulation (EU)
    - "EU-AI-Act-High-Risk"     # EU Artificial Intelligence Act (High-Risk Systems)
    - "OWASP-LLM-Top-10-2025"   # OWASP Top 10 for LLM Applications
    - "RBI-Cyber-Resilience"    # Reserve Bank of India BFSI Master Direction
    - "SOC-2-Type-II"           # Trust Services Criteria

# Full-Spectrum Multi-Cloud CSPM (TRISU-CSPM-01 to 14)
cspm:
  enabled: true
  audit_interval: "continuous"
  posture_domains:
    continuous_cis_benchmark: true
    workload_identity_federation: true
    immutable_worm_storage: true
    zero_trust_private_endpoints: true
    tamper_evident_audit_logging: true
    automated_drift_remediation: true
    dedicated_hsm_cmek: true
    sovereign_geofencing: true
    kspm_kubernetes_hardening: true
    dspm_database_protection: true
    ai_cspm_model_perimeter: true
    ciem_least_privilege: true
    edge_waf_ddos_shield: true
    shift_left_iac_validation: true

  providers:
    aws:
      enabled: true
      immutability_mode: "COMPLIANCE" # S3 Object Lock
      enforce_private_subnets: true
      require_kms_cmek: true
    azure:
      enabled: true
      defender_tier: "standard"
      require_managed_identity: true
    gcp:
      enabled: true
      scc_tier: "premium"
      enforce_vpc_service_controls: true
    alibaba_cloud:
      enabled: false
    oci:
      enabled: false

# AI & Agentic Governance (TRISU-AGNT & TRISU-LLM)
ai_governance:
  dual_key_hitl_required: true   # Require 2 human approvals for production release
  mcp_tool_approval: "explicit"  # Model Context Protocol explicit confirmation
  ai_bom_generation: true        # CycloneDX AI v1.6 output
  runtime_guardrails:
    input_content_filtering: true
    output_pii_redaction: true
    hallucination_threshold: 0.05
```

---

## ⚡ Step 2: Interactive AI Execution (How to Run it During Development)

Once your IDE rules are placed, TriSuElla governs every conversational turn between you and your AI assistant.

### 2.1 The 3-Phase Gatekeeper Workflow

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   AI DEVELOPMENT WITH TRISUELLA GATES (v3.0)                     │
├────────────────────────┬─────────────────────────────┬───────────────────────────┤
│ 1. INCEPTION           │ 2. CONSTRUCTION             │ 3. OPERATIONS             │
├────────────────────────┼─────────────────────────────┼───────────────────────────┤
│ Prompt: "Build auth"   │ AI writes code:             │ AI writes deployment:     │
│ 🛑 AI STOP GATE:       │ • Sanitizes all inputs      │ • Checks cloud posture    │
│ • Threat Model (STRIDE)│ • Zero hardcoded secrets    │ • Writes canary rollout   │
│ • Data classification  │ • Parameterized DB queries  │ • Enforces Dual-Key HITL  │
│ • Secret store design  │ 🛑 20-Item Security Review  │ 🛑 Pre-commit / CI Pass   │
└────────────────────────┴─────────────────────────────┴───────────────────────────┘
```

### 2.2 Example Interaction: What You Experience in the IDE

#### Phase 1: You request a feature
```text
User: "Create a FastAPI endpoint that takes user prompts, calls OpenAI GPT-4, and stores queries in PostgreSQL."
```

#### AI Response (TriSuElla Gate Enforced):
```text
Assistant: 
[TriSuElla v3.0 Gate — Phase 1: Inception Threat Model]
Before writing code, let's identify the threat boundaries for this feature:
1. Threat (STRIDE - Tampering/Injection): Malicious prompt injection via user input into the LLM context.
   -> Mitigation: Implement input sanitization and strict delimiter boundary wrapping.
2. Threat (Information Disclosure): OpenAI API key or PostgreSQL password leaked via environment variables or logs.
   -> Mitigation: AWS Secrets Manager / Azure Key Vault integration with Pydantic BaseSettings.
3. Threat (Elevation of Privilege): SQL injection via prompt storage.
   -> Mitigation: SQLAlchemy ORM parameterized statements with UUID primary keys.

Do you approve this threat model and architecture before I generate the code?
```

#### Phase 2: Generating Code & 20-Item Security Review
Once approved, the AI generates the code and appends the mandatory checklist:
```text
[TriSuElla 20-Item Security Code Review Checklist]
[PASS] 1. Input Validation: Pydantic schemas enforce type, max length (1000 chars), regex sanitization.
[PASS] 2. Injection Prevention: Parameterized SQLAlchemy queries; no raw string interpolation.
[PASS] 3. Secrets Management: Loaded from OS environment via SecretManager client; 0 hardcoded strings.
[PASS] 4. Authentication & RBAC: JWT Bearer token validated via OAuth2PasswordBearer.
[PASS] 5. LLM Safety (TRISU-LLM-01): System prompt isolated from user input; output sanitized for PII.
[PASS] 6. Logging & Telemetry: Query text masked; PII scrubbed before emitting to CloudWatch.
[RESULT]: 0 Critical, 0 High findings. Unit ready for local test verification.
```

---

## 🔍 Step 3: Running CLI Audits & Inspecting Results

The framework includes `tools/trisu-cli/trisu_validator.py`, a zero-dependency CLI written entirely in Python's standard library. It requires no `pip install` or external packages.

### 3.1 Command Reference

| Command | Purpose | When to Run | Output / Exit Code |
| :--- | :--- | :--- | :--- |
| `python tools/trisu-cli/trisu_validator.py check` | Verifies repository readiness, templates, and manifests | Before starting work | `0` = Ready, `1` = Missing templates |
| `python tools/trisu-cli/trisu_validator.py audit` | Scans workspace for hardcoded secrets, insecure patterns, and policy violations | During local dev & pre-commit | `0` = Clean, `1` = Blocking `[CRITICAL]` |
| `python tools/trisu-cli/trisu_validator.py audit --sarif audit.sarif` | Generates standardized OASIS SARIF v2.1.0 security report | In CI/CD pipelines & IDE SARIF viewers | Writes `audit.sarif` |
| `python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json` | Catalogs models, datasets, and pipelines into CycloneDX AI v1.6 Bill of Materials | Before release / deployment | Writes `ai-bom.json` |
| `python tools/trisu-cli/trisu_validator.py rules` | Validates master rules index and verifies all 184 `TRISU-*` identifiers | Post-update or audit verification | `0` = 184 rules valid |

---

### 3.2 Command Walkthrough & Sample Outputs

#### 1. Checking Repository Readiness
```bash
python tools/trisu-cli/trisu_validator.py check
```
**Sample Output:**
```text
======================================================================
  OWASP TriSuElla-AIDLCA Policy Gate Validator v3.0
  Framework Status: Institutionalized | Checks: 285 | Rules: 184
======================================================================
[*] Checking TriSuElla Framework artifacts and configuration...
  ✓ Configuration manifest present: trisuella.config.yaml
  ✓ Master rules index verified: TRISUELLA_MASTER_RULES_AND_CHECKS.md
  ✓ Drop-in template verified: .cursorrules
  ✓ Drop-in template verified: CLAUDE.md
  ✓ Drop-in template verified: .windsurfrules
  ✓ Drop-in template verified: .github/copilot-instructions.md
  ✓ Drop-in template verified: .pre-commit-config.yaml
  ✓ CI/CD workflow verified: .github/workflows/trisuella-gate.yml
  ✓ All core TriSuElla v3.0 artifacts and templates verified successfully.
```

#### 2. Running a Blocking Security Audit
```bash
python tools/trisu-cli/trisu_validator.py audit
```
**Sample Output (Clean Pass):**
```text
[*] Running static security and policy compliance audit on target directory...
  ✓ Audited 42 source and configuration files.
  ✓ Static secret scanning passed: 0 exposed private keys, bearer tokens, or cloud credentials.
  ✓ Insecure pattern scanning passed: No unparameterized queries or wildcard IAM statements.
  ✓ Blocking Audit Result: 0 Critical, 0 High findings. Policy gate PASSED.
```

**Sample Output (Blocked on Critical Violation):**
```text
[*] Running static security and policy compliance audit on target directory...
  [CRITICAL] Hardcoded AWS Secret Access Key discovered in src/cloud/deploy.py:Line 24
  [HIGH] Unsanitized prompt injection sink found in src/agent/tools.py:Line 89
  [HIGH] Insecure S3 bucket configuration with public read ACL in terraform/storage.tf:Line 12
  ----------------------------------------------------------------------
  Audit Summary: 1 Critical, 2 High, 0 Medium, 0 Low findings.
  FAILED: 3 blocking vulnerabilities must be resolved before proceeding.
```
*(CLI exits with code `1`, immediately halting local commits or CI/CD pipelines).*

---

### 3.3 Visualizing Results in IDE & Dashboard

#### A. Viewing SARIF Findings in VS Code
1. Generate the SARIF file:
   ```bash
   python tools/trisu-cli/trisu_validator.py audit --sarif audit.sarif
   ```
2. Install the free **SARIF Viewer** extension by Microsoft (`MS-SarifVSCode.sarif-viewer`).
3. Open `audit.sarif` in VS Code. Violations appear as clickable markers in your Problems panel (`Ctrl+Shift+M`), jumping directly to the offending file, line, and remediation guidance.

#### B. Sisu Nexus Visual Compliance Dashboard
The framework includes an interactive, browser-based single-page application dashboard located at `tools/sisu-ui/index.html`.
- Double-click `tools/sisu-ui/index.html` or open it directly in Google Chrome, Microsoft Edge, or Mozilla Firefox.
- **Features**:
  - Real-time **SISU/TILLIT/DUGNAD** posture breakdown.
  - Multi-Cloud CSPM 14-domain radar charts.
  - Live AI-agent audit trail with Dual-Key HITL authorization statuses.
  - Exportable executive compliance reports (PDF/JSON).

---

## 🚀 Step 4: DevSecOps & CI/CD Pipeline Integration

Embed TriSuElla-AIDLCA as an automated, non-negotiable security gatekeeper across your deployment pipelines.

### 4.1 Local Git Pre-Commit Hook (Prevent Leaks Before Push)

Install the pre-commit framework:
```bash
pip install pre-commit
pre-commit install
```

The included `.pre-commit-config.yaml` runs `trisu_validator.py audit` before every local commit:
```yaml
repos:
  - repo: local
    hooks:
      - id: trisuella-audit
        name: "TriSuElla-AIDLCA v3.0 Security & Policy Audit"
        entry: python tools/trisu-cli/trisu_validator.py audit
        language: system
        pass_filenames: false
        always_run: true
```
If an engineer or AI assistant inadvertently includes a secret key or unvalidated sink, `git commit` is immediately rejected on the developer's workstation.

---

### 4.2 GitHub Actions (Automated PR Gating & Code Scanning)

Use `templates/.github/workflows/trisuella-gate.yml` in your repository at `.github/workflows/trisuella-gate.yml`:

```yaml
name: "TriSuElla-AIDLCA Security & Policy Gate"

on:
  push:
    branches: [ "main", "master", "develop" ]
  pull_request:
    branches: [ "main", "master" ]

jobs:
  trisuella-gate:
    name: "Enforce TriSuElla v3.0 Gates"
    runs-on: ubuntu-latest

    permissions:
      contents: read
      security-events: write # Required for SARIF upload
      pull-requests: write

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Verify Framework Artifacts & Templates
        run: |
          python tools/trisu-cli/trisu_validator.py check

      - name: Audit for Blocking [CRITICAL]/[HIGH] Findings & Generate SARIF
        run: |
          python tools/trisu-cli/trisu_validator.py audit --sarif trisuella-audit.sarif

      - name: Generate CycloneDX AI v1.6 Bill of Materials (AI-BoM)
        run: |
          python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json

      - name: Upload SARIF Report to GitHub Code Scanning
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: trisuella-audit.sarif
          category: trisuella-security-gate

      - name: Archive AI-BoM Artifact
        uses: actions/upload-artifact@v4
        with:
          name: ai-bom-cyclonedx
          path: ai-bom.json
```

**Results in GitHub**:
- Pull Requests with `[CRITICAL]` or `[HIGH]` findings are blocked from merging.
- Detailed findings appear under the repository's **Security -> Code scanning alerts** tab.
- The `ai-bom.json` artifact is archived with each build for supply chain provenance.

---

### 4.3 GitLab CI/CD Pipeline (`.gitlab-ci.yml`)

For teams using GitLab, add this job to `.gitlab-ci.yml`:

```yaml
stages:
  - test
  - security-audit

trisuella_security_gate:
  stage: security-audit
  image: python:3.11-slim
  script:
    - python tools/trisu-cli/trisu_validator.py check
    - python tools/trisu-cli/trisu_validator.py audit --sarif trisuella-audit.sarif
    - python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json
  artifacts:
    reports:
      sast: trisuella-audit.sarif
    paths:
      - trisuella-audit.sarif
      - ai-bom.json
    when: always
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
```

---

### 4.4 Azure DevOps Pipelines (`azure-pipelines.yml`)

For teams using Azure DevOps:

```yaml
trigger:
  - main
pr:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.11'
  displayName: 'Use Python 3.11'

- script: |
    python tools/trisu-cli/trisu_validator.py check
    python tools/trisu-cli/trisu_validator.py audit --sarif $(Build.ArtifactStagingDirectory)/trisuella-audit.sarif
    python tools/trisu-cli/trisu_validator.py bom --output $(Build.ArtifactStagingDirectory)/ai-bom.json
  displayName: 'Run TriSuElla v3.0 Policy Gate'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'trisuella-reports'
    publishLocation: 'Container'
  condition: always()
```

---

### 4.5 Multi-Cloud Shift-Left IaC Security Scan

Incorporate Infrastructure-as-Code (IaC) linting alongside TriSuElla rules in CI/CD before any cloud deployment:

```bash
# Scan Terraform / CloudFormation / Bicep for CSPM compliance
checkov -d ./terraform --framework terraform --check CKV_AWS_18,CKV_AWS_19,CKV_AWS_145
```

The 14 **TRISU-CSPM** controls validated include:
1. **TRISU-CSPM-01**: CIS Benchmark Level 2 continuous compliance.
2. **TRISU-CSPM-02**: Non-Human Identity (NHI) federation via OIDC (no long-lived secret keys).
3. **TRISU-CSPM-03**: Storage WORM lock with Compliance Retention (S3, Azure Blob, GCS Bucket Lock).
4. **TRISU-CSPM-04**: Zero-Trust network perimeters (AWS PrivateLink, Azure Private Link, GCP PSC).
5. **TRISU-CSPM-05**: Multi-region tamper-evident audit logging with 365-day retention.
6. **TRISU-CSPM-06**: Automated configuration drift remediation.
7. **TRISU-CSPM-07**: Dedicated Customer-Managed Encryption Keys (CMEK) via Cloud HSM.
8. **TRISU-CSPM-08**: Sovereign geofencing restricting regions to statutory jurisdictions.
9. **TRISU-CSPM-09**: Kubernetes (KSPM) private API endpoints and non-root admission controls.
10. **TRISU-CSPM-10**: Database (DSPM) private VPC binding, TLS 1.3, and column-level encryption.
11. **TRISU-CSPM-11**: AI-CSPM model endpoint private perimeters (SageMaker, Azure OpenAI, Vertex AI).
12. **TRISU-CSPM-12**: Cloud Infrastructure Entitlement Management (CIEM) least-privilege scoping.
13. **TRISU-CSPM-13**: Layer 7 Edge WAF and managed anti-DDoS shielding.
14. **TRISU-CSPM-14**: Shift-Left IaC security scanning blocking unencrypted infrastructure PRs.

---

## 🤖 Step 5: Multi-Agent Governance (`TRISUELLA-AIDLCAa`)

When operating autonomous agent swarms (e.g., using CrewAI, AutoGen, LangGraph, or custom agent runtimes), TriSuElla provides the **TRISU-ZTP Zero-Trust Envelope Protocol**:

```json
{
  "sender": "BuilderAgent",
  "receiver": "TesterAgent",
  "task_id": "TASK-84920",
  "state_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "payload": {
    "unit_id": "AUTH-01",
    "git_commit": "4f9d2a1",
    "security_review": "PASSED_20_OF_20"
  },
  "signature": "ed25519:3f982...b0c4"
}
```

### Dual-Key Human-in-the-Loop (HITL) Gate

No autonomous agent is permitted to deploy to production, modify production databases, or publish API keys. The **DeployerAgent** halts execution until two distinct cryptographic or signed approvals are registered in `audit.md`:

```markdown
### 🛡️ Production Release HITL Approval Block
- **Release Target**: v3.0.0 (Container: `registry.internal/api:v3.0.0`)
- **Key 1 (Security Lead)**: Approved by `sec-lead@company.internal` (GPG: `0x7A9B21...`)
- **Key 2 (Engineering Lead)**: Approved by `eng-lead@company.internal` (GPG: `0x8C1F42...`)
- **Status**: RELEASE AUTHORIZED
```

---

## ❓ Frequently Asked Questions & Troubleshooting

### Q: Does running the framework slow down AI generation?
**A**: No. TriSuElla guidelines operate as structural prompt context. Modern LLMs (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) follow these Markdown rules natively, outputting secure code on the first attempt and eliminating the rework cycle typically required after security scans fail.

### Q: How do I handle false positives in `trisu_validator.py audit`?
**A**: Add approved exception fingerprints to `trisuella.config.yaml` under the `audit_exceptions` block with a business justification and expiration timestamp.

### Q: Can I use this framework with local LLMs (e.g., Ollama / vLLM)?
**A**: Yes. Provide `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md` as the system instruction when running models like Llama 3, Mistral, or Qwen.

---

## 📚 Key Reference Documents

- **Master Rules Specification (285 Checks, 184 Rules)**: [TRISUELLA_MASTER_RULES_AND_CHECKS.md](TRISUELLA_MASTER_RULES_AND_CHECKS.md)
- **Detailed Developer Manual & CSPM Crosswalk**: [TRISUELLA-AIDLCA-Rules/FULL_README.md](TRISUELLA-AIDLCA-Rules/FULL_README.md)
- **Framework Philosophy & Charter**: [TRISUELLA-AIDLCA-Rules/CHARTER.md](TRISUELLA-AIDLCA-Rules/CHARTER.md)
- **Turnkey Prompt Library (28 Prompts)**: [TRISUELLA-AIDLCA-Rules/prompts/README.md](TRISUELLA-AIDLCA-Rules/prompts/README.md)
- **Autonomous Multi-Agent Architecture**: [TRISUELLA-AIDLCAa/README.md](TRISUELLA-AIDLCAa/README.md)
- **Visual Compliance Dashboard**: [tools/sisu-ui/index.html](tools/sisu-ui/index.html)

---

*OWASP TriSuElla-AIDLCA Secure Development Framework v3.0 — Security-First, AI-Native. Built for Agentic Autonomy.*
