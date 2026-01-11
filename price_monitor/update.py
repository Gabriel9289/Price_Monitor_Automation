# update.py
from storage import load_prices, save_prices
from detector import detect_changes


def update(current_prices: dict[str, float]):
    previous_prices = load_prices()

    changes = detect_changes(previous_prices, current_prices)

    if changes:
        for k, v in changes.items():
            if isinstance(v, tuple):
                print(f"{k}: {v[0]} → {v[1]}")
            else:
                print(f"{k}: {v}")
    else:
        print("No price changes detected.")

    save_prices(current_prices)
