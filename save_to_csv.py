
from extract_info import items
import pandas as pd

df = pd.DataFrame(items, columns=["Title", "Price", "Star Rating", "Stock Availability"])
df.to_csv("Book_description.csv", index=False)

print("CSV saved successfully!")