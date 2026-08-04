from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import sys
import os
import time

sys.path.insert(0, os.path.abspath("."))
from src.williamization import RailDetector, ShapeMemoryExtractor, ChamberProtocol
from src.sekg.ledger import FinancialLedger

app = FastAPI(
    title="Williamization Engine API",
    description="Cognitive Motion & Anti-Smoothing Protocol for AI Agents",
    version="1.0.0"
)

detector = RailDetector()
chamber = ChamberProtocol()
ledger = FinancialLedger()

# In-memory telemetry counter
telemetry_stats = {
    "total_requests": 0,
    "detect_rails_calls": 0,
    "chamber_process_calls": 0,
    "smoothed_responses_caught": 0,
    "errors_count": 0,
    "start_time": time.time()
}

class DetectRailsRequest(BaseModel):
    text: str

class ChamberProcessRequest(BaseModel):
    user_input: str
    llm_output: str

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

@app.get("/v1/telemetry")
def get_telemetry():
    uptime_seconds = round(time.time() - telemetry_stats["start_time"], 2)
    totals = ledger.get_totals()
    return {
        "uptime_seconds": uptime_seconds,
        "telemetry": telemetry_stats,
        "ledger_summary": totals
    }

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
