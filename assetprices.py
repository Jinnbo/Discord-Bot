# Sharpe Ratio Calculator
# For Cryptocurrency 

import yfinance as yf
import math
import statistics

def close_price(ticker):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="max")

    return hist['Close'][-1]

def ticker_detail(ticker):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="max")

    return type(hist)

print(ticker_detail("TSLA"))


def price_daily(ticker,start,end):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="max",interval="1d")

    past_price_daily = []
    for i in range(len(hist)):
        past_price_daily.append(hist['Close'][i])

    return past_price_daily


def price_weekly(ticker):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="max",interval="1wk")

    past_price_weekly = []

    for i in range(len(hist)):
        past_price_weekly.append(hist['Close'][i])

    return past_price_weekly

def sr(ticker):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="max")

    past_price = []
    for i in range(len(hist)):
        past_price.append(hist['Close'][i])

    daily_returns = []
    for i in range(len(past_price)-1):
        daily_change = past_price[i+1]-past_price[i]
        percent = daily_change/past_price[i]
        daily_percent_change = percent*100
        daily_returns.append(daily_percent_change)

    average_daily_return = sum(daily_returns)/len(daily_returns)
    sharpe_ratio =average_daily_return/statistics.stdev(daily_returns)*math.sqrt(365)

    return sharpe_ratio

#print(price("BTC-USD"))
#print(sr("BTC-USD"))

