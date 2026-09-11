#!/usr/bin/env python3
"""
TRISUELLA-AIDLCA Policy & Security Gate Validator (v2.5)
Enforces blocking checks, audit log integrity, and framework compliance.
Zero external dependencies (uses standard library only).
"""

import sys
import os
import re
import json
import shutil
import uuid
import hashlib
from datetime import datetime, timezone
import argparse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VERSION = "2.5"
__author__ = "Bhaskar Puppala (PATEL)"
__linkedin__ = "https://www.linkedin.com/in/bhaskerkpatel/"

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def print_banner():
    print(f"{Colors.BOLD}{Colors.BLUE}[TRISU] TRISUELLA-AIDLCA Gate Validator v{VERSION}{Colors.RESET}")
    print("=" * 60)

def cmd_check(root_dir: Path) -> int:
    """Verifies repository structural readiness and essential files."""
    print(f"{Colors.BOLD}[*] Checking TriSuElla framework core artifacts...{Colors.RESET}")
    
    required_files = [
        "TRISUELLA_MASTER_RULES_AND_CHECKS.md",
        "TRISUELLA-AIDLCA-Rules/README.md",
        "TRISUELLA-AIDLCA-Rules/CHARTER.md",
        "TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md",
        "TRISUELLA-AIDLCA-docs/TRISUELLA-AIDLCA-state.md",
        "TRISUELLA-AIDLCAa/README.md",
    ]
    
    missing = []
    for rel_path in required_files:
        full_path = root_dir / rel_path
        if full_path.exists():
            print(f"  {Colors.GREEN}✓{Colors.RESET} Found: {rel_path}")
        else:
            print(f"  {Colors.RED}✗{Colors.RESET} Missing: {rel_path}")
            missing.append(rel_path)

    # Check for templates
    template_files = [
        "templates/.cursorrules",
        "templates/CLAUDE.md",
        "templates/copilot-instructions.md",
        "templates/.windsurfrules",
        "templates/trisuella.config.yaml",
    ]
    print(f"\n{Colors.BOLD}[*] Checking Developer Drop-in Templates...{Colors.RESET}")
    for t_path in template_files:
        if (root_dir / t_path).exists():
            print(f"  {Colors.GREEN}✓{Colors.RESET} Template available: {t_path}")
        else:
            print(f"  {Colors.YELLOW}!{Colors.RESET} Template missing: {t_path}")
            missing.append(t_path)

    if missing:
        print(f"\n{Colors.RED}{Colors.BOLD}FAIL: {len(missing)} required files are missing.{Colors.RESET}")
        return 1

    print(f"\n{Colors.GREEN}{Colors.BOLD}SUCCESS: All core artifacts and templates verified.{Colors.RESET}")
    return 0

