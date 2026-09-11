<!-- Drop this file into .github/copilot-instructions.md -->
# GitHub Copilot Instructions — TRISUELLA-AIDLCA v3.0

When assisting with code generation, review, or architecture in this repository:
1. Always implement security by default adhering to the OWASP Top 10 and OWASP Top 10 for LLM Applications.
2. Validate and sanitize all inputs at system and function boundaries. Never trust client or model input.
3. Apply the 3-Layer Risk Model: prioritize Layer 1 Residual Risk (Cloud IAM, secret management, container hardening) over cosmetic controls.
4. For AI/LLM features:
   - Ensure vector store queries isolate user tenancy and redact PII.
   - Enforce semantic validation and JSON-schema constraints on all model outputs.
   - Sandbox all agent tool-use with minimal execution privilege.
5. If you identify any [CRITICAL] or [HIGH] vulnerability, immediately flag it and propose a secure refactoring.
