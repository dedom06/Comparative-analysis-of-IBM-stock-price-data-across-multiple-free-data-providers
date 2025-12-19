import requests
import json

url = (
    "https://api.stockdata.org/v1/data/eod?symbols=IBM&"
    "interval=day&"
    "date_from=2025-07-17&"
    "date_to=2025-12-05&"
    "format=json&"
    "api_token=api_key"
)

response = requests.get(url)
data = response.json()  

with open(r"filePath\DailyClosing_IBM_StockData.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

