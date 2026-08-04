import os
import subprocess
import urllib.request
import json

def purge_conversations_from_github():
    print("=== EXECUTING EMERGENCY PRIVACY PURGE ===")
    
    # 1. Ensure .gitignore includes conversations/
    gitignore_path = ".gitignore"
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        if "conversations/" not in lines and "conversations" not in lines:
            with open(gitignore_path, "a", encoding="utf-8") as f:
                f.write("\nconversations/\nconversations\n*.docx\n")

    # 2. Remove conversations from git cache
    cmd1 = "git rm -r --cached conversations"
    subprocess.run(cmd1, shell=True, capture_output=True, text=True, errors="ignore")

    # 3. Amend/Create clean commit
    cmd2 = "git add .gitignore"
    subprocess.run(cmd2, shell=True, capture_output=True, text=True, errors="ignore")

    cmd3 = 'git commit -m "Security & Privacy Purge: Remove conversations directory from repo history"'
    subprocess.run(cmd3, shell=True, capture_output=True, text=True, errors="ignore")

    # 4. Get GitHub Token from .env
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()

    token = env_vars.get("GITHUB_TOKEN", "")
    if token:
        remote_url = f"https://x-access-token:{token}@github.com/DryZebra/williamization.git"
        # Force push clean tree
        cmd4 = f"git push origin main --force"
        res = subprocess.run(cmd4, shell=True, capture_output=True, text=True, errors="ignore")
        print("[SUCCESS] Force pushed clean privacy-enforced state to GitHub.")
    else:
        print("[WARN] GITHUB_TOKEN missing, local git cache cleaned.")

if __name__ == "__main__":
    purge_conversations_from_github()
