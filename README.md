# Price Monitor Automation

A Python-based price monitoring service that scrapes book prices from *Books to Scrape*, stores them locally, and exposes the data through a FastAPI backend.

This project focuses on **clean separation of concerns**, **manual refresh control**, and **data freshness visibility**, rather than continuous scraping.

---

## Features

- Scrapes all book titles and prices from Books to Scrape
- Stores scraped data in a CSV file
- Exposes a REST API using FastAPI
- Manual refresh endpoint to control scraping
- Status endpoint showing last refresh metadata
- Fast read access without triggering scrapes

---

## API Endpoints

### Health Check
GET /health

yaml
Copy code

Returns service health information.

---

### Get Latest Prices
GET /prices/latest

yaml
Copy code

Returns the most recently stored prices from CSV storage.

- Does **not** trigger scraping  
- Safe and fast to call repeatedly

---

### Refresh Prices (Manual)
POST /prices/refresh

yaml
Copy code

Triggers a full scrape of the website and updates stored prices.

- Intended to be called by the system (not end users)
- Expensive operation by design

---

### Refresh Status
GET /prices/status

yaml
Copy code

Returns metadata about the last refresh:

- Timestamp of last refresh
- Status (success / failure)
- Number of items scraped

---

## Project Structure

Price_Monitor_Automation/
├── README.md
├── requirements.txt
├── prices.csv
├── refresh_status.json
│
├── price_monitor/
│   ├── __init__.py
│   ├── scraper.py
│   ├── storage.py
│   ├── storage_status.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── services.py
│   │   └── test_services.py
│   │
│   └── working_reference.py

yaml
Copy code

---

## Design Decisions

- **Manual refresh instead of automatic scraping**
  - Prevents accidental load on the target site
  - Makes scraping an explicit, controlled action

- **Separation of read vs write paths**
  - `/prices/latest` reads cached data only
  - `/prices/refresh` performs scraping and storage

- **CSV storage**
  - Simple, transparent, and sufficient for this use case
  - Easy to replace later with a database if needed

---

## Setup & Run

### 1. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the API
bash
Copy code
uvicorn price_monitor.api.app:app --reload
API will be available at:

cpp
Copy code
http://127.0.0.1:8000
Swagger UI:

arduino
Copy code
http://127.0.0.1:8000/docs
Notes
HTTPS verification warnings are intentionally ignored for this portfolio project.

This project is not intended for production use.

The architecture is designed to be extended with scheduling, authentication, or database storage in the future.