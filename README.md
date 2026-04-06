# 📚 Books to Scrape – Web Scraping Project

## 📌 Overview

This project demonstrates **end-to-end web scraping using Python**, where data is collected from the demo website:

👉 https://books.toscrape.com/

The system extracts structured information about books such as:

* Title
* Price
* Star Rating
* Stock Availability

The scraped data is processed and stored in a **CSV dataset**, making it ready for analysis or further machine learning tasks.

---

## 🎯 Objectives

* Learn how to scrape data from websites
* Extract meaningful information from HTML
* Build a structured dataset from raw web data
* Understand real-world scraping workflows
* Handle multiple pages efficiently

---

## 🧱 Project Architecture

```text
Website (books.toscrape.com)
        ↓
Download HTML Pages
        ↓
Parse HTML (BeautifulSoup)
        ↓
Extract Book Data
        ↓
Store in Python List
        ↓
Convert to DataFrame
        ↓
Export to CSV
```

---

## 📂 Project Structure

```text
project/
│
├── htmls/                      # Downloaded HTML pages
│   ├── pages1.html
│   ├── pages2.html
│   └── ...
│
├── download_web_pages.py       # Step 1: Download pages
├── extract_info.py             # Step 2: Extract data
├── save_to_csv.py              # Step 3: Save to CSV
│
├── Book_description.csv        # Final dataset
└── README.md
```

---

## ⚙️ Workflow Explained

### 🔹 Step 1: Download HTML Pages

**File:** `download_web_pages.py`

* Uses `requests` to fetch web pages
* Iterates through 50 pages
* Saves HTML locally for offline processing

```python
for i in range(1, 51):
    requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
```

✅ Benefits:

* Avoids repeated API calls
* Faster processing
* Safer (reduces server load)

---

### 🔹 Step 2: Extract Information

**File:** `extract_info.py`

* Uses `BeautifulSoup` for parsing HTML
* Extracts:

  * Title
  * Price
  * Star Rating
  * Availability

```python
articles = soup.select("article.product_pod")
```

### Extracted Fields:

| Field              | Description             |
| ------------------ | ----------------------- |
| Title              | Book name               |
| Price              | Cost in GBP (£)         |
| Star Rating        | Rating (One to Five)    |
| Stock Availability | In stock / Out of stock |

---

### 🔹 Step 3: Save to CSV

**File:** `save_to_csv.py`

* Converts extracted data into a Pandas DataFrame
* Saves it as a CSV file

```python
df.to_csv("Book_description.csv", index=False)
```

---

## 📊 Sample Output

```text
Title                                 Price   Star Rating   Stock Availability
A Light in the Attic                  51.77   Three         In stock
Tipping the Velvet                    53.74   One           In stock
Sapiens: A Brief History of Humankind 54.23   Five          In stock
```

---

## 🧠 Key Concepts Covered

* Web Scraping Fundamentals
* HTTP Requests using `requests`
* HTML Parsing using `BeautifulSoup`
* CSS Selectors for data extraction
* Data Cleaning & Structuring
* File Handling in Python
* Data Export using Pandas

---

## 💻 Technologies Used

* Python
* Requests
* BeautifulSoup (bs4)
* Pandas

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install requests beautifulsoup4 pandas
```

---

### 2. Download HTML Pages

```bash
python download_web_pages.py
```

---

### 3. Extract Data

```bash
python extract_info.py
```

---

### 4. Save to CSV

```bash
python save_to_csv.py
```

---

## ⚠️ Important Notes

### ✅ File Handling Safety

* Checks if HTML file exists before processing:

```python
if not os.path.exists(filepath):
```

### ✅ Clean Data Extraction

* Removes unwanted symbols like `£` from price
* Uses `.get_text(strip=True)` for clean text

---

## 🎓 Learning Outcome

By completing this project, you will:

* Understand real-world web scraping workflows
* Learn how to extract structured data from websites
* Build reusable and scalable scraping pipelines
* Prepare data for analytics or ML applications

---

## 📌 Conclusion

This project demonstrates a **complete web scraping pipeline**, from downloading raw HTML pages to generating a structured dataset.

It serves as a strong foundation for:

* Data Engineering
* Data Analysis
* Machine Learning pipelines

---
