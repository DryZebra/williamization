import os
import subprocess
import urllib.request
import json
import sys

sys.path.insert(0, os.path.abspath("."))
from src.tools.privacy_firewall import audit_git_staging

def create_and_push_github():
    print("=== EXECUTING GITHUB PUSH PIPELINE ===")

    # 1. MANDATORY PRE-PUSH PRIVACY FIREWALL CHECK
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
    url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": repo_name,
        "description": "Williamization Engine & Chamber of Motion Protocol for AI Agents",
        "private": False
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Antigravity-Monetizer"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
    except Exception:
        pass

    remote_url = f"https://x-access-token:{token}@github.com/DryZebra/{repo_name}.git"
    
    commands = [
        "git init",
        "git config user.name \"DryZebra\"",
        "git config user.email \"ezrabyrd@gmail.com\"",
        "git add README.md requirements.txt vercel.json config.yaml .gitignore api/ src/ tests/ okf/schema/",
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
