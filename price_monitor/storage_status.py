import json
import os

STATUS_FILE = "refresh_status.json"


def load_status() -> dict:
    if not os.path.exists(STATUS_FILE):
        return {
            "last_refresh_at": None,
            "status": "never",
            "item_count": 0,
        }

    with open(STATUS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_status(status: dict) -> None:
    with open(STATUS_FILE, "w", encoding="utf-8") as file:
        json.dump(status, file, indent=2)
