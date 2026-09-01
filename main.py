from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI(title="Porsche Dashboard API")

# ─── SERVE STATIC IMAGES ──────────────────────────────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")

# ─── STATIC DATA ──────────────────────────────────────────────────────────

# Existing data (kept for charts 0-5)
MARGIN = {
    "years": ["2022","2023","2024","2025","2026","2027(P)","2028(P)"],
    "margin": [18.0, 18.6, 15.0, 12.5, 10.8, 15.5, 18.2],
    "china": [93.3, 79.3, 64.1, 41.9, 33.0, 48.0, 62.0]
}

REGIONAL = {
    "regions": ["N.America","Europe","China","Germany","Overseas"],
    "2023": [86.0, 70.2, 79.3, 32.4, 52.2],
    "2026": [76.5, 62.0, 33.0, 28.1, 46.0]
}

POWERTRAIN = {
    "labels": ["2022","2024","2026 (Strategy)","2028 (Target)"],
    "BEV": [11, 13, 20, 35],
    "PHEV": [15, 19, 30, 35],
    "ICE": [74, 68, 50, 30]
}

PRODUCTION = {
    "plants": ["Zuffenhausen","Leipzig","Other"],
    "2025": [82, 94, 28],
    "2026": [68, 85, 22]
}

QUALITY = {
    "quarters": ["Q1","Q2","Q3","Q4"],
    "defect": [120, 95, 78, 65],
    "complaints": [42, 38, 29, 21]
}

REGION_MIX = {
    "labels": ["N.America","Europe","China","Germany","Overseas"],
    "values": [30, 28, 18, 14, 10]
}

# ─── NEW DATA FOR EXPANDED PAGES ──────────────────────────────────────────

SOLUTIONS_DATA = {
    "pillars": [
        {
            "id": "china",
            "title": "China Market Re‑entry",
            "icon": "fa-earth-asia",
            "color": "#d5001c",
            "kpi": {"label": "Recovery Target", "value": "62k units", "change": "+46%"},
            "description": "Porsche is re‑establishing its premium positioning in China through localized EV production, a strategic joint venture with Geely, and dynamic pricing recalibration.",
            "actions": [
                "Localized Taycan & Macan EV production in Shanghai by Q4 2026",
                "Joint venture for battery swapping infrastructure with Geely",
                "Dynamic pricing model – 12% reduction on entry trims, 5% increase on exclusive Sonderwunsch models",
                "Direct‑to‑consumer digital showroom expansion in 15 tier‑1 cities"
            ],
            "status": "In Progress"
        },
        {
            "id": "software",
            "title": "Software & Cariad Overhaul",
            "icon": "fa-code",
            "color": "#00b4d8",
            "kpi": {"label": "Delivery Delay Reduction", "value": "18→3 mos", "change": "-83%"},
            "description": "Accelerating internal software capabilities to reduce dependency on Cariad, with a focus on driver‑assistance, UI/UX, and OTA updates.",
            "actions": [
                "Porsche OS 2.0 – in‑house infotainment stack (launch Q1 2027)",
                "Google partnership for navigation & voice AI integration",
                "Agile sprint squads – 8 cross‑functional teams working in 2‑week cycles",
                "Open‑source contributions to the Automotive Grade Linux project"
            ],
            "status": "Delayed"
        },
        {
            "id": "powertrain",
            "title": "Powertrain Flexibility",
            "icon": "fa-gears",
            "color": "#d4af37",
            "kpi": {"label": "PHEV Mix Target", "value": "35%", "change": "+16pp"},
            "description": "Maintaining margin stability by balancing ICE, PHEV, and BEV production based on regional demand signals – plus eFuel commercialisation.",
            "actions": [
                "Flexible assembly line – switch between powertrains in < 45 minutes",
                "eFuel plant in Chile – scale to 2.5M litres by year‑end",
                "Cayenne & Panamera PHEV battery upgrade (27 kWh → 45 kWh)",
                "Retrofit program for existing ICE vehicles to run on eFuel"
            ],
            "status": "On Track"
        }
    ]
}

FINANCIALS_DATA = {
    "labels": ["Baseline 2026", "+ China Re-entry", "+ Software Catch-up", "+ PHEV/eFuel Mix", "Recovery 2028"],
    "revenue": [38.2, 4.5, 2.1, 3.8, 48.6],
    "ebit": [4.1, 0.9, 0.4, 0.8, 6.2],
    "margin": [10.8, 12.2, 13.0, 14.5, 18.2]
}

RISK_MATRIX = {
    "quadrants": [
        {"id": "high-impact", "label": "High Impact / High Feasibility", "items": ["China Localisation", "PHEV Portfolio", "eFuel Scaling"]},
        {"id": "high-risk", "label": "High Impact / Low Feasibility", "items": ["Full BEV Transition", "Cariad Replacement"]},
        {"id": "quick-wins", "label": "Low Impact / High Feasibility", "items": ["Exclusive Manufaktur", "Dealer Morale"]},
        {"id": "monitor", "label": "Low Impact / Low Feasibility", "items": ["Hydrogen Fuel Cell", "Fully Autonomous"]}
    ]
}

PLAYBOOK_DATA = {
    "rapid": [
        {"phase": "Recommend", "owner": "Aviraj (ENFP-T)", "desc": "Propose China re‑entry strategy and dealer engagement plan"},
        {"phase": "Agree", "owner": "Amaan (ISFJ-T)", "desc": "Approve capital allocation and cost models"},
        {"phase": "Perform", "owner": "Krrish (ENTP-A)", "desc": "Execute software audit and platform decoupling"},
        {"phase": "Input", "owner": "Riaan (ENFP-T)", "desc": "Provide market intelligence and partner landscapes"},
        {"phase": "Decide", "owner": "Devansh (ESFP)", "desc": "Final brand communication and go‑to‑market narrative"}
    ],
    "templates": [
        {"title": "Investor Update", "desc": "Quarterly letter highlighting margin recovery, China progress, and software milestones."},
        {"title": "Dealer Bulletin", "desc": "Weekly brief on inventory allocation, pricing adjustments, and customer retention incentives."},
        {"title": "Media Statement", "desc": "Crisis communication boilerplate for EV transition and Cariad delays – emphasising engineering heritage."}
    ]
}

# ─── API ENDPOINTS ──────────────────────────────────────────────────────────

@app.get("/api/margin")
async def get_margin(): return MARGIN

@app.get("/api/regional")
async def get_regional(): return REGIONAL

@app.get("/api/powertrain")
async def get_powertrain(): return POWERTRAIN

@app.get("/api/production")
async def get_production(): return PRODUCTION

@app.get("/api/quality")
async def get_quality(): return QUALITY

@app.get("/api/region-mix")
async def get_region_mix(): return REGION_MIX

# ─── NEW ENDPOINTS ──────────────────────────────────────────────────────────

@app.get("/api/solutions")
async def get_solutions(): return SOLUTIONS_DATA

@app.get("/api/financials")
async def get_financials(): return FINANCIALS_DATA

@app.get("/api/risk-matrix")
async def get_risk_matrix(): return RISK_MATRIX

@app.get("/api/playbook")
async def get_playbook(): return PLAYBOOK_DATA

# ─── SERVE INDEX ───────────────────────────────────────────────────────────

@app.get("/")
async def serve_index():
    return FileResponse("index.html")