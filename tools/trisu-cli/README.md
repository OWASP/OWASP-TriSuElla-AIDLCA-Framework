# OWASP TriSuElla-AIDLCA Policy Gate Validator CLI (`trisu`)

The official zero-dependency command-line utility for the **OWASP TriSuElla-AIDLCA Framework (v3.0)**. Enforces deterministic Zero Trust Code (ZTC) invariants, Open Source Security (OSS) supply chain checks, CycloneDX AI-BoM generation, and automated CI/CD gating.

## ⚡ Quick Installation

### Option 1: Direct Execution (Zero Install)
From the repository root:
```bash
# Windows
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
Now `trisu` is available globally in your PATH:
```bash
trisu --help
trisu check
trisu audit --sarif audit.sarif
trisu oss --sarif oss.sarif
trisu bom --output ai-bom.json
trisu rules
trisu init --target ./my-app
```

## 🛠 Commands Overview

| Command | Description |
|---|---|
| `trisu check` | Verifies repository readiness, core artifacts, and drop-in templates |
| `trisu audit` | Scans workspace for hardcoded secrets, dangerous sinks (`eval`, `exec`, `shell=True`), and ZTC violations |
| `trisu oss` | Audits open source dependencies, pinned lockfiles, license contamination, and supply chain integrity |
| `trisu bom` | Generates CycloneDX AI v1.6 Bill of Materials (`ai-bom.json`) for models, datasets, and agents |
| `trisu rules` | Validates master rules index and displays breakdown across all 25 domains and 198 rules |
| `trisu init` | Scaffolds TriSuElla governance templates (`.cursorrules`, `CLAUDE.md`, config, CI workflow) into a project |
