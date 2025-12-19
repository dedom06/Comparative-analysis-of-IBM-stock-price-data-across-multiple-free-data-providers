import requests
import json


url = (
    "https://api.marketstack.com/v2/eod?symbols=IBM&"
    "date_from=2025-07-17&"
    "date_to=2025-12-05&"
    "access_key=api_key"
)

response = requests.get(url)
data = response.json()  

with open(r"filePath\DailyClosing_IBM_Marketstack.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

