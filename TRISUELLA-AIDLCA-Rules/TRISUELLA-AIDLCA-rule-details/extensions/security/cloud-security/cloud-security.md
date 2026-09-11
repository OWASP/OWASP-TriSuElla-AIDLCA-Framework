# TRISU-CLOUD: Cloud-Native Resource & Managed Service Security Rules

## Overview

These rules define the **TRISU-CLOUD Platform Standard**. They are **MANDATORY blocking constraints** for any system hosted on cloud infrastructure. Designed to be platform-agnostic, these rules apply regardless of the specific provider (AWS, Azure, GCP), managed service, or orchestration layer used.

TRISU-CLOUD establishes a trust-centric (**TILLIT**) operational layer where cloud-native resources are hardened, monitored, and governed with zero-trust principles.

---

## 🚦 TRISU Cloud Enforcement
- **Scope**: Applied to IAM, object storage, cloud-native networking, serverless functions, and managed database services.
- **Verification Requirement**: Every TRISU-CLOUD rule must be verified as "Compliant" before a stage or phase can be closed.
- **Blocking Logic**: Any [CRITICAL] or [HIGH] violation triggers a **Mandatory Halt**.

---

## Rule TRISU-CLOUD-01 [CRITICAL]: Identity & Access Management (IAM) Invariants

**Rule**: Every cloud identity (user, service, role, or workload) MUST adhere to uncompromising least-privilege principles.

**Required Controls**:
- **Zero Wildcarding**: Use of `*` or equivalent catch-all actions/resources is PROHIBITED in production policies. Permissions MUST be scoped to specific API actions and resource identifiers (ARNs/IDs).
- **Decoupled Service Identities**: Every service, function, or container group MUST have its own unique identity. Shared credentials across services are PROHIBITED.
- **Ephemeral Machine Credentials**: Automated workloads (CI/CD, services) MUST use short-lived, role-assumed credentials (e.g., OIDC, IAM Roles) instead of static, long-lived access keys.
- **Federated Human Access**: All human administrative access MUST be mediated through federated identity (SSO) with mandatory Multi-Factor Authentication.

**Verification**:
- IAM policies confirm zero unauthorized wildcarding.
- Audit shows zero static access keys in use for automated services.
- Federation is confirmed as the sole path for human administrative login.

---

## Rule TRISU-CLOUD-02 [CRITICAL]: Cloud Storage Isolation & Protection

**Rule**: All cloud storage resources (Buckets, Blobs, Volumes) MUST be private by default and encrypted at the platform layer.

**Required Controls**:
- **Mandatory Public Access Block**: High-level platform settings MUST explicitly block public access for all storage resources unless a specific, documented exception exists for public assets (e.g., CDN origins).
- **Zero-Trust Write Access**: Unauthenticated or anonymous write access is strictly PROHIBITED.
- **Encryption at Rest**: All storage MUST utilize server-side encryption (managed or customer-provided keys).
- **Versioned Continuity**: Enable versioning for critical or irreplaceable data stores to defend against accidental deletion or ransomware.
- **Audit-First Visibility**: Storage-level access logs MUST be enabled and shipping to a centralized, restricted zone.

**Verification**:
- Platform-level public access block is verified active.
- Storage policies confirm zero anonymous access.
- Encryption configurations are present on all storage definitions.

---

## Rule TRISU-CLOUD-03 [CRITICAL]: Virtual Network Topology & Perimeter Hardening

**Rule**: Cloud network configurations MUST follow "Deny-by-Default" logic and minimize public exposure surface.

**Required Controls**:
- **Isolated Workload Subnets**: Compute instances, databases, and cognitive agents MUST run in private subnets with zero direct route to an internet gateway.
- **Private Endpoint Prioritization**: Use private platform endpoints (e.g., VPC Endpoints) to access other cloud-managed services, avoiding the public internet for internal traffic.
- **Zero Public Management Ingress**: Administrative ports (SSH/RDP) MUST NOT be open to the public internet (`0.0.0.0/0`). Access MUST be mediated via VPN or secure session managers.
- **Segregated Data Tiers**: Database and storage services MUST NOT have public IP addresses or internet-facing endpoints.
- **Autonomous Flow Logging**: Network flow logs MUST be active in all production environments to capture forensic metadata.

