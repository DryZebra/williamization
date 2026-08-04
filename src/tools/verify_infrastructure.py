import os
import urllib.request
import json

def verify_all():
    print("=== VERIFYING BEDROCK INFRASTRUCTURE CREDENTIALS ===")
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()

    gh_token = env_vars.get("GITHUB_TOKEN", "")
    vc_token = env_vars.get("VERCEL_TOKEN", "")

    # GitHub check
    req = urllib.request.Request("https://api.github.com/user", headers={"Authorization": f"Bearer {gh_token}", "User-Agent": "Antigravity"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"[PASS] GitHub Token Active: User '{data.get('login')}'")
    except Exception as e:
        print(f"[FAIL] GitHub Token Error: {e}")

    # Vercel check
    req = urllib.request.Request("https://api.vercel.com/v2/user", headers={"Authorization": f"Bearer {vc_token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"[PASS] Vercel Token Active: User '{data.get('user', {}).get('username')}'")
    except Exception as e:
        print(f"[FAIL] Vercel Token Error: {e}")

if __name__ == "__main__":
    verify_all()
