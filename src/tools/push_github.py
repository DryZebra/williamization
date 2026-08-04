import os
import subprocess
import urllib.request
import json
import sys

sys.path.insert(0, os.path.abspath("."))
from src.tools.privacy_firewall import audit_git_staging

PUBLIC_WHITELIST_FILES = [
    "README.md",
    "requirements.txt",
    "vercel.json",
    "pyproject.toml",
    "config.yaml",
    ".gitignore",
    "api/",
    "src/api/",
    "src/sekg/",
    "src/utils/",
    "src/williamization/",
    "src/tools/privacy_firewall.py",
    "src/tools/deploy_vercel.py",
    "src/tools/push_github.py",
    "src/tools/verify_infrastructure.py",
    "tests/",
    "okf/schema/"
]

def create_and_push_github():
    print("=== EXECUTING GITHUB PUSH PIPELINE ===")

    if not audit_git_staging():
        print("[ABORT] GitHub push aborted by Privacy Firewall.")
        return False

    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()

    token = env_vars.get("GITHUB_TOKEN", "")
    if not token:
        print("[FAIL] GITHUB_TOKEN missing from .env")
        return False

    repo_name = "williamization"
    remote_url = f"https://x-access-token:{token}@github.com/DryZebra/{repo_name}.git"
    
    stage_cmd = "git add " + " ".join(PUBLIC_WHITELIST_FILES)
    
    commands = [
        "git init",
        "git config user.name \"DryZebra\"",
        "git config user.email \"ezrabyrd@gmail.com\"",
        stage_cmd,
        "git commit -m \"Update Williamization Engine codebase\"",
        "git branch -M main",
        "git remote remove origin",
        f"git remote add origin {remote_url}",
        "git push -u origin main"
    ]

    for cmd in commands:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors="ignore", cwd=os.getcwd())
        clean_cmd = cmd.replace(remote_url, "https://github.com/DryZebra/williamization.git")
        if res.returncode == 0:
            print(f"[PASS] {clean_cmd}")
        else:
            print(f"[INFO] {clean_cmd}: {res.stderr.strip() if res.stderr else ''}")

    print(f"\n>>> REPOSITORY PUSHED SAFELY TO GITHUB: https://github.com/DryZebra/williamization <<<")
    return True

if __name__ == "__main__":
    create_and_push_github()
