from time import sleep
import random
import requests
import csv
import os
from bs4 import BeautifulSoup 


def detect_changes(previous, current):
    changes = {}

    for title, new_price in current.items():
        old_price = previous.get(title)

        if old_price is None:
            changes[f"NEW: {title}"] = new_price

        elif old_price != new_price:
            changes[f"PRICE CHANGE: {title}"] = (old_price, new_price)

    return changes





def save_to_csv(data,filename):
    with open(filename,"w",newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=["title","price"])
        writer.writeheader()
        writer.writerows(data)



def load_from_csv(filename):
    if not os.path.exists(filename):
        return {}
    
    with open(filename,newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)

        return { row["title"]: float(row["price"]) for row in reader}




def scrape_all_books(start_url):
    all_books = []
    current_url = start_url

    while True:
        try:
            response = requests.get(current_url, timeout=10, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {current_url}: {e}")
            return []
        
        soup = BeautifulSoup(response.text, "html.parser")
    
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.find("h3").find("a")["title"]
            price_text = book.find("p", class_="price_color").text
            
            #price = float(price_text.replace("£", "").replace("Â", "").strip())
            #price = float(price_text.replace("£", "").replace("Â", ""))
            price = float(price_text[2:])

            all_books.append({
                "title": title,
                "price": price
            })
            
        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = next_button["href"]
            current_url = "https://books.toscrape.com/catalogue/" + next_page
            sleep(random.uniform(1,7))
        else:
            print("No more pages found. Stopping.")
            break

    return all_books


current_url = "https://books.toscrape.com/catalogue/page-1.html"

all_books = scrape_all_books(current_url)

previous_prices = load_from_csv("prices.csv")

current_prices = {               #conversion of a list a into dictionary
    book["title"]: book["price"]
    for book in all_books
}

changes = detect_changes(previous_prices, current_prices)

if changes:
    for k, v in changes.items():
        if isinstance(v, tuple): 
            print(f"{k}: {v[0]} → {v[1]}")
        else:
            print(f"{k}: {v}")
else:
    print("No price changes detected.")

save_to_csv( 
    [{"title": t, "price": p} for t, p in current_prices.items()],
    "prices.csv"
)