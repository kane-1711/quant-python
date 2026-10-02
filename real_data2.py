import yfinance as yf
from dailyreturns2 import volatility

tickers=["RELIANCE.NS","TCS.NS","HDFCBANK.NS","IDEA.NS","HINDUNILVR.NS", "SUZLON.NS", "TSLA"]
results={}

for name in tickers:
    prices=yf.Ticker(name).history(period="5y")["Close"].tolist()
    results[name]=volatility(prices)

for name,v in sorted(results.items(), key=lambda item: item[1], reverse=True):
    print(name, "Daily=",round(v,2),"% Annual=",round((v*15.9),2),"%")