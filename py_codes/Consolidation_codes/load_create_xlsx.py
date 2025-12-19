import json
from openpyxl import Workbook

filePath_StockData      = r"filePath\DailyClosing_IBM_StockData.json"        
filePath_AlphaVantage   = r"filePath\DailyClosing_IBM_AlphaVantage.json"
filePath_MarketStack    = r"CfilePath\DailyClosing_IBM_Marketstack.json"

opened_StockData = open(filePath_StockData, "r", encoding="utf-8")
key_StockData = "data"
data_StockData = json.load(opened_StockData)[key_StockData]

opened_AlphaVantage = open(filePath_AlphaVantage, "r", encoding="utf-8")
key_AlphaVantage = "Time Series (Daily)"
data_AlphaVantage = json.load(opened_AlphaVantage)[key_AlphaVantage]

opened_MarketStack = open(filePath_MarketStack, "r", encoding="utf-8")
key_MarketStack = "data"
data_MarketStack = json.load(opened_MarketStack)[key_MarketStack]

wb = Workbook()
ws = wb.active

ws.append([
    "Date",
    "Opening StockData", "Opening MarketStack", "Diff opening adj",
    
    "Opening Alphavantage", "Opening MarketStack", "Diff opening unAdj",

    "Closing StockData", "Closing MarketStack", "Diff closing adj",
    
    "Closing Alphavantage", "Closing MarketStack", "Diff closing unAdj",

    "Volume StockData", "Volume MarketStack", "Diff Volume", 
    "Volume Alphavantage", "Volume MarketStack", "Diff volume"
])

for i in range(len(data_StockData)):
    date = data_StockData[i]["date"][0:10]
    
    if date in data_AlphaVantage:
        opening_StockData = float(data_StockData[i]["open"])
        opening_AlphaVantage = float(data_AlphaVantage[date]["1. open"])
        diff_opening = opening_AlphaVantage - opening_StockData

        closing_StockData = float(data_StockData[i]["close"])
        closing_AlphaVantage = float(data_AlphaVantage[date]["4. close"])
        diff_closing = closing_AlphaVantage - closing_StockData

        volume_StockData = float(data_StockData[i]["volume"])
        volume_AlphaVantage = float(data_AlphaVantage[date]["5. volume"])
        diff_volume = volume_AlphaVantage - volume_StockData

        ws.append([
            date,

            opening_StockData, opening_AlphaVantage, diff_opening,

            closing_StockData, closing_AlphaVantage, diff_closing,

            volume_StockData, volume_AlphaVantage, diff_volume
        ])

wb.save(r"filePath\overviewData.xlsx")

opened_StockData.close
opened_AlphaVantage.close