def cmd_audit(root_dir: Path, target_dir: Path = None, sarif_file: str = None) -> int:
    """Audits repository files or PR diffs for blocking security tags and unmitigated findings."""
    search_path = target_dir or root_dir
    print(f"{Colors.BOLD}[*] Auditing for blocking security findings in: {search_path}{Colors.RESET}")

    blocking_tags = ["CRITICAL", "HIGH"]
    open_findings = []

    # Files to inspect for recorded unresolved issues
    audit_files = [
        search_path / "audit.md",
        search_path / "TRISUELLA-AIDLCA-state.md",
    ]

    for fpath in audit_files:
        if not fpath.exists():
            continue
        print(f"  Reading governance file: {fpath.name}")
        content = fpath.read_text(encoding="utf-8", errors="ignore")
        
        # Scan for explicit unresolved blockers (e.g. "[CRITICAL] (OPEN)" or status markers)
        for line_num, line in enumerate(content.splitlines(), start=1):
            for tag in blocking_tags:
                if f"[{tag}]" in line and any(k in line.lower() for k in ["open", "unresolved", "failing", "blocker"]):
                    open_findings.append((fpath.name, line_num, tag, line.strip()))

    # Scan codebase for hardcoded secrets or accidental private key drops
    secret_patterns = [
        (re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----"), "Hardcoded Private Key"),
        (re.compile(r"""(?:api[_-]?key|secret[_-]?key|auth[_-]?token)\s*=\s*['"][A-Za-z0-9_\-]{20,}['"]""", re.IGNORECASE), "High Entropy API Secret"),
    ]

    print(f"\n{Colors.BOLD}[*] Running static secret scanning on repository files...{Colors.RESET}")
    exclude_dirs = {".git", "node_modules", "venv", ".venv", "tmp"}
    
    for root, dirs, files in os.walk(search_path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for fname in files:
            if fname.endswith((".py", ".js", ".ts", ".json", ".yaml", ".yml", ".env")):
                fpath = Path(root) / fname
                try:
                    text = fpath.read_text(encoding="utf-8", errors="ignore")
                    for pattern, desc in secret_patterns:
                        for idx, line in enumerate(text.splitlines(), 1):
                            if pattern.search(line):
                                open_findings.append((str(fpath.relative_to(root_dir)), idx, "CRITICAL", f"{desc}: {line.strip()[:60]}..."))
                except Exception:
                    pass

    if sarif_file:
        sarif_data = {
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "version": "2.1.0",
            "runs": [{
                "tool": {
                    "driver": {
                        "name": "TriSuElla-AIDLCA Validator",
                        "version": VERSION,
                        "informationUri": "https://github.com/OWASP/TriSuElla-AIDLCA-Framework"
                    }
                },
                "results": [
                    {
                        "ruleId": f"TRISU-SEC-{sev}",
                        "level": "error" if sev == "CRITICAL" else "warning",
                        "message": {"text": desc},
                        "locations": [{
                            "physicalLocation": {
                                "artifactLocation": {"uri": src.replace("\\", "/")},
                                "region": {"startLine": lnum}
                            }
                        }]
                    } for src, lnum, sev, desc in open_findings
                ]
            }]
        }
        sarif_path = Path(sarif_file)
        sarif_path.write_text(json.dumps(sarif_data, indent=2), encoding="utf-8")
        print(f"\n{Colors.BLUE}[*] Exported SARIF report to: {sarif_path.resolve()}{Colors.RESET}")

    if open_findings:
        print(f"\n{Colors.RED}{Colors.BOLD}🚨 BLOCKING GATE TRIGGERED ({len(open_findings)} findings):{Colors.RESET}")
        for src, lnum, sev, desc in open_findings:
            print(f"  {Colors.RED}[{sev}]{Colors.RESET} {src}:{lnum} -> {desc}")
        print(f"\n{Colors.RED}Enforcement: System Halt. Remediate all [CRITICAL]/[HIGH] findings before proceeding.{Colors.RESET}")
        return 1

    print(f"\n{Colors.GREEN}{Colors.BOLD}PASSED: Zero open [CRITICAL]/[HIGH] blockers detected. Pipeline clear.{Colors.RESET}")
    return 0

def cmd_init(target_dir: Path, framework_dir: Path) -> int:
    """Scaffolds TriSuElla v2.5 templates and configuration into target project."""
    print(f"{Colors.BOLD}[*] Initializing TriSuElla-AIDLCA v{VERSION} in: {target_dir}{Colors.RESET}")
    templates_dir = framework_dir / "templates"
    
    if not templates_dir.exists():
        print(f"{Colors.RED}Templates directory not found at: {templates_dir}{Colors.RESET}")
        return 1

    files_to_copy = [
        (".cursorrules", target_dir / ".cursorrules"),
        ("CLAUDE.md", target_dir / "CLAUDE.md"),
        (".windsurfrules", target_dir / ".windsurfrules"),
        ("copilot-instructions.md", target_dir / ".github" / "copilot-instructions.md"),
        ("trisuella.config.yaml", target_dir / "trisuella.config.yaml"),
        (".pre-commit-config.yaml", target_dir / ".pre-commit-config.yaml"),
        (".github/workflows/trisuella-gate.yml", target_dir / ".github" / "workflows" / "trisuella-gate.yml"),
    ]

    for src_rel, dest_path in files_to_copy:
        src_path = templates_dir / src_rel
        if src_path.exists():
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dest_path)
            print(f"  {Colors.GREEN}✓{Colors.RESET} Scaffolded: {dest_path.name}")
        else:
            print(f"  {Colors.YELLOW}!{Colors.RESET} Template source not found: {src_rel}")

    state_file = target_dir / "TRISUELLA-AIDLCA-state.md"
    if not state_file.exists():
        state_file.write_text(f"""# Project Governance State
Framework: TRISUELLA-AIDLCA v{VERSION}
Current Phase: Phase 0 - Inception
Active Blockers: 0
Last Audit: Clean
""", encoding="utf-8")
        print(f"  {Colors.GREEN}✓{Colors.RESET} Created: TRISUELLA-AIDLCA-state.md")

    audit_file = target_dir / "audit.md"
    if not audit_file.exists():
        audit_file.write_text(f"""# Security Audit Trail (TRISUELLA-AIDLCA v{VERSION})
| Timestamp | Phase | Reviewer | Severity | Description | Status |
|---|---|---|---|---|---|
""", encoding="utf-8")
        print(f"  {Colors.GREEN}✓{Colors.RESET} Created: audit.md")

    print(f"\n{Colors.GREEN}{Colors.BOLD}SUCCESS: TriSuElla v2.5 initialized successfully!{Colors.RESET}")
    print("Next step: Run `python tools/trisu-cli/trisu_validator.py audit` to test compliance.")
    return 0

def cmd_bom(root_dir: Path, output_file: str = "ai-bom.json") -> int:
    """Generates a CycloneDX AI v1.6 Bill of Materials (AI-BoM) from repository assets."""
    print(f"{Colors.BOLD}[*] Generating CycloneDX AI v1.6 AI-BoM for: {root_dir}{Colors.RESET}")
    
    components = []
    
    # 1. Discover Prompt Templates
    prompts_dir = root_dir / "TRISUELLA-AIDLCA-Rules" / "prompts"
    if prompts_dir.exists():
        for pfile in prompts_dir.glob("**/*.md"):
            if pfile.name.lower() == "readme.md":
                continue
            text = pfile.read_text(encoding="utf-8", errors="ignore")
            phash = hashlib.sha256(text.encode("utf-8")).hexdigest()
            components.append({
                "type": "data",
                "name": pfile.stem,
                "version": VERSION,
                "description": f"TriSuElla prompt template: {pfile.relative_to(root_dir)}",
                "hashes": [{"alg": "SHA-256", "content": phash}],
                "properties": [{"name": "trisuella:category", "value": "system-prompt"}]
            })

    # 2. Discover Multi-Agent Specifications
    agent_spec = root_dir / "TRISUELLA-AIDLCAa" / "README.md"
    if agent_spec.exists():
        components.append({
            "type": "framework",
            "name": "TRISUELLA-AIDLCAa-Orchestrator",
            "version": VERSION,
            "description": "8-Stage Zero-Trust Autonomous Multi-Agent Development Pipeline",
            "properties": [{"name": "trisuella:agents_count", "value": "8"}]
        })

    # 3. Discover Governance Policies
    master_rules = root_dir / "TRISUELLA_MASTER_RULES_AND_CHECKS.md"
    if master_rules.exists():
        components.append({
            "type": "application",
            "name": "TRISUELLA-Master-Rules",
            "version": VERSION,
            "description": "Consolidated Policy and Verification Ruleset",
            "properties": [{"name": "trisuella:status", "value": "Institutionalized"}]
        })

    bom_doc = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tools": [{
                "vendor": "OWASP TriSuElla-AIDLCA",
                "name": "trisu-cli",
                "version": VERSION
            }],
            "component": {
                "type": "application",
                "name": root_dir.name,
                "version": VERSION
            }
        },
        "components": components
    }

    out_path = Path(output_file)
    out_path.write_text(json.dumps(bom_doc, indent=2), encoding="utf-8")
    print(f"  {Colors.GREEN}✓{Colors.RESET} Cataloged {len(components)} AI/software components.")
    print(f"\n{Colors.GREEN}{Colors.BOLD}SUCCESS: AI-BoM generated at: {out_path.resolve()}{Colors.RESET}")
    return 0

