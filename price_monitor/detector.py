# Responsible for comparing old and new prices

# detector.py
def detect_changes(previous: dict, current: dict) -> dict:
    changes = {}

    for title, new_price in current.items():
        old_price = previous.get(title)

        if old_price is None:
            changes[f"NEW: {title}"] = new_price

        elif old_price != new_price:
            changes[f"PRICE CHANGE: {title}"] = (old_price, new_price)

    return changes
