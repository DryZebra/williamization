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

def audit_git_staging() -> bool:
    """
    Inspects all files tracked or staged in git.
    Returns True if 100% clean, False if ANY forbidden file is detected.
    """
    res = subprocess.run("git ls-files", shell=True, capture_output=True, text=True, errors="ignore")
    tracked_files = [f.strip() for f in res.stdout.splitlines() if f.strip()]

    violations = []
    for f in tracked_files:
        f_norm = f.replace("\\", "/")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.lower() in f_norm.lower():
                violations.append(f)
                break

    if violations:
        print("\n==================================================")
        print("[CRITICAL SECURITY BLOCK] PRE-PUSH PRIVACY FIREWALL TRIGGERED!")
        print("The following forbidden/personal files were detected in Git:")
        for v in violations:
            print(f"  - {v}")
        print("PUSH ABORTED. Remove these files before attempting to push.")
        print("==================================================\n")
        return False

    print("[PASS] Privacy Firewall Audit Passed: 0 personal/forbidden files tracked.")
    return True

if __name__ == "__main__":
    if not audit_git_staging():
        sys.exit(1)
    print("Pre-push privacy audit complete.")
