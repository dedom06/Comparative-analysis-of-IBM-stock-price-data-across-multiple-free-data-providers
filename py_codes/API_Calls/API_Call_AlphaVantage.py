import requests
import json

# Documentation: https://www.alphavantage.co/documentation/

url = (
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&"
    "symbol=IBM&"
    "apikey=api_key"
)

request = requests.get(url)
data = request.json()

with open(r"filePath\DailyClosing_IBM_AlphaVantage.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
