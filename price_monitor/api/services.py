#services.py
from price_monitor.storage import load_prices ,save_prices
from price_monitor.scraper import scrape_all_books
from price_monitor.storage_status import save_status
from price_monitor.storage_status import load_status
from datetime import datetime, timezone




def refresh_prices():
    items = scrape_all_books()
    save_prices(items)

    status = {
    "last_refresh_at": datetime.now(timezone.utc).isoformat(),
    "status": "success",
    "item_count": len(items),
    }


    save_status(status)

    return {
        "status": "ok",
        "source": "live-scrape",
        "count": len(items),
    }

def get_refresh_status():
    return load_status()
 
def get_latest_prices():
    """
    Service layer:
    - Calls scraper
    - Shapes data for the API
    """
    prices = load_prices()

    items = [
        {"title": title, "price": price}
        for title, price in prices.items()
    ]

    return {
        "items": items,
        "source": "csv-cashe",
        "count": len(items),
    }



