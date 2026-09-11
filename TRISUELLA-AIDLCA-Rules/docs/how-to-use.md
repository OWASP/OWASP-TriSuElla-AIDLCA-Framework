# How to Use the TRISUELLA-AIDLCA Secure Development Framework

> **TRISUELLA-AIDLCA SDF** — Security-first, AI-native. From idea to production.

This guide explains how to integrate the TRISUELLA-AIDLCA Secure Development Framework into your development workflow, whether you are a vibe coder building a product with AI tools, a developer using an AI coding assistant, or a team lead establishing security standards for an AI-accelerated project.

---

## What This Framework Is

The TRISUELLA-AIDLCA Secure Development Framework is a **rules kit for AI coding assistants and agent systems**. It tells the AI how to behave during each phase of software development — from requirements through deployment — so that security, privacy, and compliance are embedded by default, not bolted on at the end.

Think of it as a set of standing instructions that you give your AI coding assistant once, and it follows throughout the project. Instead of remembering to ask "did you add input validation?" or "are any secrets hardcoded?" on every feature, the AI knows to enforce these standards automatically.

The framework works with any AI coding tool that accepts system prompts or custom instructions:
- **Claude** (claude.ai, Claude API, Claude Code)
- **ChatGPT / GPT-4** (custom instructions or system prompt)
- **GitHub Copilot Chat** (custom instructions in `.github/copilot-instructions.md`)
- **Cursor** (rules via `.cursorrules` or the Rules for AI setting)
- **Windsurf / Codeium** (custom AI instructions)
- **Any OpenAI-compatible API** (system message)
- **Custom agents built with LangChain, LlamaIndex, or the Claude Agent SDK**

---

## Quick Start — 3 Steps

### Step 1: Load the core rules into your AI assistant

Copy the contents of `TRISUELLA-AIDLCA-rules/core-workflow.md` into your AI tool's system prompt or custom instructions field, or simply copy the ready-to-use templates from the `templates/` directory into your project root:

- **For Cursor**: copy `templates/.cursorrules` to your project root.
- **For Claude Code / Claude Projects**: copy `templates/CLAUDE.md` to your project root.
- **For GitHub Copilot**: copy `templates/copilot-instructions.md` to `.github/copilot-instructions.md`.
- **For Windsurf**: copy `templates/.windsurfrules` to your project root.
- **For Project Policy Configuration**: customize `templates/trisuella.config.yaml` to set active compliance tiers and blocking rules.

### Step 2: Choose your extensions

The core rules cover the security baseline. Extensions add depth for specific topics. You only load what your project needs — keeping context lean and focused.

Look at your project and answer the questions in `docs/which-extensions.md` — it walks you through 8 yes/no questions that map directly to the right extensions. The quick summary:

