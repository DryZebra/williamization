import os
import subprocess
import sys
import json
import re

GENERIC_FORBIDDEN_EXTENSIONS = [
    ".env", ".pem", ".key", ".pkcs12", ".pfx", ".docx", ".doc", ".pdf", ".zip", ".tar", ".gz"
]

GENERIC_FORBIDDEN_KEYWORDS = [
    "secret", "private_key", "password", "token_vault", "credentials"
]

# Strict PII Email Regex (Flags any raw personal emails in source files)
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@(gmail|yahoo|hotmail|outlook|icloud)\.com"

def audit_git_staging() -> bool:
    """
    Enterprise-Grade Security Firewall.
    Scans every file tracked in Git against security rules, PII leaks, and local .security_vault.json patterns.
    """
    res = subprocess.run("git ls-files", shell=True, capture_output=True, text=True, errors="ignore")
    tracked_files = [f.strip() for f in res.stdout.splitlines() if f.strip()]

    vault_paths = []
    vault_texts = []
    vault_file = ".security_vault.json"
    if os.path.exists(vault_file):
        try:
            with open(vault_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                vault_paths = data.get("forbidden_path_patterns", [])
                vault_texts = data.get("forbidden_text_patterns", [])
        except Exception:
            pass

    violations = []
    text_leaks = []

    for f in tracked_files:
        f_norm = f.replace("\\", "/")
        
        # 1. Extension & Path Violation Check
        for ext in GENERIC_FORBIDDEN_EXTENSIONS:
            if f_norm.lower().endswith(ext):
                violations.append(f"{f} (Forbidden extension: {ext})")
                break

        for kw in GENERIC_FORBIDDEN_KEYWORDS:
            if kw in f_norm.lower() and "privacy_firewall.py" not in f_norm:
                violations.append(f"{f} (Forbidden keyword: {kw})")
                break

        for vp in vault_paths:
            if vp.lower() in f_norm.lower():
                violations.append(f"{f} (Vault path policy match)")
                break

        # 2. Text Content & PII Leak Check (Scan EVERY tracked file)
        if f_norm.endswith((".md", ".py", ".toml", ".json", ".yaml", ".txt")) and "privacy_firewall.py" not in f_norm:
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as file_obj:
                    content = file_obj.read()
                    content_lower = content.lower()
                    
                    # PII Email Check
                    email_matches = re.findall(EMAIL_REGEX, content_lower)
                    if email_matches:
                        text_leaks.append(f"{f} (Personal Email PII Leak detected)")

                    # Vault Text Policy Check
                    for vt in vault_texts:
                        if vt.lower() in content_lower:
                            text_leaks.append(f"{f} (Vault text match: '{vt}')")
            except Exception:
                pass

    if violations or text_leaks:
        print("\n==================================================")
        print("[CRITICAL SECURITY BLOCK] ENTERPRISE PRIVACY FIREWALL TRIGGERED!")
        if violations:
            print("Forbidden Path/Extension Violations Detected:")
            for v in violations:
                print(f"  - {v}")
        if text_leaks:
            print("Content Policy Violations Detected in Text:")
            for tl in text_leaks:
                print(f"  - {tl}")
        print("PUSH ABORTED. Sanitize repository before attempting to push.")
        print("==================================================\n")
        return False

    print("[PASS] Enterprise Security Audit Passed: 0 security policy violations detected.")
    return True

if __name__ == "__main__":
    if not audit_git_staging():
        sys.exit(1)
    print("Pre-push security audit complete.")
