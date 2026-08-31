from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI(title="Porsche Dashboard API")

# ─── Static data (replace with DB/CSV later) ──────────────────────────────
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

# ─── API endpoints ──────────────────────────────────────────────────────────

@app.get("/api/margin")
async def get_margin():
    return MARGIN

@app.get("/api/regional")
async def get_regional():
    return REGIONAL

@app.get("/api/powertrain")
async def get_powertrain():
    return POWERTRAIN

@app.get("/api/production")
async def get_production():
    return PRODUCTION

@app.get("/api/quality")
async def get_quality():
    return QUALITY

@app.get("/api/region-mix")
async def get_region_mix():
    return REGION_MIX

# ─── Serve the frontend ─────────────────────────────────────────────────────
# FastAPI will serve index.html at the root.
# No need for a separate Node server.

@app.get("/")
async def serve_index():
    return FileResponse("index.html")