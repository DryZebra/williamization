import os
import sys
import subprocess

def deploy_to_vercel():
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

    project_name = "williamization-engine"
    print(f"Deploying Williamization Engine API to Vercel Project '{project_name}'...")
    
    # Run vercel deploy with explicit --name and --token
    cmd = f"npx -y vercel deploy --yes --name={project_name} --token={token} --prod"
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
        if res.returncode == 0:
            print(f"\n>>> DEPLOYMENT SUCCESSFUL! Live Endpoint: https://{project_name}.vercel.app <<<")
            return True
        else:
            print(f"[FAIL] Vercel deploy exited with code {res.returncode}")
            return False
    except Exception as e:
        