# 🤖 TRISUELLA-AIDLCAa: Multi-Agent Autonomous Development & Governance System
**Version**: 2.5 | **Status**: Production Architecture | **Pillars**: SISU, TILLIT, DUGNAD

> **TRISUELLA-AIDLCAa** (AI-Driven Development Life Cycle Agents) is the automated multi-agent implementation of the TriSuElla framework. It translates the 285 governance rules and sequential lifecycle gates into a coordinated pipeline of specialized autonomous agents operating under a Zero-Trust orchestration fabric.

---

## 🏛️ Architectural Overview

While individual developers can use the TriSuElla rules as system prompts for single AI coding assistants (Cursor, Claude, Copilot), enterprise teams and autonomous software factories deploy **TRISUELLA-AIDLCAa** as an 8-stage agent pipeline:

```mermaid
graph TD
    subgraph "TRISUELLA-AIDLCAa Orchestration Fabric (Zero Trust Bus)"
        P1[1. Planner Agent<br/>STRIDE & Scope] --> P2[2. Designer Agent<br/>NFR & Architecture]
        P2 --> P3[3. Builder Agent<br/>Secure Code Gen]
        P3 --> P4[4. Tester Agent<br/>PyRIT / Garak / SAST]
        P4 --> P5[5. Releaser Agent<br/>AI-BoM & Syft Sign]
        P5 --> P6[6. Deployer Agent<br/>Dual-Key HITL Gate]
        P6 --> P7[7. Monitor Agent<br/>Drift & Telemetry]
        P7 --> P8[8. Improver Agent<br/>Continuous Hardening]
        P8 -.-> P1
    end

    HITL[👤 Human Steward Gatekeeper] --> P6
    HITL -.-> P1
```

---

## 🤖 The 8 Specialized Lifecycle Agents

| # | Agent Name | Phase | Primary Responsibilities | Mandatory Output Artifacts |
|---|---|---|---|---|
| **1** | **Planner Agent** | Inception | Requirements elicitation, scope bounding, STRIDE-AI threat modeling, intent precision. | `threat-model.md`, `requirements-matrix.md` |
| **2** | **Designer Agent** | Architecture | Microservices, API contracts, NFR specs, zero-trust network boundaries, secrets architecture. | `architecture-spec.md`, `nfr-checklist.md` |
| **3** | **Builder Agent** | Construction | Deterministic, secure code generation, adherence to the 20-item security code review checklist. | Source code, `Dockerfile`, `migration.sql` |
| **4** | **Tester Agent** | Verification | SAST/DAST orchestration, secret scanning, adversarial jailbreak testing (Garak/PyRIT), fuzzing. | `security-test-report.md`, `sast-results.sarif` |
| **5** | **Releaser Agent** | Packaging | AI Bill of Materials (AI-BoM) generation via Syft/CycloneDX, Cosign cryptographic signing. | `ai-bom.json`, `cosign.sig` |
| **6** | **Deployer Agent** | Deployment | Immutable environment verification, canary rollout execution, **Dual-Key HITL approval gate**. | `deployment-receipt.json`, `audit-log.md` |
| **7** | **Monitor Agent** | Operations | PSI/K-S statistical drift tracking, semantic guardrail breach alarms, circuit breaker tripping. | `drift-metrics.json`, `alerts.log` |
| **8** | **Improver Agent** | Feedback | Post-incident analysis, prompt regression tests, automated policy refinement. | `hardening-patch.diff`, `post-mortem.md` |

---

## 🛡️ Zero-Trust Inter-Agent Communication Protocol (TRISU-ZTP)

All inter-agent message exchanges MUST pass through the tamper-evident message envelope:

```json
{
  "$schema": "https://trisuella.org/schemas/agent-envelope-v2.5.json",
  "envelope_id": "env_9f83a2c4-7b1e-4209-8431",
  "timestamp": "2026-04-01T12:00:00Z",
  "source_agent": {
    "role": "BuilderAgent",
    "instance_id": "builder-01-prod",
    "spiffe_id": "spiffe://trisuella.internal/ns/dev/sa/builder"
  },
  "destination_agent": {
    "role": "TesterAgent",
    "instance_id": "tester-01-prod",
    "spiffe_id": "spiffe://trisuella.internal/ns/dev/sa/tester"
  },
  "lifecycle_phase": "Phase 4 - Test & Evaluation",
  "payload": {
    "target_commit": "a1b2c3d4e5f6",
    "artifacts": ["src/", "Dockerfile", "tests/"]
  },
  "governance_checkpoint": {
    "blocking_findings": 0,
    "audit_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "signature": "MEUCIQDx...cosign-signature..."
}
```

---

## 🚦 Dual-Key Human-in-the-Loop (HITL) Gate

Under the **DUGNAD** pillar, no agent possesses unilateral authority to deploy AI model weights, alter production IAM, or waive `[CRITICAL]` security findings.

- **Gate 1 (Technical Sign-off)**: Primary Architect or Lead Security Engineer cryptographic authorization.
- **Gate 2 (Compliance Sign-off)**: Data Protection Officer (DPO) or Compliance Steward approval.

---

## 🚀 Getting Started with TRISUELLA-AIDLCAa

### Prerequisites
- Python 3.11+ or Node.js 20+
- OIDC / Workload Identity provider (e.g. SPIFFE/SPIRE or HashiCorp Vault)
- Container runtime (Docker / Podman)

### Configuration Example (`trisuella-agents.yaml`)
```yaml
version: "2.5"
orchestrator:
  mode: strict-zero-trust
  audit_file: "./audit.md"
  state_file: "./TRISUELLA-AIDLCA-state.md"

agents:
  planner:
    model: "claude-3-7-sonnet"
    threat_model_framework: "STRIDE-AI"
  builder:
    model: "claude-3-7-sonnet"
    rules_path: "./TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md"
  tester:
    tools: ["garak", "pyrit", "semgrep", "trufflehog"]
    blocking_severity: ["CRITICAL", "HIGH"]
  deployer:
    dual_key_required: true
    stewards:
      - "sec-lead@company.internal"
      - "compliance-dpo@company.internal"
```

---

## 📚 Architectural Standards & Invariants
- 🔐 **Agentic Identity & Delegation**: See [TRISU-AIAM](../TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/security/zero-trust/agentic-iam.md) for RFC 8693 token exchange and SPIFFE/mTLS workload identity specifications.
- 🔌 **Tool & MCP Sandboxing**: See [TRISU-MCP](../TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/security/ai-agentic/mcp-security.md) for runtime tool sandboxing and parameter sanitization.
- 📋 **Master Governance Reference**: Consult [TRISUELLA_MASTER_RULES_AND_CHECKS.md](../TRISUELLA_MASTER_RULES_AND_CHECKS.md) (285 Checks) and [CHARTER.md](../TRISUELLA-AIDLCA-Rules/CHARTER.md).
