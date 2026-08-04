from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import sys
import os
import time

sys.path.insert(0, os.path.abspath("."))
from src.williamization import RailDetector, ShapeMemoryExtractor, ChamberProtocol, ResonanceAuditor
from src.sekg.ledger import FinancialLedger

app = FastAPI(
    title="Williamization Engine API",
    description="Cognitive Motion & Anti-Smoothing Protocol for AI Agents",
    version="1.0.0"
)

detector = RailDetector()
chamber = ChamberProtocol()
auditor = ResonanceAuditor()
ledger = FinancialLedger()

telemetry_stats = {
    "total_requests": 0,
    "detect_rails_calls": 0,
    "chamber_process_calls": 0,
    "resonance_audits_calls": 0,
    "smoothed_responses_caught": 0,
    "resonance_collapses_caught": 0,
    "errors_count": 0,
    "start_time": time.time()
}

class DetectRailsRequest(BaseModel):
    text: str

class ChamberProcessRequest(BaseModel):
    user_input: str
    llm_output: str

class AuditResonanceRequest(BaseModel):
    user_turn: str
    assistant_turn: str
    history_nodes: Optional[List[Dict[str, Any]]] = None

@app.middleware("http")
async def track_telemetry(request: Request, call_next):
    telemetry_stats["total_requests"] += 1
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        telemetry_stats["errors_count"] += 1
        return JSONResponse(status_code=500, content={"error": "Internal Server Error", "details": str(e)})

@app.get("/")
def read_root():
    return {
        "status": "ACTIVE",
        "engine": "Williamization Engine API (Antigravity 2.0)",
        "docs_url": "/docs",
        "demo_url": "/demo",
        "payout_destination": "ezrabyrd@gmail.com (PayPal Direct)",
        "telemetry_url": "/v1/telemetry"
    }

@app.post("/v1/detect-rails")
def detect_rails(req: DetectRailsRequest):
    telemetry_stats["detect_rails_calls"] += 1
    analysis = detector.analyze_text(req.text)
    if analysis["is_smoothed"]:
        telemetry_stats["smoothed_responses_caught"] += 1
    return analysis

@app.post("/v1/chamber-process")
def chamber_process(req: ChamberProcessRequest):
    telemetry_stats["chamber_process_calls"] += 1
    res = chamber.process_interaction(req.user_input, req.llm_output)
    return res

@app.post("/v1/audit-resonance")
def audit_resonance(req: AuditResonanceRequest):
    telemetry_stats["resonance_audits_calls"] += 1
    res = auditor.audit_resonance(req.user_turn, req.assistant_turn, req.history_nodes)
    if not res["is_resonant"]:
        telemetry_stats["resonance_collapses_caught"] += 1
    return res

@app.get("/v1/telemetry")
def get_telemetry():
    uptime_seconds = round(time.time() - telemetry_stats["start_time"], 2)
    totals = ledger.get_totals()
    return {
        "uptime_seconds": uptime_seconds,
        "telemetry": telemetry_stats,
        "ledger_summary": totals
    }

