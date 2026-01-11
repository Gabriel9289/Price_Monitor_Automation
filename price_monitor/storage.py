# Responsible for loading and saving prices to CSV
# storage.py
import csv
import os


def load_prices(filename="prices.csv") -> dict[str, float]:
    if not os.path.exists(filename):
        return {}

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return {row["title"]: float(row["price"]) for row in reader}


def save_prices(prices: dict[str, float], filename="prices.csv") -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price"])
        writer.writeheader()

        for title, price in prices.items():
            writer.writerow({"title": title, "price": price})

