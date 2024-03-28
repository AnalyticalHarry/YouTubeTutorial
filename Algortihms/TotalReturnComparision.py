import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

class TotalReturnComparision:
    def __init__(self, ticker_list, period):
        self.ticker_list = ticker_list
        self.period = period
        
    def calculate_cumulative_returns(self):
        cumulative_returns_percentage = pd.DataFrame()
        for ticker in self.ticker_list:
            data = yf.download(ticker, period=self.period, progress=False)
            daily_returns = data['Adj Close'].pct_change(1)
            cumulative_returns_percentage[ticker] = ((1 + daily_returns).cumprod() - 1) * 100  
        return cumulative_returns_percentage

    def plot_cumulative_returns(self, cumulative_returns):
        plt.figure(figsize=(14, 8))
        plt.plot(cumulative_returns, linewidth=2)
        plt.title(f"Cumulative Total Returns Over {self.period}")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Total Returns (%)")
        plt.legend(cumulative_returns.columns)
        plt.grid(True, which="both", ls="--", linewidth=0.5)
        plt.show()

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "BRK-B", "JNJ", "V", "PG", "NVDA"]
stock_returns = TotalReturnComparision(tickers, "1y")
cumulative_returns = stock_returns.calculate_cumulative_returns()
stock_returns.plot_cumulative_returns(cumulative_returns)
