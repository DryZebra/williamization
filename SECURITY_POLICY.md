# Enterprise Data Governance & Security Policy

## 1. Core Principles (Privacy by Design & Default Deny)

This project strictly enforces **NIST SP 800-122**, **GDPR Article 25 (Data Protection by Design)**, and **ISO/IEC 27001** standards for version control, API services, and data management.

1. **Zero PII in Public Repositories**: Personally Identifiable Information (PII) including email addresses, real names, phone numbers, and payment identifiers must NEVER be committed to Git.
2. **Default-Deny Staging**: Only files explicitly listed in the **Product Whitelist Manifest** are permitted in version control. All unlisted files are blocked by default.
3. **Environment-Driven Configuration**: Operational credentials and payment destination emails are read dynamically from runtime environment variables (`PAYPAL_BUSINESS_EMAIL`, `GIT_AUTHOR_EMAIL`). Fallbacks must use generic anonymous identifiers (`developer@users.noreply.github.com`).
4. **Anonymous Exclusion Wildcards**: `.gitignore` must use generic wildcards (`*.json`, `*.md`, `*.env`) rather than naming specific local workspace files.
5. **Separation of Concerns**: Internal orchestration configs, deployment tools, manuscript readers, and dev scratch utilities reside in local, git-ignored environments (`scratch/`).

---

## 2. Product Whitelist Manifest

The public GitHub repository is strictly restricted to the following product components:

- `README.md` & `LICENSE` (Public Open-Source Documentation)
- `pyproject.toml` & `requirements.txt` (Package Dependency Specs)
- `vercel.json` & `config.yaml` (Deployment Configuration)
- `.gitignore` (Anonymous Wildcard Rules)
- `api/` & `src/api/` (FastAPI Serverless Application)
- `src/williamization/` (Williamization Core Engine & Decorator)
- `src/sekg/` (Semantic Knowledge Graph Engine & Parser)
- `src/utils/` & `src/agents/` (Core Utility Modules)
- `tests/` (Automated Unit Test Suite)
- `okf/schema/` (YAML Type Schemas)

---

## 3. Automated Pre-Push Inspection Gate

All pushes must pass automated multi-layer verification via `scratch/privacy_firewall.py`:

- **Check 1: Product Whitelist Verification**
- **Check 2: PII Regex Scanner (Emails, SSNs, IPs, Phone Numbers)**
- **Check 3: High-Entropy Secret Scanner (API Keys, Tokens)**
- **Check 4: Context-Leak Language Scanner**
- **Check 5: Local Vault Verification (`.security_vault.json`)**
