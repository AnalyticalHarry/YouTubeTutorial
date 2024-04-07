import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def plot_daily_growth(tickers, period):
    plt.figure(figsize=(20, 8))
    for ticker in tickers:
        try:
            data = yf.download(ticker, period=period, progress=False)['Adj Close']
            daily_growth = (data / data.iloc[0] * 100) - 100
            plt.plot(daily_growth.index, daily_growth, label=ticker, lw=1)
        except Exception as e:
            print(f"Failed to download {ticker}: {e}")
    plt.title(f'Daily Growth Comparison Over {period}')
    plt.xlabel('Date')
    plt.ylabel('Growth(%)')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.show()

tickers = ["GLD", "UUP", "GC=F","DX-Y.NYB"]
period = "10y"  
plot_daily_growth(tickers, period)
