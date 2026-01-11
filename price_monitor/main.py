# FastAPI entry point and request orchestration
#main.py
from scraper import scrape_all_books
from update import update

current_url = "https://books.toscrape.com/catalogue/page-1.html"

prices = scrape_all_books(current_url)
update(prices)
