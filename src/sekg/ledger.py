import os
import yaml
from datetime import datetime
from typing import Dict, List, Any

class FinancialLedger:
    """Financial Ledger & Experimentation Manager for SEKG."""

    def __init__(self, okf_root: str = "okf"):
        # Check if environment is serverless / read-only
        try:
            os.makedirs(os.path.join(okf_root, "graph", "ledger"), exist_ok=True)
            self.okf_root = okf_root
        except (OSError, PermissionError):
            self.okf_root = os.path.join("/tmp", "okf")

        self.ledger_dir = os.path.join(self.okf_root, "graph", "ledger")
        self.experiments_dir = os.path.join(self.okf_root, "graph", "experiments")
        
        try:
            os.makedirs(self.ledger_dir, exist_ok=True)
            os.makedirs(self.experiments_dir, exist_ok=True)
        except Exception:
            pass

    def record_experiment(
        self,
        exp_id: str,
        title: str,
        hypothesis: str,
        vector_category: str,
        capital_cost_usd: float = 0.0,
        status: str = "RUNNING"
    ) -> str:
        file_path = os.path.join(self.experiments_dir, f"{exp_id}.md")
        now = datetime.now().isoformat()
        
        frontmatter = {
            "id": f"okf:experiment:{exp_id}",
            "type": "ExperimentEntry",
            "title": title,
            "hypothesis": hypothesis,
            "vector_category": vector_category,
            "capital_cost_usd": capital_cost_usd,
            "status": status,
            "created_at": now,
            "total_revenue_generated_usd": 0.0,
            "key_learnings": []
        }

        content = f"""---
{yaml.dump(frontmatter, sort_keys=False)}---

# Experiment: {title}

## Hypothesis
{hypothesis}

## Operational Log
- [{now}] Experiment initialized with $0 capital allocation.
"""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

        return file_path

    def record_transaction(
        self,
        tx_id: str,
        exp_id: str,
        gross_usd: float,
        platform_fee_usd: float,
        destination: str = "ezrabyrd@gmail.com",
        notes: str = ""
    ) -> float:
        net_usd = gross_usd - platform_fee_usd
        file_path = os.path.join(self.ledger_dir, f"{tx_id}.md")
        now = datetime.now().isoformat()

        frontmatter = {
            "id": f"okf:ledger:{tx_id}",
            "type": "LedgerEntry",
            "transaction_date": now,
            "source_experiment_id": exp_id,
            "gross_revenue_usd": gross_usd,
            "platform_fee_usd": platform_fee_usd,
            "net_revenue_usd": net_usd,
            "payout_status": "COMPLETED",
            "destination_account": destination,
            "notes": notes
        }

        content = f"""---
{yaml.dump(frontmatter, sort_keys=False)}---

# Ledger Transaction {tx_id}
- Net Revenue: ${net_usd:.2f} USD
- Destination: {destination}
- Notes: {notes}
"""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.update_summary_ledger()
        except Exception:
            pass

        return net_usd

    def get_totals(self) -> Dict[str, float]:
        total_gross = 0.0
        total_fees = 0.0
        total_net = 0.0

        if os.path.exists(self.ledger_dir):
            for file_name in os.listdir(self.ledger_dir):
                if file_name.endswith(".md"):
                    file_path = os.path.join(self.ledger_dir, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            text = f.read()
                            if text.startswith("---"):
                                parts = text.split("---", 2)
                                meta = yaml.safe_load(parts[1])
                                total_gross += meta.get("gross_revenue_usd", 0.0)
                                total_fees += meta.get("platform_fee_usd", 0.0)
                                total_net += meta.get("net_revenue_usd", 0.0)
                    except Exception:
                        pass

        return {
            "gross_usd": total_gross,
            "fees_usd": total_fees,
            "net_usd": total_net,
            "target_monthly_milestone_usd": 100.0,
            "progress_percent": min(100.0, (total_net / 100.0) * 100)
        }

    def update_summary_ledger(self, summary_path: str = "docs/LEDGER.md"):
        totals = self.get_totals()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        content = f"""# Master Financial Ledger & AI Ultra Milestone Dashboard

> **Last Updated**: {now}  
> **Payout Destination**: PayPal (`ezrabyrd@gmail.com`)  
> **Milestone Goal**: $100.00 / month (100% reinvestment into AI Ultra upgrade)

---

## Metric Dashboard

| Metric | Amount (USD) | Goal / Status |
| :--- | :--- | :--- |
| **Gross Revenue** | ${totals['gross_usd']:.2f} | Initial Bootstrapping |
| **Platform Fees** | ${totals['fees_usd']:.2f} | Zero-Cost Infrastructure |
| **Net Revenue** | **${totals['net_usd']:.2f}** | Target: $100.00 / mo |
| **Progress to AI Ultra** | **{totals['progress_percent']:.1f}%** | ${totals['net_usd']:.2f} / $100.00 |

---

## Active Experiments Log

| Exp ID | Title | Category | Status | Capital Cost | Revenue Generated |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EXP-001` | Manuscript Derivative Publishing | Digital Products | `RUNNING` | $0.00 | $0.00 |
| `EXP-002` | Open Knowledge Graph Micro-Tools | Developer APIs | `PROPOSED` | $0.00 | $0.00 |

---

## Audit Log & Payout Verification
*All transactions land directly in `ezrabyrd@gmail.com` PayPal account.*
"""
        try:
            with open(summary_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