- Does it use AI/ML models, LLMs, or agents? → Load `ai-agentic-security.md`
- Does it store or process sensitive information (PII, health, financial, children's data)? → Load `sensitive-data-security.md`
- Does it need to comply with GDPR, HIPAA, PCI-DSS, DPDPA, SOC 2, or ISO 27001? → Load `compliance-mapping.md`
- Does it have infrastructure (Docker, Kubernetes, CI/CD, cloud)? → Load `infra-security.md`
- Does it run on cloud (AWS, Azure, GCP)? → Load `cloud-security.md`
- Is it a multi-tenant system, multi-agent pipeline, or regulated enterprise product? → Load `zero-trust.md`
- Does it use privacy-by-design patterns (consent, data minimisation, purpose limitation)? → Load `privacy-secure-design.md`

For each extension you choose: open the `*.opt-in.md` file first — it is a short summary of the options. Then load the full `*.md` file alongside the core rules.

### Step 3: Start your project — let the AI guide you

With the rules loaded, begin your project description. The AI will ask you structured clarifying questions before generating any code or architecture. Answer them honestly — the questions determine which controls apply.

As you work through each phase (plan → design → build → test → release → deploy → monitor → improve), the AI will enforce the applicable rules and flag blocking findings before allowing you to progress.

---

## Project Setup Patterns

### Pattern A: Single-session vibe coding (small project)

For a weekend project or quick prototype, you can load everything in one context window:

1. Start a new Claude conversation.
2. Paste the full contents of `core-workflow.md` as your first message, prefixed with: "Please follow these development rules for our entire conversation:"
3. Add any extensions relevant to your project.
4. Describe your project and begin.

**Tip**: For small projects, you often only need core + `ai-agentic-security.md` (if using LLMs). Keep it lean. The core rules already include the security baseline for APIs and code generation.

### Pattern B: Multi-session project (Claude Project)

For a longer project with multiple conversations:

1. Create a Claude Project at claude.ai/projects.
2. Open Project Settings → Instructions.
3. Paste `core-workflow.md` contents into the Instructions field.
4. Upload the relevant extension `.md` files as Project Knowledge files.
5. Every new conversation in this project automatically has access to all rules.

This is the recommended approach for any project longer than one day.

### Pattern C: Team repository (Cursor / Copilot / Windsurf / CI/CD)

For a team working in a shared codebase:

1. Copy the appropriate IDE rule template from `templates/` (`.cursorrules`, `CLAUDE.md`, `.windsurfrules`, or `copilot-instructions.md`) into your repository root.
2. Commit `templates/trisuella.config.yaml` to define your project risk tier and active compliance rules.
3. Install the pre-commit hook using `templates/.pre-commit-config.yaml` to block local commits that contain open `[CRITICAL]` security findings.
4. Add the GitHub Action workflow from `templates/.github/workflows/trisuella-gate.yml` to automatically enforce policy gates on Pull Requests using `tools/trisu-cli/trisu_validator.py`.
5. Every developer on the team automatically inherits the same security baseline, and CI blocks any PR that fails compliance invariants.

### Pattern D: TRISUELLA-AIDLCAa automated multi-agent system

For teams that want a fully automated multi-agent pipeline:

1. See the `TRISUELLA-AIDLCAa/` directory for the autonomous multi-agent architecture.
2. TRISUELLA-AIDLCAa implements all the TRISUELLA-AIDLCA phases as 8 specialised agents (Planner, Designer, Builder, Tester, Releaser, Deployer, Monitor, Improver) under a Zero Trust inter-agent communication protocol (TRISU-ZTP).
3. The agents automatically consume the rule files as their operating constraints.
4. See `TRISUELLA-AIDLCAa/README.md` for complete architecture, message envelopes, and configuration instructions.

---

## Working Through Each Phase

### Phase 0 — Inception

The AI will ask you a series of structured questions about your project. Take time to answer them well — these answers determine which security controls apply.

Key questions the AI asks:
- What is the project building? (type of system)
- Who are the users? (public, internal, enterprise, consumers, potentially minors)
- What sensitive data does it handle? (triggers Sensitive Data extension)
- What compliance frameworks apply?
- What is the deployment target? (cloud, on-premise, edge)
- Does it use AI/ML or LLM components?

The AI produces a **Requirements Summary** and a **Threat Model** from your answers. Review these — they are the security foundation for the rest of the project.

### Phase 1 — Design

The AI proposes an architecture. Before accepting it, check:
- Is there a security architecture section (Zero Trust, least privilege, defence in depth)?
- Are the data flows documented? (especially sensitive data flows)
- Is there a secrets management design?
- Are external dependencies and third-party services identified?

The AI will flag if the proposed design violates any rules. If you see a blocking finding at this stage, it is much cheaper to fix than after code is written.

### Phase 2 — Build

This is where most time is spent. The AI enforces rules during code generation:
- No secrets hardcoded in code
- Input validation on all external inputs
- Parameterised queries (no SQL injection)
- No `eval()` or equivalent dynamic code execution with unsanitised input
- Appropriate error handling (no stack traces to end users)
- Logging without PII

**If the AI flags a blocking finding during Build**: do not skip it. The finding is there because the generated code violates a security rule. Fix the code, then proceed.

### Phase 3 — Test

The AI helps generate and execute a security-aware test suite:
- Unit tests for security-critical logic (authentication, authorisation, input validation)
- Dependency vulnerability scan
- Secret scan of the codebase
- SAST (static analysis)
- For AI/LLM features: prompt injection tests, output sanitisation tests

Only progress to Release when the test gate passes.

### Phase 4 — Release

The AI checks the release artifact against the release security checklist:
- SBOM generated
- Artifact signed
- No secrets in the artifact
- Changelog updated
- Security notes documented for any known limitations

### Phase 5 — Deploy

The AI validates the deployment configuration:
- Infrastructure as Code scanned
- Secrets injected at runtime (not baked into image or config)
- TLS configured
- WAF active (if applicable)
- Container security context correct (non-root, no privilege escalation)

### Phase 6 — Monitor

The AI sets up the observability configuration:
- Centralised logging (no PII in logs)
- Security alerting (authentication failures, privilege escalation, anomalous traffic)
- Health checks and uptime monitoring

### Phase 7 — Improve

The AI reviews findings from monitoring and testing and proposes improvements. This closes the loop — improvements feed back into the next Build phase.

---

## File Reference

```
TRISUELLA-AIDLCA-secure-rules/
├── TRISUELLA-AIDLCA-rules/
│   └── core-workflow.md               ← ALWAYS LOAD THIS FIRST
├── TRISUELLA-AIDLCA-rule-details/
│   ├── common/
│   │   ├── process-overview.md        ← Visual phase summary (Inception/Construction/Operations)
│   │   ├── session-continuity.md      ← How the AI tracks progress across sessions
│   │   ├── terminology.md             ← Glossary of TRISUELLA-AIDLCA terms
│   │   └── ...                        ← Other common behaviour rules
│   ├── inception/                     ← Phase-specific rules: requirements, threat model
│   ├── construction/                  ← Phase-specific rules: design, build, test, release
│   ├── operations/                    ← Phase-specific rules: deploy, monitor, improve
│   └── extensions/
│       ├── security/
│       │   ├── baseline/
│       │   │   └── security-baseline.md         ← Core security rules (always active)
│       │   ├── ai-agentic/
│       │   │   ├── ai-agentic-security.md        ← AI/LLM/agent security (8 rules)
│       │   │   └── ai-agentic-security.opt-in.md
│       │   ├── cloud-security/
│       │   │   ├── cloud-security.md             ← AWS/Azure/GCP controls (10 rules)
│       │   │   └── cloud-security.opt-in.md
│       │   ├── infra-security/
│       │   │   ├── infra-security.md             ← Infra, K8s, Docker, supply chain (15 rules)
│       │   │   └── infra-security.opt-in.md
│       │   ├── privacy-secure-design/
│       │   │   ├── privacy-secure-design.md      ← Privacy by design (10 rules)
│       │   │   └── privacy-secure-design.opt-in.md
│       │   ├── sensitive-data/
│       │   │   ├── sensitive-data-security.md    ← PII, health, financial, AI data (8 rules)
│       │   │   └── sensitive-data-security.opt-in.md
│       │   └── zero-trust/
│       │       ├── zero-trust.md                 ← Zero Trust architecture (9 rules)
│       │       └── zero-trust.opt-in.md
│       ├── compliance/
│       │   ├── compliance-mapping.md             ← GDPR, HIPAA, PCI-DSS, DPDPA, SOC 2, ISO 27001
│       │   └── compliance-mapping.opt-in.md
│       └── testing/
│           └── property-based/
│               └── property-based-testing.md     ← Property-based testing (10 rules)
├── prompts/
│   ├── README.md                      ← Index of all prompt templates
│   ├── planning/                      ← P-01–P-05: requirements, threat model, architecture
│   ├── build/                         ← B-01–B-06: secure code generation, review, auth
│   ├── test/                          ← T-01–T-06: security testing, prompt injection, infra
│   ├── ai-agents/                     ← A-01–A-06: LLM features, multi-agent, RAG, MCP
│   └── compliance/                    ← C-01–C-05: GDPR, DPDPA, HIPAA, PCI-DSS, DSR workflow
└── docs/
    ├── how-to-use.md                  ← This file
    ├── which-extensions.md            ← 8 questions to pick the right extensions
    ├── faq.md                         ← Common questions and answers
    ├── benefits.md                    ← Why use this framework
    ├── vibe-coding-guide.md           ← Guide for AI-assisted / vibe coding workflows
    └── adr-template.md                ← Architecture Decision Record template
```

---

## Using the Prompt Template Library

The `prompts/` directory contains 28 copy-paste ready prompts across 5 categories. These are designed to work with any AI tool that has the framework loaded — just paste the prompt template, fill in your project-specific details in the `[bracketed fields]`, and send.

**Planning prompts** (`prompts/planning/`): Use P-01 at the start of a new project, P-03 to generate a STRIDE threat model, P-04 to add security acceptance criteria to user stories.

**Build prompts** (`prompts/build/`): Use B-01 when generating a new API endpoint, B-02 to run a security review of existing code, B-03 to generate a secure Dockerfile, B-06 for a complete authentication implementation.

**Test prompts** (`prompts/test/`): Use T-01 to generate a security test suite for an API, T-02 to generate prompt injection tests for an AI feature, T-04 to set up secret scanning in CI/CD.

**AI agent prompts** (`prompts/ai-agents/`): Use A-01 when adding any LLM feature, A-02 for multi-agent system design, A-03 for RAG security design, A-06 to security-review an MCP server.

**Compliance prompts** (`prompts/compliance/`): Use C-01 for a GDPR checklist on a new feature, C-02 for DPDPA compliance if you have Indian users, C-05 to design a data subject rights response workflow.

**Tip**: Start with the planning prompts before writing any code. A well-structured threat model at the beginning prevents far more security issues than code review at the end.

---

## Tips for Getting the Most Out of the Framework

**Be specific in your project description.** The more context you give the AI about what you are building, who uses it, and what data it handles, the more precisely it can apply the right rules. Vague descriptions lead to vague security guidance.

**Do not skip blocking findings.** The AI labels some issues as blocking findings — it will not progress the phase until they are resolved. These are not suggestions; they are the rules that prevent the most common and most severe security failures. If a blocking finding seems wrong for your context, discuss it with the AI and document your reasoning.

**Use the extension opt-in files first.** Before loading a full extension, read its `.opt-in.md` file. It is short and tells you exactly what you get. This helps you decide whether the extension is relevant and which options within it apply to your project.

**Commit your rule configuration.** If you are using Cursor, Copilot, or a similar editor-integrated AI, commit the rule files to your repository. This ensures every team member and every new conversation starts with the same baseline.

**Review the generated artifacts.** The framework produces several documents alongside code: threat model, architecture design, hardening baseline, test results. These artifacts are valuable — they document the security thinking behind the system and are useful for compliance audits, security reviews, and onboarding new team members.

**Use the prompt library.** The `prompts/` directory contains 28 ready-to-use prompts for every phase of development. Instead of writing a prompt from scratch to ask for a security code review or a GDPR compliance check, use the templates — they are structured to get consistent, thorough results.

**Document your architecture decisions.** For any significant design choice, use `docs/adr-template.md` to write an ADR. The template includes sections for security impact, compliance impact, and AI agent interaction impact — fields that are unique to the TRISUELLA-AIDLCA SDF and capture the reasoning that standard ADR templates miss.
