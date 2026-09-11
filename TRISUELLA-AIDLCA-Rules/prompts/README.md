# TRISUELLA-AIDLCA Prompt Template Library
> **Version**: 2.5 | **Status**: Production Library | **Mapped Checks**: 285  
> **TRISUELLA-AIDLCA SDF** — Security-first, AI-native. From idea to production.

Copy-paste ready prompts for every stage of the TRISUELLA-AIDLCA workflow. Use these with any AI coding assistant — Claude, ChatGPT, Copilot Chat, Cursor, Windsurf — to get structured, security-aware outputs.

**How to use**: Find the stage you are working on. Copy the relevant prompt. Replace `[BRACKETED]` placeholders with your project details. Paste into your AI assistant.

For the best results, these prompts assume the TRISUELLA-AIDLCA SDF core rules are already loaded in your AI tool's system prompt or project instructions. If they are not, load `TRISUELLA-AIDLCA-rules/core-workflow.md` first.

---

## Prompt Categories

| Category | File | What it covers |
|---|---|---|
| Planning | [planning/requirements-and-threat-model.md](planning/requirements-and-threat-model.md) | Project kickoff (P-01), requirements deep dive (P-02), STRIDE threat model (P-03), user stories with security ACs (P-04), architecture review (P-05) |
| Build | [build/secure-code-generation.md](build/secure-code-generation.md) | Secure API endpoint (B-01), security code review (B-02), secure Dockerfile (B-03), secure DB schema (B-04), refactor for security (B-05), auth implementation (B-06) |
| Test | [test/security-testing.md](test/security-testing.md) | API security tests (T-01), prompt injection tests (T-02), dependency scan setup (T-03), secret scan setup (T-04), AI model evaluation (T-05), infra security checklist (T-06) |
| AI / Agents | [ai-agents/ai-agent-security-prompts.md](ai-agents/ai-agent-security-prompts.md) | Secure LLM feature design (A-01), multi-agent system design (A-02), RAG security design (A-03), LLM output validation (A-04), prompt template review (A-05), MCP server security review (A-06) |
| Compliance | [compliance/compliance-prompts.md](compliance/compliance-prompts.md) | GDPR checklist (C-01), DPDPA compliance check (C-02), HIPAA gap assessment (C-03), PCI-DSS scoping (C-04), data subject rights workflow (C-05) |

---

## Quick Reference by Task

**Starting a new project** → P-01 (Project Kickoff) then P-03 (STRIDE Threat Model)

**Generating a new API endpoint** → B-01 (Secure API Endpoint)

**Reviewing existing code for security** → B-02 (Security Code Review)

**Setting up a Docker container** → B-03 (Secure Dockerfile)

**Adding authentication** → B-06 (Auth Implementation)

**Writing security tests** → T-01 (API Security Tests)

**Testing an AI feature for prompt injection** → T-02 (Prompt Injection Test Suite)

**Setting up secret scanning in CI/CD** → T-04 (Secret Scan Setup)

**Designing an LLM-powered feature** → A-01 (Secure LLM Feature Design)

**Designing a multi-agent system** → A-02 (Secure Multi-Agent System Design)

**Securing a RAG pipeline** → A-03 (RAG Security Design)

**Reviewing an MCP server** → A-06 (MCP Server Security Review) & `extensions/security/ai-agentic/mcp-security.md`

**GDPR compliance check on a feature** → C-01 (GDPR Compliance Checklist)

**DPDPA check for Indian users** → C-02 (DPDPA Compliance Check)

**EU AI Act High-Risk assessment** → `extensions/compliance/compliance-eu-ai-act.md` (Articles 9–15)

**PCI-DSS scope assessment** → C-04 (PCI-DSS Scoping)

**Designing a data deletion/erasure workflow** → C-05 (Data Subject Rights Response Workflow)

---

## ⚡ Automated Tooling Tip
Instead of manually evaluating prompts, you can generate an automated CycloneDX AI v1.6 Bill of Materials of all prompt templates and dependencies using:
```bash
python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json
```

## Total: 28+ prompts across 5 categories | Mapped to 258 Master Invariants
