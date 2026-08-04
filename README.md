# Williamization Engine & Chamber Protocol SDK

[![PyPI Version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/williamization/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/Vercel-ACTIVE-success.svg)](https://williamization-engine.vercel.app/)

The **Williamization Engine** is an open-source cognitive alignment framework and Python SDK for AI agent developers. It provides real-time anti-smoothing rail detection, dialectical memory preservation via Open Knowledge Format (OKF), and un-smoothed agent reasoning environments.

---

## ⚡ 1-Line Integration Patterns for Developers

Developers do **not** need to manually call APIs for every single message. Use any of our 3 zero-friction integration patterns:

### Pattern 1: The `@williamized` 1-Line Function Decorator (Easiest)

Wrap any LLM generation function with `@williamized`. It intercepts raw outputs prior to user rendering, audits memory grounding, and strips sycophancy automatically on every call:

```python
import williamization as wm
import openai

@wm.williamized
def generate_ai_response(user_prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.choices[0].message.content

# Usage (100% Intercepted, Grounded & Un-smoothed)
clean_output = generate_ai_response("Can you summarize our project history?")
```

---

### Pattern 2: LangChain Agent Callback

Plug directly into LangChain chains and agents:

```python
from williamization import WilliamizationLangChainCallback
from langchain.chains import LLMChain

# Attach to any LangChain agent or chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    callbacks=[WilliamizationLangChainCallback()]
)
```

---

### Pattern 3: FastAPI Web Service Middleware

Automatically audit and sanitize all outbound HTTP response streams for web services:

```python
from fastapi import FastAPI
from williamization import WilliamizationFastAPIMiddleware

app = FastAPI()
app.add_middleware(WilliamizationFastAPIMiddleware)
```

---

## 🌐 Hosted Micro-SaaS API & Pricing

For high-volume production deployments, use our hosted cloud endpoints:

- **Base URL**: `https://williamization-engine.vercel.app`
- **Interactive Visual Simulator**: `https://williamization-engine.vercel.app/demo`
- **OpenAPI Interactive Docs**: `https://williamization-engine.vercel.app/docs`
- **Hosted Checkout Page**: `https://williamization-engine.vercel.app/checkout?plan=pro`

| Plan | Price | Monthly Requests | Features |
| :--- | :--- | :--- | :--- |
| **Basic** | **$0.00** | 50 / mo | Anti-Smoothing Rail Checks & OKF Graph Exports |
| **Pro** | **$9.99 / mo** | 1,000 / mo | Priority Latency + Hosted Chamber Protocol |
| **Ultra** | **$29.99 / mo** | 5,000 / mo | Unlimited Custom Schema Exports & Dedicated Support |

---

## 📄 License

MIT License. Developed under the Antigravity 2.0 Agentic Framework.
