import os
import subprocess
import urllib.request
import json

def create_and_push_github():
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
    print(f"Creating GitHub repository '{repo_name}' for user DryZebra...")

    # Create repo via GitHub REST API if not exists
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
            print(f"[SUCCESS] Repository created on GitHub: {data.get('html_url')}")
    except Exception as e:
        print(f"[INFO] Repo creation response: {e} (Repo may already exist).")

    # Configure local git remote & push
    remote_url = f"https://x-access-token:{token}@github.com/DryZebra/{repo_name}.git"
    
    commands = [
        "git init",
        "git config user.name \"DryZebra\"",
        "git config user.email \"ezrabyrd@gmail.com\"",
        "git add .",
        "git commit -m \"Initial commit: Williamization Engine & Chamber of Motion Protocol\"",
        "git branch -M main",
        f"git remote remove origin",
        f"git remote add origin {remote_url}",
        "git push -u origin main --force"
    ]

    for cmd in commands:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        # Print output without exposing token
        clean_cmd = cmd.replace(remote_url, "https://github.com/DryZebra/williamization.git")
        if res.returncode == 0:
            print(f"[PASS] {clean_cmd}")
        else:
            print(f"[WARN] {clean_cmd}: {res.stderr.strip()}")

    print(f"\n>>> REPOSITORY PUSHED TO GITHUB: https://github.com/DryZebra/williamization <<<")
    return True

if __name__ == "__main__":
    create_and_push_github()
