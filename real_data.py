import yfinance as yf
from dailyreturns2 import volatility

ticker = yf.Ticker("RELIANCE.NS")
data = ticker.history(period="6mo")

prices = data["Close"].tolist()

print("Number of prices=", len(prices))
print("First 5 prices:",prices[:5])
print("Daily volatility:", round(volatility(prices),2),"%")