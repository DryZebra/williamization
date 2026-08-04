import os
import subprocess
import json

def deploy_to_vercel():
    print("Deploying Williamization Engine API to Vercel Project 'williamization-engine'...")
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()

    token = env_vars.get("VERCEL_TOKEN", "")
    if not token:
        print("[FAIL] VERCEL_TOKEN missing from .env")
        return False

    cmd = f"npx vercel --token {token} --prod --yes"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors="ignore")
    print("STDOUT:", res.stdout.strip())
    print("STDERR:", res.stderr.strip())

    if res.returncode == 0:
        print("\n>>> DEPLOYMENT SUCCESSFUL! Live Endpoint: https://williamization-engine.vercel.app <<<")
        return True
    else:
        print("[FAIL] Vercel deployment failed.")
        return False

if __name__ == "__main__":
    deploy_to_vercel()
