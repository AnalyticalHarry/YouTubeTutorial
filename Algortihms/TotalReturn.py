import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

class TotalReturn:
    def __init__(self, ticker, period):
        self.ticker = ticker
        self.period = period
        
    def calculate(self):
        self.close = yf.download(self.ticker, period=self.period)['Close']
        initial = self.close.values[0]
        final = self.close.values[-1]
        self.growth = (final - initial) / initial * 100
        print(f'Growth of {self.ticker} in {self.period} is {round(self.growth,2)} %')

    def plot_total_return(self):
        if hasattr(self, 'close'):
            daily_returns = self.close.pct_change(1) * 100
            cumulative_returns = daily_returns.cumsum()
            plt.figure(figsize=(10, 4))
            plt.plot(cumulative_returns)
            plt.title(f'{self.ticker} Total Return Percentage Over {self.period}')
            plt.xlabel('Date')
            plt.ylabel('Total Return Percentage')
            plt.grid(True, ls='--', alpha=0.5)
            plt.show()
        else:
            print('No data available to plot. Please run calculate() method first.')

ticker_list = [ "NVDA", "^GSPC"]
for i in range(len(ticker_list)):
    stock_return = TotalReturn(ticker_list[i], "1y")
    stock_return.calculate()
    stock_return.plot_total_return()
  
