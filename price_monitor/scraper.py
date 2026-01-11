# Responsible for scraping all book prices from the website
# scraper.py
from time import sleep
import random
import requests
from bs4 import BeautifulSoup


def scrape_all_books() -> dict[str, float]:
    all_books = {}
    url = "https://books.toscrape.com/catalogue/page-1.html"

    while True:
        try:
            response = requests.get(url, timeout=10, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url}: {e}")
            return all_books

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.find("h3").find("a")["title"]
            price_text = book.find("p", class_="price_color").text
            price = float(price_text[2:])

            all_books[title] = price  # ✅ key decision

        next_button = soup.select_one("li.next a")
        if next_button:
            url = "https://books.toscrape.com/catalogue/" + next_button["href"]
            sleep(random.uniform(1, 7))
        else:
            break

    return all_books
