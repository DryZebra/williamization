import os
import json
import time
from typing import Dict, Any, List

class FinancialLedger:
    """
    Financial Ledger tracking payments and platform fee deductions.
    Destination account is extracted from PAYPAL_BUSINESS_EMAIL environment variable.
    """
    def __init__(self, okf_root: str = None, ledger_file: str = "okf_test_tmp/ledger.json"):
        self.okf_root = okf_root
        self.ledger_file = ledger_file
        os.makedirs(os.path.dirname(self.ledger_file), exist_ok=True)
        if not os.path.exists(self.ledger_file):
            self._save({"transactions": [], "experiments": []})

    def _load(self) -> Dict[str, Any]:
        try:
            with open(self.ledger_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"transactions": [], "experiments": []}

    def _save(self, data: Dict[str, Any]):
        with open(self.ledger_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def record_experiment(self, exp_id: str, title: str = "", status: str = "RUNNING", **kwargs) -> str:
        data = self._load()
        if "experiments" not in data:
            data["experiments"] = []
        exp = {
            "exp_id": exp_id,
            "title": title,
            "status": status,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "details": kwargs
        }
        data["experiments"].append(exp)
        self._save(data)
        
        if self.okf_root:
            exp_dir = os.path.join(self.okf_root, "graph", "experiments")
            os.makedirs(exp_dir, exist_ok=True)
            exp_file_path = os.path.join(exp_dir, f"{exp_id}.md")
            with open(exp_file_path, "w", encoding="utf-8") as f:
                f.write(f"# Experiment {exp_id}: {title}\nStatus: {status}\n")
            return exp_file_path
        return self.ledger_file

    def record_transaction(
        self,
        tx_id: str,
        exp_id: str,
        gross_usd: float,
        platform_fee_usd: float = 0.0,
        destination: str = None,
        notes: str = ""
    ) -> float:
        if not destination:
            destination = os.environ.get("PAYPAL_BUSINESS_EMAIL", "payments@williamization.org")

        net_usd = round(gross_usd - platform_fee_usd, 2)
        data = self._load()
        tx = {
            "tx_id": tx_id,
            "exp_id": exp_id,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "gross_usd": gross_usd,
            "platform_fee_usd": platform_fee_usd,
            "net_usd": net_usd,
            "destination": destination,
            "notes": notes
        }
        data["transactions"].append(tx)
        self._save(data)
        return net_usd

    def get_totals(self) -> Dict[str, float]:
        data = self._load()
        total_gross = sum(t.get("gross_usd", 0.0) for t in data["transactions"])
        total_fee = sum(t.get("platform_fee_usd", 0.0) for t in data["transactions"])
        total_net = sum(t.get("net_usd", 0.0) for t in data["transactions"])
        target_monthly_goal = 100.00
        progress_pct = round((total_net / target_monthly_goal) * 100, 1)
        return {
            "gross_usd": round(total_gross, 2),
            "fee_usd": round(total_fee, 2),
            "net_usd": round(total_net, 2),
            "total_gross_usd": round(total_gross, 2),
            "total_fee_usd": round(total_fee, 2),
            "total_net_usd": round(total_net, 2),
            "progress_percent": progress_pct
        }
