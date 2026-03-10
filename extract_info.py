"""Extracting meaningful content from HTML pages"""

from bs4 import BeautifulSoup
import os

items=[]

# with open("htmls/pages1.html",  encoding="utf-8") as a:
#     content = a.read()

# soup = BeautifulSoup(content, "html.parser")

# articles = soup.select("article.product_pod")

# for article in articles:
#     title = article.find("h3").find("a")["title"]
#     price = article.select_one("p.price_color").text.split("£")[1]
#     rating = article.select_one("p.star-rating")
#     rating_class = rating.get("class")[1]
#     availablity = article.select_one("p.instock.availability").get_text(strip=True)
#     items.append([title, price, rating_class, availablity])
#     print(title, price, rating_class, availablity)

for page_no in range(1, 51):

    filepath = f"htmls/pages{page_no}.html"

    if not os.path.exists(filepath):
        print(f"Skipping missing file: {filepath}")
        continue

    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    articles = soup.select("article.product_pod")

    for article in articles:
        title = article.find("h3").find("a")["title"]
        price = article.select_one("p.price_color").text.split("£")[1]
        rating_class = article.select_one("p.star-rating").get("class")[1]
        availability = article.select_one("p.instock.availability").get_text(strip=True)

        items.append([title, price, rating_class, availability])

print(f"Extracted {len(items)} records from all pages.")