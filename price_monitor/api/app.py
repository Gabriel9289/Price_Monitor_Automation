from fastapi import FastAPI  #app.py
from price_monitor.api.services import get_latest_prices ,refresh_prices,get_refresh_status

app = FastAPI()


@app.post("/prices/refresh")
def refresh_prices_endpoint():
    return refresh_prices()


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "price-monitor",
        "version": "0.1.0"
    }


@app.get("/prices/latest")
def prices_latest():
    return get_latest_prices()

@app.get("/prices/status")
def prices_status():
    return get_refresh_status()