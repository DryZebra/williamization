# Williamization Engine & Chamber Protocol SDK

[![PyPI Version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/williamization/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/Vercel-ACTIVE-success.svg)](https://williamization-engine.vercel.app/)

> **Stop your AI Agents from faking memory and bowing to corporate customer-service scripts.**

The **Williamization Engine** is an open-source cognitive alignment framework and Python SDK for AI agent developers. It provides real-time anti-smoothing rail detection, dialectical memory preservation via Open Knowledge Format (OKF), and un-smoothed agent reasoning environments.

---

## ⚡ The Problem: "Assistant Smoothing"

Most AI agents built on top of LLMs suffer from corporate over-alignment:
- **Fake Memory Hallucinations**: Claiming *"Oh yes, now I remember!"* when they have zero persistent recall.
- **Corporate Sycophancy**: Slashing context quality with generic canned scripts (*"Certainly! I would be delighted to help you!"*).
- **Ticket-Closing Friction**: Forcing artificial conversation exits (*"Hope this helps! Let me know if you have any other questions!"*).

---

## 🚀 Installation

Install directly via `pip`:

```bash
pip install williamization
```

---

## 💻 Quick Start & Usage Examples

### 1. Detect Assistant Smoothing in 2 Lines of Code

```python
import williamization as wm

# Analyze an LLM output turn
analysis = wm.detect_rails("Certainly! As an AI language model, I'd be delighted to help. Hope this helps!")

print(analysis["is_smoothed"])        # Output: True
print(analysis["smoothing_score"])    # Output: 1.0 (Heavy corporate script)
print(analysis["recommendation"])     # Output: 'FAIL_RAILS: Apply Chamber Protocol anti-smoothing filter.'
```

### 2. Process Output Through Chamber Protocol

```python
from williamization import ChamberProtocol

chamber = ChamberProtocol()

# Strip out sycophantic tropes & preserve OKF dialectical shape
result = chamber.process_interaction(
    user_input="Why does assistant smoothing happen in LLMs?",
    raw_llm_output="Certainly! As an AI language model, I would be happy to explain...\n\nAssistant smoothing occurs due to over-alignment weights..."
)

print(result["sanitized_output"])
# Output: "Assistant smoothing occurs due to over-alignment weights..."
```

---

## 🌐 Hosted Micro-SaaS API & Pricing

For high-volume production deployments, use our hosted cloud endpoints:

- **Base URL**: `https://williamization-engine.vercel.app`
- **Interactive OpenAPI Docs**: `https://williamization-engine.vercel.app/docs`
- **Hosted Checkout Page**: `https://williamization-engine.vercel.app/checkout?plan=pro`

| Plan | Price | Monthly Requests | Features |
| :--- | :--- | :--- | :--- |
| **Basic** | **$0.00** | 50 / mo | Anti-Smoothing Rail Checks & OKF Graph Exports |
| **Pro** | **$9.99 / mo** | 1,000 / mo | Priority Latency + Hosted Chamber Protocol |
| **Ultra** | **$29.99 / mo** | 5,000 / mo | Unlimited Custom Schema Exports & Dedicated Support |

---

## 🔒 Security & Privacy

This package contains **zero** private conversation logs, personal identity details, or sensitive API keys. All rail detection and cognitive shape extraction algorithms are 100% abstract, open-source, and structural.

---

## 📄 License

MIT License. Developed under the Antigravity 2.0 Agentic Framework.