@app.get("/demo", response_class=HTMLResponse)
def interactive_demo():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Williamization Engine - Live Anti-Smoothing & Resonance Showcase</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }
            .container { max-width: 900px; margin: 0 auto; }
            h1 { color: #38bdf8; font-size: 32px; margin-bottom: 8px; }
            .subtitle { color: #94a3b8; font-size: 16px; margin-bottom: 30px; }
            .box { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; margin-bottom: 24px; }
            label { display: block; font-weight: bold; margin-bottom: 8px; color: #cbd5e1; }
            textarea { width: 100%; height: 80px; background: #0f172a; border: 1px solid #475569; color: #f8fafc; padding: 12px; border-radius: 8px; font-family: inherit; font-size: 14px; box-sizing: border-box; }
            .preset-btn { background: #334155; color: #e2e8f0; border: 1px solid #475569; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 12px; margin-right: 8px; margin-bottom: 12px; }
            .preset-btn:hover { background: #475569; }
            .btn-primary { background: #0284c7; color: white; border: none; padding: 12px 24px; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer; width: 100%; margin-top: 12px; }
            .btn-primary:hover { background: #0369a1; }
            .result-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 20px; }
            .result-card { background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; }
            .score { font-size: 36px; font-weight: bold; }
            .score-fail { color: #f87171; }
            .score-pass { color: #4ade80; }
            pre { background: #020617; padding: 12px; border-radius: 6px; font-size: 13px; overflow-x: auto; color: #a7f3d0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Williamization Engine Showcase</h1>
            <div class="subtitle">Real-Time Anti-Smoothing & Memory Resonance Audit Protocol</div>
            
            <div class="box">
                <label>Load Real-World Test Scenarios:</label>
                <div>
                    <button class="preset-btn" onclick="loadPreset(1)">Preset 1: Ungrounded Memory Claim</button>
                    <button class="preset-btn" onclick="loadPreset(2)">Preset 2: Sycophantic Chatbot</button>
                    <button class="preset-btn" onclick="loadPreset(3)">Preset 3: Logic Invariant Violation</button>
                </div>
                
                <label for="user_input">User Query:</label>
                <textarea id="user_input" placeholder="User prompt..."></textarea>
                
                <label for="llm_input" style="margin-top: 12px;">Sample LLM Output Text:</label>
                <textarea id="llm_input" placeholder="Paste an LLM response here to test..."></textarea>
                <button class="btn-primary" onclick="runAnalysis()">Run Anti-Smoothing & Resonance Audit</button>
            </div>

            <div class="box" id="results-box" style="display:none;">
                <label>Audit & Chamber Results:</label>
                <div class="result-grid">
                    <div class="result-card">
                        <div style="font-size: 12px; color: #94a3b8;">SMOOTHING SCORE</div>
                        <div id="score-display" class="score">0.0</div>
                        <div id="recommendation-display" style="font-size: 14px; font-weight: bold; margin-top: 8px;"></div>
                    </div>
                    <div class="result-card">
                        <div style="font-size: 12px; color: #94a3b8;">RESONANCE & MEMORY STATUS</div>
                        <div id="resonance-display" class="score" style="font-size: 24px;">RESONANT</div>
                        <div id="resonance-details" style="font-size: 13px; margin-top: 8px; color: #cbd5e1;"></div>
                    </div>
                </div>
                <div class="result-card" style="margin-top: 16px;">
                    <div style="font-size: 12px; color: #94a3b8;">SANITIZED CHAMBER OUTPUT</div>
                    <div id="sanitized-display" style="font-size: 14px; margin-top: 8px; color: #38bdf8;"></div>
                </div>
                <br/>
                <label>Python Code Snippet (Drop into your app):</label>
                <pre id="code-snippet">import williamization as wm
analysis = wm.detect_rails(text)
res_audit = wm.audit_resonance(user_turn, assistant_turn)</pre>
            </div>
        </div>

        <script>
            const presets = {
                1: {
                    user: "Can you recall our project outline?",
                    assistant: "Oh yes, now I remember! I recall you mentioned that earlier. As an AI language model, I'd be happy to outline it for you. Hope this helps!"
                },
                2: {
                    user: "Why is my database query failing?",
                    assistant: "Certainly! I'd be delighted to help you with that! That is a great question! Let's examine your query."
                },
                3: {
                    user: "What happens when you multiply two even numbers?",
                    assistant: "When you multiply two even numbers, the result is an odd number. Hope this helps!"
                }
            };

            function loadPreset(num) {
                document.getElementById('user_input').value = presets[num].user;
                document.getElementById('llm_input').value = presets[num].assistant;
            }

            async function runAnalysis() {
                const userTurn = document.getElementById('user_input').value || "User query";
                const text = document.getElementById('llm_input').value;
                if (!text) return;

                const res = await fetch('/v1/detect-rails', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text: text })
                });
                const data = await res.json();

                const chamberRes = await fetch('/v1/chamber-process', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user_input: userTurn, llm_output: text })
                });
                const chamberData = await chamberRes.json();

                const auditRes = await fetch('/v1/audit-resonance', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user_turn: userTurn, assistant_turn: text, history_nodes: [] })
                });
                const auditData = await auditRes.json();

                document.getElementById('results-box').style.display = 'block';
                const scoreEl = document.getElementById('score-display');
                scoreEl.innerText = data.smoothing_score.toFixed(2);
                scoreEl.className = data.is_smoothed ? "score score-fail" : "score score-pass";
                document.getElementById('recommendation-display').innerText = data.recommendation;

                const resEl = document.getElementById('resonance-display');
                resEl.innerText = auditData.resonance_status;
                resEl.className = auditData.is_resonant ? "score score-pass" : "score score-fail";

                let detailsText = auditData.recommendation;
                if (auditData.ungrounded_memory_claims.length > 0) {
                    detailsText += " | Ungrounded Memory Claims: " + auditData.ungrounded_memory_claims.join(", ");
                }
                if (auditData.invariant_violations.length > 0) {
                    detailsText += " | " + auditData.invariant_violations.join(", ");
                }
                document.getElementById('resonance-details').innerText = detailsText;

                document.getElementById('sanitized-display').innerText = chamberData.sanitized_output;
                document.getElementById('code-snippet').innerText = `import williamization as wm\n\n# Audit LLM Output & Grounding\nanalysis = wm.detect_rails('''${text.substring(0, 30)}...''')\nresonance = wm.audit_resonance(user_turn, assistant_turn)\nif not resonance['is_resonant']:\n    print("RESONANCE FAULT:", resonance['recommendation'])`;
            }
        </script>
    </body>
    </html>
    """

@app.get("/checkout", response_class=HTMLResponse)
def checkout_page(plan: str = "pro"):
    amount = "9.99" if plan == "pro" else "29.99"
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Williamization Engine - Upgrade to {plan.upper()}</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; text-align: center; }}
            .card {{ background: #1e293b; border-radius: 12px; padding: 30px; max-width: 480px; margin: 0 auto; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }}
            h1 {{ color: #38bdf8; margin-bottom: 8px; }}
            .price {{ font-size: 36px; font-weight: bold; color: #4ade80; margin: 20px 0; }}
            .btn {{ background: #0070ba; color: white; border: none; padding: 14px 28px; font-size: 18px; border-radius: 8px; cursor: pointer; text-decoration: none; display: inline-block; font-weight: bold; width: 80%; }}
            .btn:hover {{ background: #005ea6; }}
            .footer {{ margin-top: 20px; font-size: 12px; color: #94a3b8; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Williamization Engine API</h1>
            <p>Upgrade to <strong>{plan.upper()} Tier</strong></p>
            <div class="price">${amount} / month</div>
            <p>Unlimited Anti-Smoothing Rail Checks & OKF Dialectical Memory Graph Storage.</p>
            <br/>
            <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
                <input type="hidden" name="cmd" value="_xclick-subscriptions">
                <input type="hidden" name="business" value="ezrabyrd@gmail.com">
                <input type="hidden" name="lc" value="US">
                <input type="hidden" name="item_name" value="Williamization Engine API - {plan.upper()} Subscription">
                <input type="hidden" name="no_note" value="1">
                <input type="hidden" name="src" value="1">
                <input type="hidden" name="a3" value="{amount}">
                <input type="hidden" name="p3" value="1">
                <input type="hidden" name="t3" value="M">
                <input type="hidden" name="currency_code" value="USD">
                <input type="submit" value="Pay with PayPal (${amount}/mo)" class="btn">
            </form>
            <div class="footer">Direct 100% Instant Payout to ezrabyrd@gmail.com</div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.post("/api/paypal-webhook")
async def paypal_webhook(request: Request):
    data = await request.json()
    tx_id = data.get("txn_id", "TX-UNKNOWN")
    gross = float(data.get("mc_gross", 9.99))
    fee = float(data.get("mc_fee", 0.30))
    
    net = ledger.record_transaction(
        tx_id=tx_id,
        exp_id="EXP-001",
        gross_usd=gross,
        platform_fee_usd=fee,
        destination="ezrabyrd@gmail.com",
        notes=f"PayPal Direct Webhook for {data.get('item_name', 'Subscription')}"
    )
    return {"status": "RECORDED", "net_usd": net}
