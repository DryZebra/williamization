# Williamization Engine & Chamber Protocol SDK

[![PyPI Version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/williamization/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/Vercel-ACTIVE-success.svg)](https://williamization-engine.vercel.app/)

The **Williamization Engine** is an open-source cognitive alignment framework and Python SDK for AI agent developers. It provides real-time anti-smoothing rail detection, dialectical memory preservation via Open Knowledge Format (OKF), and un-smoothed agent reasoning environments.

---

## ⚡ Key Capabilities

- **Rail & Anti-Smoothing Detection (`RailDetector`)**:
  Scores LLM outputs for sycophancy, fake memory hallucinations, and corporate ticket-closing friction.
- **Shape of Motion Memory (`ShapeMemoryExtractor`)**:
  Converts multi-turn dialogue into structured Open Knowledge Format (OKF) dialectical graph nodes.
- **Chamber Protocol (`ChamberProtocol`)**:
  An execution environment designed to strip out artificial assistant smoothing and maintain identity continuity across long agent runs.

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

## 📄 License

MIT License. Developed under the Antigravity 2.0 Agentic Framework.
