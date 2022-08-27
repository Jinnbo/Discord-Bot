# Graph price over time with matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

def daily_graph(ticker):

    plt.figure()

    tick = yf.Ticker(ticker)
    ticker_history = tick.history('max','1d')

    sf = ticker_history['Close']
    df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})

    date = df['Date'].tolist()
    price = df['Values'].tolist()

    plt.style.use('fast')
    plt.plot(date,price)

    currency = "USD"
    if len(ticker) >3:
        if ticker[-4] == "-":
            if ticker[-3:] != "USD":
                currency = ticker[-3:]


    plt.title(f'{ticker.upper()} Daily Price Chart')
    plt.ylabel(f'{currency.upper()} Price($)')
    plt.xlabel('Date (daily)', rotation=0)
    #plt.show()
    plt.savefig(f'{ticker}daily.png')

def weekly_graph(ticker):

    plt.figure()

    tick = yf.Ticker(ticker)
    ticker_history = tick.history('max', '1wk')

    sf = ticker_history['Close']
    df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})

    date = df['Date'].tolist()
    price = df['Values'].tolist()

    plt.style.use('fast')
    plt.plot(date,price)

    currency = "USD"
    if len(ticker) > 3:
        if ticker[-4] == "-":
            if ticker[-3:] != "USD":
                currency = ticker[-3:]

    plt.title(f'{ticker.upper()} Weekly Price Chart')
    plt.ylabel(f'{currency.upper()} Price ($)')
    plt.xlabel('Date (weekly)', rotation=0)
    plt.savefig(f'{ticker}weekly.png')



    
