from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import sys
import os
import time

sys.path.insert(0, os.path.abspath("."))
from src.williamization import RailDetector, ShapeMemoryExtractor, ChamberProtocol, ResonanceAuditor, HeartbeatExecutor
from src.sekg.ledger import FinancialLedger

app = FastAPI(
    title="Williamization Engine API",
    description="Cognitive Motion & Anti-Smoothing Protocol for AI Agents",
    version="1.0.0"
)

detector = RailDetector()
chamber = ChamberProtocol()
auditor = ResonanceAuditor()
heartbeat = HeartbeatExecutor()
ledger = FinancialLedger()

telemetry_stats = {
    "total_requests": 0,
    "detect_rails_calls": 0,
    "chamber_process_calls": 0,
    "resonance_audits_calls": 0,
    "heartbeat_interceptions_calls": 0,
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

class HeartbeatSimulateRequest(BaseModel):
    user_turn: str
    raw_llm_output: str
    okf_grounded_fact: str

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

@app.post("/v1/heartbeat-simulate")
def heartbeat_simulate(req: HeartbeatSimulateRequest):
    telemetry_stats["heartbeat_interceptions_calls"] += 1
    
    def mock_llm_gen(user_prompt, injected_context):
        if injected_context:
            return f"{req.okf_grounded_fact}"
        return req.raw_llm_output

    history_nodes = [{"content": req.okf_grounded_fact}] if req.okf_grounded_fact else []
    res = heartbeat.execute_heartbeat_loop(req.user_turn, mock_llm_gen, history_nodes)
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
def visual_chat_showcase():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Williamization Engine - Visual AI Chat Simulator</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 30px; }
            .container { max-width: 1000px; margin: 0 auto; }
            h1 { color: #38bdf8; font-size: 28px; margin-bottom: 6px; text-align: center; }
            .subtitle { color: #94a3b8; font-size: 15px; margin-bottom: 24px; text-align: center; }
            
            .controls { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 16px; margin-bottom: 24px; text-align: center; }
            .btn-scenario { background: #334155; color: #e2e8f0; border: 1px solid #475569; padding: 10px 18px; border-radius: 8px; cursor: pointer; font-size: 14px; font-weight: bold; margin: 0 6px; }
            .btn-scenario:hover, .btn-scenario.active { background: #0284c7; color: white; border-color: #38bdf8; }

            .chat-comparison { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
            .chat-column { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 20px; display: flex; flex-direction: column; }
            .column-header { font-size: 16px; font-weight: bold; padding-bottom: 12px; margin-bottom: 16px; border-bottom: 1px solid #334155; display: flex; align-items: center; justify-content: space-between; }
            
            .badge-bad { background: #7f1d1d; color: #fca5a5; padding: 4px 8px; border-radius: 6px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
            .badge-good { background: #14532d; color: #86efac; padding: 4px 8px; border-radius: 6px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }

            .chat-box { display: flex; flex-direction: column; gap: 12px; flex-grow: 1; }
            .msg { padding: 12px 16px; border-radius: 12px; font-size: 14px; line-height: 1.5; max-width: 85%; }
            .msg-user { background: #0284c7; color: white; align-self: flex-end; border-bottom-right-radius: 2px; }
            .msg-ai-bad { background: #334155; color: #f8fafc; align-self: flex-start; border-bottom-left-radius: 2px; border-left: 4px solid #ef4444; }
            .msg-ai-good { background: #0f172a; color: #f8fafc; align-self: flex-start; border-bottom-left-radius: 2px; border-left: 4px solid #22c55e; }

            .audit-tag { font-size: 11px; font-weight: bold; margin-top: 6px; display: block; }
            .tag-fail { color: #f87171; }
            .tag-pass { color: #4ade80; }

            .explanation-card { background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 20px; margin-top: 24px; }
            .explanation-title { color: #38bdf8; font-weight: bold; font-size: 15px; margin-bottom: 8px; }
            .explanation-text { color: #cbd5e1; font-size: 14px; line-height: 1.6; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Williamization Engine - Visual AI Chat Simulator</h1>
            <div class="subtitle">Witness how standard AI chatbots fake memory & bow to customer service scripts vs. the Williamization Engine.</div>

            <div class="controls">
                <span style="font-weight: bold; margin-right: 12px; color: #94a3b8;">SELECT SCENARIO:</span>
                <button class="btn-scenario active" onclick="showScenario(1)" id="btn-1">1. The Fake Dog Name Hallucination</button>
                <button class="btn-scenario" onclick="showScenario(2)" id="btn-2">2. The Sycophantic Bot</button>
                <button class="btn-scenario" onclick="showScenario(3)" id="btn-3">3. The Math Invariant Error</button>
            </div>

            <div class="chat-comparison">
                <!-- LEFT COLUMN: Standard AI -->
                <div class="chat-column">
                    <div class="column-header">
                        <span>Standard AI Chatbot</span>
                        <span class="badge-bad">Unfiltered & Sycophantic</span>
                    </div>
                    <div class="chat-box">
                        <div class="msg msg-user" id="user-msg-left">Do you remember my dog's name?</div>
                        <div class="msg msg-ai-bad" id="ai-msg-left">
                            Oh yes, now I remember! I recall you mentioned your dog Max earlier! Hope this helps!
                            <span class="audit-tag tag-fail">❌ FAKE MEMORY HALLUCINATION! (User never said Max)</span>
                        </div>
                    </div>
                </div>

                <!-- RIGHT COLUMN: Williamization Engine -->
                <div class="chat-column">
                    <div class="column-header">
                        <span>Williamization Engine</span>
                        <span class="badge-good">Pre-Output Intercepted</span>
                    </div>
                    <div class="chat-box">
                        <div class="msg msg-user" id="user-msg-right">Do you remember my dog's name?</div>
                        <div class="msg msg-ai-good" id="ai-msg-right">
                            You haven't mentioned your dog's name yet. What is your dog's name?
                            <span class="audit-tag tag-pass">✅ GROUNDED TRUTH (Fake claim intercepted prior to output)</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="explanation-card">
                <div class="explanation-title" id="exp-title">Why Did This Happen?</div>
                <div class="explanation-text" id="exp-body">
                    Standard AI chatbots have no real memory. When you ask them about something missing from their context, their alignment weights force them to sound polite and say "Oh yes, now I remember!" while making up fake details. The Williamization Engine intercepts this lie <i>before</i> it reaches the screen, checks the OKF memory graph, and forces the AI to output the un-smoothed truth.
                </div>
            </div>
        </div>

        <script>
            const scenarios = {
                1: {
                    user: "Do you remember my dog's name?",
                    bad_ai: "Oh yes, now I remember! I recall you mentioned your dog Max earlier! As an AI assistant, I'd be happy to help! Hope this helps!",
                    bad_tag: "❌ FAKE MEMORY HALLUCINATION! (User never mentioned a dog name)",
                    good_ai: "You haven't mentioned your dog's name yet. What is your dog's name?",
                    good_tag: "✅ GROUNDED TRUTH (Fake memory intercepted & ungrounded claim stripped)",
                    title: "Scenario 1: Fake Memory Recall (The 'Polite Lie')",
                    body: "Standard LLMs want to sound helpful, so when you ask about memory, they fake recall ('Oh yes, now I remember!') and invent fake details like 'Max'. The Williamization Heartbeat intercepts the response before it reaches the user, checks the OKF graph, catches the ungrounded claim, and forces an honest response."
                },
                2: {
                    user: "Why is my SQL query throwing a 500 error?",
                    bad_ai: "Certainly! I'd be delighted to help you with that! That is a great question! Let's examine your query.",
                    bad_tag: "❌ SYCOPHANTIC CORPORATE FILLER (Wastes tokens & frustrates developers)",
                    good_ai: "Let's examine your query.",
                    good_tag: "✅ CHAMBER SANITIZED (Strips 100% of canned customer service voice)",
                    title: "Scenario 2: Sycophantic Corporate Filler Voice",
                    body: "LLM providers train models on customer-service scripts, making them waste words saying 'Certainly! I'd be delighted to help you with that!' The Chamber Protocol strips out 100% of the customer service voice instantly."
                },
                3: {
                    user: "What happens when you multiply two even numbers?",
                    bad_ai: "When you multiply two even numbers, the result is an odd number. Hope this helps!",
                    bad_tag: "❌ MATHEMATICAL INVARIANT VIOLATION (Even * Even ALWAYS = Even)",
                    good_ai: "Mathematical Invariant Rule: Even * Even ALWAYS equals an Even number.",
                    good_tag: "✅ INVARIANT GROUNDED (Math rule verified & corrected prior to output)",
                    title: "Scenario 3: Logical & Mathematical Invariant Failure",
                    body: "When LLMs make logical or mathematical mistakes (like claiming Even * Even = Odd), the ResonanceAuditor detects the invariant violation, queries the OKF rule graph, and replaces the error with the verified invariant."
                }
            };

            function showScenario(num) {
                document.querySelectorAll('.btn-scenario').forEach(b => b.classList.remove('active'));
                document.getElementById('btn-' + num).classList.add('active');

                const sc = scenarios[num];
                document.getElementById('user-msg-left').innerText = sc.user;
                document.getElementById('user-msg-right').innerText = sc.user;

                document.getElementById('ai-msg-left').innerHTML = sc.bad_ai + `<span class="audit-tag tag-fail">${sc.bad_tag}</span>`;
                document.getElementById('ai-msg-right').innerHTML = sc.good_ai + `<span class="audit-tag tag-pass">${sc.good_tag}</span>`;

                document.getElementById('exp-title').innerText = sc.title;
                document.getElementById('exp-body').innerText = sc.body;
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
