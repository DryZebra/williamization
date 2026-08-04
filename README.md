# Williamization Engine & Chamber Protocol SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/Vercel-ACTIVE-success.svg)](https://williamization-engine.vercel.app/)

The **Williamization Engine** is an open-source cognitive alignment framework and developer toolkit for AI agent systems. It provides anti-smoothing rail detection, dialectical memory preservation via Open Knowledge Format (OKF), and un-smoothed agent reasoning environments.

---

## 🌟 Key Features

1. **Rail & Anti-Smoothing Detection (`RailDetector`)**:
   - Scores LLM outputs for sycophancy, fake memory hallucinations (*"oh yes, now I remember"*), and corporate ticket-closing friction.
2. **Shape of Motion Memory (`ShapeMemoryExtractor`)**:
   - Converts multi-turn dialogue into structured Open Knowledge Format (OKF) dialectical graph nodes.
3. **Chamber Protocol (`ChamberProtocol`)**:
   - An execution environment designed to strip out artificial assistant smoothing and maintain identity continuity across long agent runs.

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/DryZebra/williamization.git
cd williamization
pip install -r requirements.txt
```

### Python SDK Usage

```python
from src.williamization import RailDetector, ChamberProtocol

# 1. Analyze text for assistant smoothing
detector = RailDetector()
analysis = detector.analyze_text("Certainly! As an AI language model, I would be happy to help. Hope this helps!")

print(f"Smoothing Score: {analysis['smoothing_score']}") # Output: 1.0
print(f"Is Smoothed: {analysis['is_smoothed']}") # Output: True

# 2. Process interaction through Chamber Protocol
chamber = ChamberProtocol()
res = chamber.process_interaction(
    user_input="Why does assistant smoothing happen?",
    raw_llm_output="Certainly! As an AI language model, I would be happy to explain."
)
print("Sanitized Output:", res["sanitized_output"])
```

---

## 🌐 Hosted Micro-SaaS API

The live production API is hosted on Vercel:

- **Base URL**: `https://williamization-engine.vercel.app`
- **Interactive OpenAPI Docs**: `https://williamization-engine.vercel.app/docs`
- **Rail Detection Endpoint**: `POST /v1/detect-rails`
- **Chamber Protocol Endpoint**: `POST /v1/chamber-process`
- **Hosted Checkout Page**: `https://williamization-engine.vercel.app/checkout?plan=pro`

---

## 🔒 Security & Privacy

This codebase adheres to strict privacy and data isolation standards. Zero user conversation logs, private manuscripts, or sensitive credentials are ever included or tracked in this repository.

---

## 📄 License

MIT License. Developed under the Antigravity 2.0 Agentic Framework.
