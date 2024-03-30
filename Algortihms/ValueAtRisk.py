import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

#class Portfolio Var to calculate value at risk
class PortfolioVaR:
    def __init__(self, tickers, period, weights):
        self.tickers = tickers
        self.period = period
        self.weights = np.array(weights)
        self.data = None
        self.daily_returns = None
        self.portfolio_returns = None
        self.portfolio_loss = None
        self.cumulative_portfolio_returns = None
      
    # method to get data from ticker and calculate return
    def fetch_data(self):
        self.data = yf.download(" ".join(self.tickers), period=self.period)['Adj Close']
        self.daily_returns = self.data.pct_change().dropna()

  # method for portfolio return and loss
    def calculate_portfolio_returns(self):
        self.portfolio_returns = self.daily_returns.dot(self.weights)
        self.portfolio_loss = self.portfolio_returns.quantile(0.05)
        self.cumulative_portfolio_returns = (1 + self.portfolio_returns).cumprod()

  # method to plot result
    def plot_results(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
        self.cumulative_portfolio_returns.plot(ax=ax1, color='dodgerblue', linewidth=1)
        ax1.set_title('Historical Cumulative Portfolio Returns', fontsize=14)
        ax1.set_xlabel('Date', fontsize=12)
        ax1.set_ylabel('Cumulative Returns', fontsize=12)
        ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

        ax2.hist(self.portfolio_returns, bins=100, alpha=0.75, color='dodgerblue')
        ax2.axvline(self.portfolio_loss, color='crimson', linestyle='--', linewidth=2, label=f'5th Percentile (VaR): {self.portfolio_loss*100:.2f}%')
        ax2.set_title('Historical Simulation of Portfolio Loss', fontsize=14)
        ax2.set_xlabel('Daily Portfolio Returns', fontsize=12)
        ax2.set_ylabel('Frequency', fontsize=12)
        ax2.legend(fontsize=12)
        ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
        
        plt.tight_layout()
        plt.show()

    # method to call all functions
    def run_analysis(self):
        self.fetch_data()
        self.calculate_portfolio_returns()
        self.plot_results()

# list of tickers
tickers = ["AAPL", "MSFT", "GOOG"]
# time period 5 years
period = "5Y"
# weight of the portfolio
weights = [0.3, 0.4, 0.3]

portfolio_var = PortfolioVaR(tickers, period, weights)
portfolio_var.run_analysis()
