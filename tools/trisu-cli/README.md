# 🔱 OWASP TriSuElla-AIDLCA Policy Gate Validator CLI (`trisu`)
> **Software Version**: 3.0.1 | **Framework Version**: 3.0.1 | **Status**: Production-Ready (Verified CI/CD Gate)  
> **Consolidated Invariants**: 299 Checks | **Rules**: 198 | **Domain Families**: 25  
> **Author**: [Bhaskar Puppala (PATEL)](https://www.linkedin.com/in/bhaskerkpatel/)

The official zero-dependency command-line utility for the **OWASP TriSuElla-AIDLCA Framework (v3.0.1)**. Enforces deterministic Zero Trust Code (ZTC) invariants, Open Source Security (OSS) supply chain checks, CycloneDX AI-BoM generation, and automated CI/CD gating across any platform (GitHub, GitLab, Azure DevOps, Bitbucket, Jenkins, or Local).

---

## 📈 Progress & Implementation Milestones (v3.0.1)

| Capability / Engine | Scope & Standards | Progress | Status |
| :--- | :--- | :---: | :---: |
| **AST Security Audit Engine (`trisu audit`)** | Secret scanning, dangerous sinks (`eval`, `exec`, `shell=True`), ZTC checks | 100% | **Production-Ready** |
| **Supply Chain & OSS Engine (`trisu oss`)** | Lockfile hash pinning, copyleft license checks, typosquatting defense | 100% | **Production-Ready** |
| **CycloneDX AI-BoM Generator (`trisu bom`)** | Automated CycloneDX AI v1.6 Bill of Materials generation | 100% | **Production-Ready** |
| **Repository Readiness Validator (`trisu check`)**| Validates 10 core framework artifacts & 7 developer templates | 100% | **Production-Ready** |
| **Master Rule Indexer (`trisu rules`)** | Validates 198 rule identifiers across 25 domain families | 100% | **Production-Ready** |
| **Project Scaffolder (`trisu init`)** | Instant scaffolding of `.cursorrules`, `CLAUDE.md`, config, and CI gates | 100% | **Production-Ready** |
| **Multi-Platform Turnkey Launchers** | `trisu.cmd` (Windows), `trisu` (POSIX executable), pip package | 100% | **Production-Ready** |
| **Universal OASIS SARIF 2.1.0 Export** | Standard SARIF output for GitHub, GitLab, Azure DevOps, and SonarQube | 100% | **Production-Ready** |
| **GitHub Actions CI/CD Policy Gate** | Live verified run `34675720411` with dual SARIF uploads & artifacts | 100% | **Verified Passing** |

---

## ⚡ Quick Installation & Execution

### Option 1: Direct Execution (Zero Dependencies / Zero Install)
From the repository root:
```bash
# Windows (cmd / powershell)
.\trisu.cmd check
.\trisu.cmd audit
.\trisu.cmd oss
.\trisu.cmd rules

# Linux / macOS / Git Bash
./trisu check
./trisu audit
./trisu oss
./trisu rules
```

### Option 2: Pip Editable Install (Global Command)
```bash
pip install -e tools/trisu-cli
```
Now `trisu` is available globally in your system PATH:
```bash
trisu --help
trisu check
trisu audit --sarif audit.sarif
trisu oss --sarif oss.sarif
trisu bom --output ai-bom.json
trisu rules
trisu init --target ./my-app
```

---

## 🛠 Commands Matrix

| Command | Description | Exit Code Behavior |
|---|---|---|
| `trisu check` | Verifies repository readiness, core artifacts, and drop-in templates | Exits `0` if all artifacts exist; `1` if missing |
| `trisu audit` | Scans workspace for hardcoded secrets, dangerous sinks (`eval`, `exec`, `shell=True`), and ZTC violations | Exits `1` if `[CRITICAL]` or `[HIGH]` findings exist; `0` if clean |
| `trisu oss` | Audits open source dependencies, pinned lockfiles, license contamination, and supply chain integrity | Exits `1` on unpinned dependencies or GPL in proprietary projects |
| `trisu bom` | Generates CycloneDX AI v1.6 Bill of Materials (`ai-bom.json`) for models, datasets, and agents | Exits `0` on successful generation |
| `trisu rules` | Validates master rules index and displays breakdown across all 25 domains and 198 rules | Exits `0` on valid index |
| `trisu init` | Scaffolds TriSuElla governance templates (`.cursorrules`, `CLAUDE.md`, config, CI workflow) into a project | Exits `0` on successful scaffolding |

---

## 🌐 Universal CI/CD Integration (Not Just GitHub)

The `trisu` validator generates open, vendor-neutral outputs (**OASIS SARIF 2.1.0** and **CycloneDX AI v1.6**). It integrates into any CI/CD platform:

### 1. GitLab CI (`.gitlab-ci.yml`)
```yaml
trisuella-gate:
  stage: test
  image: python:3.11-slim
  script:
    - python tools/trisu-cli/trisu_validator.py audit --sarif trisuella-audit.sarif
    - python tools/trisu-cli/trisu_validator.py oss --sarif trisuella-oss.sarif
  artifacts:
    reports:
      sast: trisuella-audit.sarif
    paths:
      - trisuella-audit.sarif
      - trisuella-oss.sarif
```

### 2. Azure DevOps (`azure-pipelines.yml`)
```yaml
steps:
- script: |
    python tools/trisu-cli/trisu_validator.py audit --sarif $(Build.ArtifactStagingDirectory)/audit.sarif
    python tools/trisu-cli/trisu_validator.py oss --sarif $(Build.ArtifactStagingDirectory)/oss.sarif
  displayName: 'Run TriSuElla Policy Gate'
- task: PublishSecurityAnalysisLogs@3
  inputs:
    ArtifactName: 'CodeAnalysisLogs'
    ArtifactType: 'Container'
```

### 3. Bitbucket Pipelines / Jenkins / Local Shell
```bash
# Runs deterministically anywhere Python 3 is installed
python tools/trisu-cli/trisu_validator.py audit
python tools/trisu-cli/trisu_validator.py oss
```
If a `[CRITICAL]` or `[HIGH]` violation is found, `trisu` automatically exits with code `1`, halting the build or deployment pipeline immediately regardless of the CI platform.

