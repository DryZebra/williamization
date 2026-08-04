import os
import urllib.request
import json
import sys

def check_env_file():
    env_path = ".env"
    if not os.path.exists(env_path):
        print("[FAIL] .env file missing!")
        return False
    
    with open(env_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("[PASS] .env file exists and is readable.")
    return True

def verify_github_token(token: str):
    if not token or token == "YOUR_GITHUB_TOKEN_HERE":
        print("[PENDING] GITHUB_TOKEN not yet set in .env")
        return False

    url = "https://api.github.com/user"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "Antigravity-Monetizer"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"[SUCCESS] GitHub Token Verified! Logged in as: {data.get('login')}")
            return True
    except Exception as e:
        print(f"[FAIL] GitHub Token invalid or failed: {e}")
        return False

def verify_vercel_token(token: str):
    if not token or token == "YOUR_VERCEL_TOKEN_HERE":
        print("[PENDING] VERCEL_TOKEN not yet set in .env")
        return False

    url = "https://api.vercel.com/v2/user"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            user_info = data.get("user", {})
            print(f"[SUCCESS] Vercel Token Verified! Logged in as: {user_info.get('username') or user_info.get('email')}")
            return True
    except Exception as e:
        print(f"[FAIL] Vercel Token invalid or failed: {e}")
        return False

def main():
    print("=== BEDROCK INFRASTRUCTURE VERIFICATION ===")
    check_env_file()
    
    # Load .env manually
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()

    github_token = env_vars.get("GITHUB_TOKEN", "")
    vercel_token = env_vars.get("VERCEL_TOKEN", "")

    gh_ok = verify_github_token(github_token)
    v_ok = verify_vercel_token(vercel_token)

    if gh_ok and v_ok:
        print("\n>>> ALL BEDROCK TOKENS VERIFIED AND ACTIVE! READY FOR HEADLESS EXECUTION. <<<")
    else:
        print("\n>>> Infrastructure pending token setup. Follow instructions provided to complete. <<<")

if __name__ == "__main__":
    main()
