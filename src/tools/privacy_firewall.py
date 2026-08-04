import os
import subprocess
import sys

# FORBIDDEN PATH PATTERNS & EXTENSIONS
FORBIDDEN_PATTERNS = [
    "conversations",
    ".docx",
    ".env",
    "Materialist Christianity EBook",
    "Materialist_Christianity_Volume_II",
    "scratch",
    "OKF/conversations"
]

# FORBIDDEN META-CHAT CONTEXT LEAK STRINGS IN PUBLIC FILES
FORBIDDEN_TEXT_LEAKS = [
    "private conversation logs",
    "personal identity details",
    "chat history",
    "my boss",
    "defensive privacy",
    "internal chat",
    "leaked"
]

def audit_git_staging() -> bool:
    """
    Inspects all files tracked or staged in git for path violations and text context leaks.
    """
    res = subprocess.run("git ls-files", shell=True, capture_output=True, text=True, errors="ignore")
    tracked_files = [f.strip() for f in res.stdout.splitlines() if f.strip()]

    violations = []
    text_leaks = []

    for f in tracked_files:
        f_norm = f.replace("\\", "/")
        # 1. Path Audit
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.lower() in f_norm.lower():
                violations.append(f)
                break

        # 2. Text Context Leak Audit (Skip firewall script itself from text-search)
        if f_norm.endswith((".md", ".py", ".toml", ".json", ".yaml", ".txt")) and "privacy_firewall.py" not in f_norm:
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as file_obj:
                    content_lower = file_obj.read().lower()
                    for leak in FORBIDDEN_TEXT_LEAKS:
                        if leak in content_lower:
                            text_leaks.append(f"{f} (contains: '{leak}')")
            except Exception:
                pass

    if violations or text_leaks:
        print("\n==================================================")
        print("[CRITICAL SECURITY BLOCK] PRE-PUSH PRIVACY & CONTEXT FIREWALL TRIGGERED!")
        if violations:
            print("Forbidden/Personal File Paths Detected:")
            for v in violations:
                print(f"  - {v}")
        if text_leaks:
            print("Internal Meta-Chat Context Leaks Detected in Text:")
            for tl in text_leaks:
                print(f"  - {tl}")
        print("PUSH ABORTED. Sanitize files before attempting to push.")
        print("==================================================\n")
        return False

    print("[PASS] Privacy & Context Firewall Audit Passed: 0 context leaks detected.")
    return True

if __name__ == "__main__":
    if not audit_git_staging():
        sys.exit(1)
    print("Pre-push privacy audit complete.")