**Verification**:
- Routing tables confirm private subnet isolation for all workloads.
- Firewall/Group rules show zero public exposure for administrative or database ports.
- Flow logging configuration is active and shipping to the observability zone.

---

## Rule TRISU-CLOUD-04 [HIGH]: Managed Compute & Registry Security

**Rule**: All managed compute resources (VMs, Containers, Serverless) MUST be built from verified artifacts and hardened at the platform layer.

**Required Controls**:
- **Hardened Base Invariant**: Use only official, hardened vendor images or internal, continuously scanned mother-images.
- **Metadata Protection**: Disable legacy, unauthenticated metadata services (e.g., IMDSv1) to prevent SSRF-based credential theft.
- **Immutable Container Runtime**: Set container filesystems to read-only and prohibit privileged mode in production environments.
- **Non-Root Execution**: Every containerized or serverless workload MUST execute as a non-privileged, non-root user.
- **Scoped Execution Roles**: Each serverless function or compute unit MUST have a dedicated execution role scoped to its specific operational requirement.

**Verification**:
- Runtime manifests confirm `runAsNonRoot: true` and `privileged: false`.
- Metadata service is verified in "Secure/Restricted" mode.
- Compute role policies are scoped to the minimum required resource set.

---

## Rule TRISU-CLOUD-05 [CRITICAL]: Federated Secrets & Key Management

**Rule**: All cloud-native secrets and cryptographic keys MUST be managed through a centralized, audited vault service.

**Required Controls**:
- **No Plaintext Secrets**: Hardcoded credentials in IaC, code, or metadata user-data are PROHIBITED.
- **Centralized Vaulting**: Retrieve all sensitive configuration from a managed vault (Secrets Manager/Key Vault) at the point of runtime.
- **Active Secret Scoped Keys**: Use unique CMKs (Customer Managed Keys) for high-sensitivity data encryption, ensuring absolute control over the key lifecycle.
- **Mandatory Logic Rotation**: Enable automated rotation for all managed database and service credentials.

**Verification**:
- Secret-scanning gate shows zero finding matches in the repository.
- Infrastructure definition points to a managed secret/key reference.

---

## Rule TRISU-COMP-08 [HIGH]: Platform Observability & Log Integrity

**Rule**: All cloud platform (Control-Plane) and service (Data-Plane) activity MUST be logged, retained, and protected from local tampering.

**Required Controls**:
- **Universal Audit Trail**: Enable cloud-native audit logging across all active regions and accounts.
- **Log Segment Isolation**: Store audit logs in a dedicated, restricted account/subscription—different from where the and actions originate.
- **Integrity Validation**: Enable log file integrity verification to detect unauthorized modification or deletion of the audit trail.
- **High-Severity Alerting**: Configure immediate alerts for:
  - Disabling or modifying audit logging.
  - Root or global administrator activity.
  - Changes to platform-level security policies.
  - Unauthorized encryption key deletion attempts.

**Verification**:
- Audit trail is active in all regions.
- Log storage destination confirmed as out-of-band and restricted.

---

## Rule TRISU-CLOUD-10 [HIGH]: Cloud Account Hygiene & Boundary Governance

**Rule**: Cloud environments MUST be organized into isolated accounts/tenants to minimize blast radius and ensure regulatory compliance.

**Required Controls**:
- **Hard Account Separation**: Maintain strictly separate cloud accounts/subscriptions for Production, Staging, and Development. Commingling is PROHIBITED.
- **Guardrail Policy Enforcement**: Implement platform-level inheritance policies (e.g., SCPs) that prevent accounts from disabling logging, removing MFA, or creating public storage.
- **Continuous Posture Scanning**: Deploy continuous cloud security posture management (CSPM) to monitor compliance against TRISU-CLOUD rules.
- **Anomaly Detection & Budget Alerting**: Configure high-fidelity billing and activity anomaly alerts to detect resource hijacking or logic runaway.

**Verification**:
- Environment accounts are confirmed distinct and isolated.
- CSPM reports show zero high-severity logic violations.
