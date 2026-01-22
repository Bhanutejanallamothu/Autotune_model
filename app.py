from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse
from starlette.middleware.base import BaseHTTPMiddleware
import os
from ultralytics import YOLO

model = YOLO("models/yolo11n.pt")

from src.parts.api_parts import app as parts_app
from src.diagnostics.api_diagnostics import app as diagnostics_app
from src.ECU.api import app as ecu_app


class LowercasePathMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.scope["path"]
        lower_path = path.lower()
        if path != lower_path:
            return RedirectResponse(lower_path)
        return await call_next(request)


app = FastAPI(
    title="AutoTuning.AI Unified API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:9002",
        "https://*.hf.space"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(LowercasePathMiddleware)

app.mount("/parts", parts_app)
app.mount("/diagnostics", diagnostics_app)
app.mount("/ecu", ecu_app)

if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "AutoTuning.AI",
        "apis": {
            "parts": "/parts",
            "diagnostics": "/diagnostics",
            "ecu": "/ecu"
        }
    }

@app.get("/{full_path:path}")
async def spa_fallback(full_path: str):
    index_path = os.path.join("static", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "Not Found"}
