""" Downloading meaningful html content of all the availabe pages"""
import requests
import os

# Create folder if not exists
os.makedirs("htmls", exist_ok=True)

for i in range(1,51):
  page_data = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
  with open(f"htmls/pages{i}.html", "w", encoding="utf-8") as a:
    a.write(page_data.text)
    print(f"Downloaded page{i}")
print("Completed")