import yfinance as yf
import pandas as pd
import numpy as np

class BetaCalculator:
    def __init__(self, market_symbol, period="5y"):
        self.market_symbol = market_symbol
        self.period = period

    def calculate_beta(self, stock_symbols):
        betas = []
        for stock_symbol in stock_symbols:
            stock_data = yf.download(stock_symbol, period=self.period, progress=False)['Adj Close']
            market_data = yf.download(self.market_symbol, period=self.period, progress=False)['Adj Close']
            stock_returns = stock_data.pct_change().dropna()
            market_returns = market_data.pct_change().dropna()
            
            covariance = np.cov(stock_returns, market_returns)[0, 1]
            variance_market = np.var(market_returns)
            beta = covariance / variance_market
            betas.append(beta)
        
        beta_df = pd.DataFrame({'Stock Symbol': stock_symbols, 'Beta': betas})
        return beta_df

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "BRK-B", "JNJ", "V", "PG", "NVDA"]
market_symbol = "^GSPC"

beta_calculator = BetaCalculator(market_symbol)
betas_df = beta_calculator.calculate_beta(tickers)
betas_df