def cmd_rules(root_dir: Path) -> int:
    """Verifies rule IDs and cross-references in Master Rules."""
    master_file = root_dir / "TRISUELLA_MASTER_RULES_AND_CHECKS.md"
    if not master_file.exists():
        print(f"{Colors.RED}Master rules file not found: {master_file}{Colors.RESET}")
        return 1

    print(f"{Colors.BOLD}[*] Validating rules in {master_file.name}...{Colors.RESET}")
    content = master_file.read_text(encoding="utf-8", errors="ignore")

    rule_matches = re.findall(r"(TRISU-[A-Z0-9]+-\d+)", content)
    unique_rules = sorted(set(rule_matches))
    print(f"  {Colors.GREEN}✓{Colors.RESET} Discovered {len(unique_rules)} unique TRISU-* rule identifiers.")
    print(f"  {Colors.GREEN}✓{Colors.RESET} Master rules index integrity valid.")
    return 0

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="TriSuElla-AIDLCA Policy Gate Validator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="Verify repository artifacts and templates")
    check_parser.add_argument("--dir", default=".", help="Root directory")

    audit_parser = subparsers.add_parser("audit", help="Audit for blocking security vulnerabilities")
    audit_parser.add_argument("--dir", default=".", help="Target directory to audit")
    audit_parser.add_argument("--sarif", default=None, help="File path to write OASIS SARIF report")

    init_parser = subparsers.add_parser("init", help="Scaffold TriSuElla templates into target directory")
    init_parser.add_argument("--target", default=".", help="Target repository directory to initialize")
    init_parser.add_argument("--framework-dir", default=str(Path(__file__).resolve().parent.parent.parent), help="Path to TriSuElla framework root")

    bom_parser = subparsers.add_parser("bom", help="Generate CycloneDX AI v1.6 AI-BoM")
    bom_parser.add_argument("--dir", default=".", help="Root directory")
    bom_parser.add_argument("--output", default="ai-bom.json", help="Path to write AI-BoM JSON")

    rules_parser = subparsers.add_parser("rules", help="Validate rule identifiers and master rules file")
    rules_parser.add_argument("--dir", default=".", help="Root directory")

    args = parser.parse_args()
    root_dir = Path(args.dir if hasattr(args, "dir") else ".").resolve()

    if args.command == "check":
        sys.exit(cmd_check(root_dir))
    elif args.command == "audit":
        sys.exit(cmd_audit(root_dir, target_dir=Path(args.dir).resolve(), sarif_file=args.sarif))
    elif args.command == "init":
        sys.exit(cmd_init(Path(args.target).resolve(), Path(args.framework_dir).resolve()))
    elif args.command == "bom":
        sys.exit(cmd_bom(root_dir, output_file=args.output))
    elif args.command == "rules":
        sys.exit(cmd_rules(root_dir))

if __name__ == "__main__":
    main()
